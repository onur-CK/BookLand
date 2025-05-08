/* jshint esversion: 6 */

// Wait for document to be ready
document.addEventListener('DOMContentLoaded', function() {
    // Get the newsletter form element by ID
    const newsletterForm = document.getElementById('newsletter-form');
    
    // Add submit event listener to handle form submission
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            // Prevent the default form submission behavior
            e.preventDefault();
            
            // Get the email input value and remove whitespace
            const emailInput = document.getElementById('newsletter-email');
            const email = emailInput.value.trim();
            
            // Validate email is not empty
            if (!email) {
                showMessage('Please enter your email address.', 'danger');
                return;
            }
            
            // Simple email validation using regex
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                showMessage('Please enter a valid email address.', 'danger');
                return;
            }
            
            // Get the CSRF token from cookies - required by Django for POST requests
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
            const submitButton = document.getElementById('newsletter-submit');
            const originalButtonText = submitButton.innerHTML;
            submitButton.innerHTML = 'Subscribing...';
            submitButton.disabled = true;
            
            // Prepare form data
            const formData = new FormData();
            formData.append('email', email);
            
            // Send AJAX POST request to the server using Fetch API
            fetch('/newsletter/subscribe/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                // Reset button state after response is received
                submitButton.innerHTML = originalButtonText;
                submitButton.disabled = false;
                
                // Show success or error message based on response status
                if (data.status === 'success') {
                    showMessage(data.message, 'success');
                    emailInput.value = ''; // Clear the input on success
                } else {
                    showMessage(data.message, 'danger');
                }
            })
            .catch(error => {
                // Handle network errors or other exceptions
                console.error('Error:', error);
                submitButton.innerHTML = originalButtonText;
                submitButton.disabled = false;
                
                // Show error message
                showMessage('An error occurred. Please try again later.', 'danger');
            });
        });
    }
    
    // Helper function to display messages with Bootstrap alert styling
    function showMessage(message, type) {
        const messageElement = document.getElementById('newsletter-message');
        messageElement.innerHTML = `<div class="alert alert-${type} small">${message}</div>`;
        
        // Automatically clear the message after 5 seconds
        setTimeout(() => {
            messageElement.innerHTML = '';
        }, 5000);
    }
});