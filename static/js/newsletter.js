/* jshint esversion: 6 */

// Wait for document to be ready
document.addEventListener('DOMContentLoaded', function() {
    // Get the newsletter form
    const newsletterForm = document.getElementById('newsletter-form');
    
    // Add submit event listener
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get the email input
            const emailInput = document.getElementById('newsletter-email');
            const email = emailInput.value.trim();
            
            // Check if email is valid
            if (!email) {
                showMessage('Please enter your email address.', 'danger');
                return;
            }
            
            // Get the CSRF token from the cookie
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
            
            // Show loading state
            const submitButton = document.getElementById('newsletter-submit');
            const originalButtonText = submitButton.innerHTML;
            submitButton.innerHTML = 'Subscribing...';
            submitButton.disabled = true;
            
            // Send the subscription request
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
            .then(response => response.json())
            .then(data => {
                // Reset button state
                submitButton.innerHTML = originalButtonText;
                submitButton.disabled = false;
                
                // Show the response message
                if (data.status === 'success') {
                    showMessage(data.message, 'success');
                    emailInput.value = '';
                } else {
                    showMessage(data.message, 'danger');
                }
            })
            .catch(error => {
                // Reset button state
                submitButton.innerHTML = originalButtonText;
                submitButton.disabled = false;
                
                // Show error message
                showMessage('An error occurred. Please try again later.', 'danger');
            });
        });
    }
    
    // Function to show message
    function showMessage(message, type) {
        const messageElement = document.getElementById('newsletter-message');
        messageElement.innerHTML = `<div class="alert alert-${type} small">${message}</div>`;
        
        // Clear message after 5 seconds
        setTimeout(() => {
            messageElement.innerHTML = '';
        }, 5000);
    }
});