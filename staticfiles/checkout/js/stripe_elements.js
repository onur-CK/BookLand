/* jshint esversion: 6 */
/* global Stripe */

/*
 * Core checkout functionality using Stripe Elements with simplified UI
 * Source: https://stripe.com/docs/payments/accept-a-payment
 */

// Get Stripe publishable key and client secret from hidden divs
const stripePublicKey = document.getElementById('stripe-public-key').textContent.trim();
const clientSecret = document.getElementById('client-secret').textContent.trim();

// Initialize Stripe with publishable key
const stripe = Stripe(stripePublicKey);

// Create an instance of Stripe Elements
const elements = stripe.elements();

// Style the card Element with clean design
const style = {
    base: {
        color: '#32325d',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
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

// Create card Element with zipCode set to false
const card = elements.create('card', {
    style: style
});

// Mount card element to the DOM
card.mount('#card-element');

// Handle real-time validation errors on the card Element
card.addEventListener('change', function(event) {
    const errorDiv = document.getElementById('card-errors');
    if (event.error) {
        // Show validation error to user
        const html = `
            <span role="alert">
                <i class="bi bi-exclamation-circle"></i>
                ${event.error.message}
            </span>
        `;
        errorDiv.innerHTML = html;
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
const form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Disable the submit button to prevent repeated clicks
    card.update({ 'disabled': true });
    document.getElementById('submit-button').disabled = true;
    
    // Show loading overlay
    document.getElementById('payment-processing-overlay').classList.remove('d-none');
    
    // Get save info preference (only if the element exists)
    const saveInfoEl = document.getElementById('id-save-info');
    const saveInfo = saveInfoEl ? saveInfoEl.checked : false;
    
    // Get the CSRF token
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    // Create data to post to the backend
    const postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    
    // URL for the cache_checkout_data view
    const url = '/checkout/cache_checkout_data/';
    
    // Post data to the backend using fetch API
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken,
        },
        body: new URLSearchParams(postData)
    })
    .then(function(response) {
        if (response.ok) {
            // Confirm card payment if caching was successful
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: document.getElementById('id_full_name').value,
                        phone: document.getElementById('id_phone_number').value,
                        email: document.getElementById('id_email').value,
                        address:{
                            line1: document.getElementById('id_street_address').value,
                            line2: document.getElementById('id_apartment').value || '',
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
                        line2: document.getElementById('id_apartment').value || '',
                        city: document.getElementById('id_city').value,
                        country: document.getElementById('id_country').value,
                        postal_code: document.getElementById('id_postal_code').value,
                    }
                },
            }).then(function(result) {
                if (result.error) {
                    // If payment processing failed, show the error
                    const errorDiv = document.getElementById('card-errors');
                    const html = `
                        <span role="alert">
                            <i class="bi bi-exclamation-circle"></i>
                            ${result.error.message}
                        </span>
                    `;
                    errorDiv.innerHTML = html;
                    
                    // Hide loading overlay and re-enable form
                    document.getElementById('payment-processing-overlay').classList.add('d-none');
                    card.update({ 'disabled': false });
                    document.getElementById('submit-button').disabled = false;
                } else {
                    // If payment processing succeeded, submit the form
                    if (result.paymentIntent.status === 'succeeded') {
                        form.submit();
                    }
                }
            });
        } else {
            // If caching failed, reload the page
            location.reload();
        }
    })
    .catch(function(error) {
        // Log errors to console and re-enable the form
        console.error('Error:', error);
        document.getElementById('payment-processing-overlay').classList.add('d-none');
        card.update({ 'disabled': false });
        document.getElementById('submit-button').disabled = false;
    });
});