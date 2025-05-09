/* jshint esversion: 6 */

// Wait for document to be ready
// Source: https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event
document.addEventListener('DOMContentLoaded', function() {
    // Get the newsletter form element by ID
    // Source: https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById
    const newsletterForm = document.getElementById('newsletter-form');
    
    // Add submit event listener to handle form submission
    // Source: https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            // Prevent the default form submission behavior
            // Source: https://developer.mozilla.org/en-US/docs/Web/API/Event/preventDefault
            e.preventDefault();
            
            // Get the email input value and remove whitespace
            // Source: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trim
            const emailInput = document.getElementById('newsletter-email');
            const email = emailInput.value.trim();
            
            // Validate email is not empty
            if (!email) {
                showMessage('Please enter your email address.', 'danger');
                return;
            }
            
            // Get the CSRF token from cookies - required by Django for POST requests
            // Source: https://docs.djangoproject.com/en/5.0/ref/csrf/
            function getCookie(name) {
                let cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    const cookies = document.cookie.split(';');
                    for (let i = 0; i < cookies.length; i++) {
                        const cookie = cookies[i].trim();
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            const csrftoken = getCookie('csrftoken');
            
            // Show loading state by changing button text and disabling it
            // Source: https://getbootstrap.com/docs/5.0/components/buttons/#disable-state
            const submitButton = document.getElementById('newsletter-submit');
            const originalButtonText = submitButton.innerHTML;
            submitButton.innerHTML = 'Subscribing...';
            submitButton.disabled = true;
            
            // Send AJAX POST request to the server using Fetch API
            // Source: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
            fetch('/newsletter/subscribe/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrftoken
                },
                body: new URLSearchParams({
                    'email': email
                })
            })
            .then(response => response.json()) // Parse JSON response
            .then(data => {
                 // Reset button state after response is received
                submitButton.innerHTML = originalButtonText;
                submitButton.disabled = false;
                
                // Show success or error message based on response status
                // Source: https://getbootstrap.com/docs/5.0/components/alerts/
                if (data.status === 'success') {
                    showMessage(data.message, 'success');
                    emailInput.value = ''; // Clear the input on success
                } else {
                    showMessage(data.message, 'danger');
                }
            })
            .catch(error => {
                // Handle network errors or other exceptions
                // Source: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch
                submitButton.innerHTML = originalButtonText;
                submitButton.disabled = false;
                
                // Show error message
                showMessage('An error occurred. Please try again later.', 'danger');
            });
        });
    }
    
    // Helper function to display messages with Bootstrap alert styling
    // Source: https://getbootstrap.com/docs/5.0/components/alerts/
    function showMessage(message, type) {
        const messageElement = document.getElementById('newsletter-message');
        messageElement.innerHTML = `<div class="alert alert-${type} small">${message}</div>`;
        
        // Automatically clear the message after 5 seconds
        // Source: https://developer.mozilla.org/en-US/docs/Web/API/setTimeout
        setTimeout(() => {
            messageElement.innerHTML = '';
        }, 5000);
    }
});