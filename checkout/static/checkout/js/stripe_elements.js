/*
    Core checkout functionality using Stripe Elements
    Source: https://stripe.com/docs/payments/accept-a-payment
*/

// Get Stripe publishable key from data attribute
const stripePublicKey = document.getElementById('id_stripe_public_key').text.slice(1, -1);
// Get client secret from data attribute
const clientSecret = document.getElementById('id_client_secret').text.slice(1, -1);

// Initialize Stripe with publishable key
const stripe = Stripe(stripePublicKey);
// Create an instance of Stripe Elements
const elements = stripe.elements();

// Create and customize the card Element
const style = {
    base: {
        color: '#000',
        fontFamily: '"Segoe UI", "Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create a card Element and mount it to the specified DOM element
const card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card Element
card.addEventListener('change', function (event) {
    const errorDiv = document.getElementById('card-errors');
    if (event.error) {
        // Show validation error to user
        const html = `
            <span class="icon" role="alert">
                <i class="bi bi-exclamation-circle"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        errorDiv.innerHTML = html;
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
const form = document.getElementById('payment-form');
form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    // Disable the submit button to prevent repeated clicks
    card.update({ 'disabled': true});
    document.getElementById('submit-button').disabled = true;
    
    // Show loading overlay
    document.getElementById('payment-processing-overlay').classList.remove('d-none');
    
    // Get the value of the save_info checkbox
    const saveInfo = Boolean(document.getElementById('id-save-info').checked);
    
    // Get the CSRF token value from the form input
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    // Create an object to pass to the view
    const postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    
    // Send POST request to the cache_checkout_data URL
    const url = '/checkout/cache_checkout_data/';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken,
        },
        body: new URLSearchParams(postData)
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        if (data.error) {
            // If there's an error, display it to the user and re-enable the form
            document.getElementById('payment-processing-overlay').classList.add('d-none');
            card.update({ 'disabled': false});
            document.getElementById('submit-button').disabled = false;
            document.getElementById('card-errors').textContent = data.error;
        } else {
            // If caching checkout data was successful, confirm the card payment
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: document.getElementById('id_full_name').value,
                        phone: document.getElementById('id_phone_number').value,
                        email: document.getElementById('id_email').value,
                        address:{
                            line1: document.getElementById('id_street_address').value,
                            line2: document.getElementById('id_apartment').value,
                            city: document.getElementById('id_city').value,
                            country: document.getElementById('id_country').value,
                            postal_code: document.getElementById('id_postal_code').value,
                        }
                    }
                },
                shipping: {
                    name: document.getElementById('id_full_name').value,
                    phone: document.getElementById('id_phone_number').value,
                    address: {
                        line1: document.getElementById('id_street_address').value,
                        line2: document.getElementById('id_apartment').value,
                        city: document.getElementById('id_city').value,
                        country: document.getElementById('id_country').value,
                        postal_code: document.getElementById('id_postal_code').value,
                    }
                },
            }).then(function(result) {
                if (result.error) {
                    // If there's an error in the payment processing, display it and re-enable the form
                    const errorDiv = document.getElementById('card-errors');
                    const html = `
                        <span class="icon" role="alert">
                            <i class="bi bi-exclamation-circle"></i>
                        </span>
                        <span>${result.error.message}</span>
                    `;
                    errorDiv.innerHTML = html;
                    
                    // Hide loading overlay and re-enable form
                    document.getElementById('payment-processing-overlay').classList.add('d-none');
                    card.update({ 'disabled': false});
                    document.getElementById('submit-button').disabled = false;
                } else {
                    // If payment processing was successful, submit the form
                    if (result.paymentIntent.status === 'succeeded') {
                        form.submit();
                    }
                }
            });
        }
    }).catch(function(error) {
        // Log any error to the console and re-enable the payment form
        console.error('Error:', error);
        document.getElementById('payment-processing-overlay').classList.add('d-none');
        card.update({ 'disabled': false});
        document.getElementById('submit-button').disabled = false;
    });
});