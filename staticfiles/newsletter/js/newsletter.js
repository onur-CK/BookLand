document.addEventListener('DOMContentLoaded', function() {
    const newsletterForm = document.getElementById('newsletter-form');
    
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const email = document.getElementById('newsletter-email').value;
            const messageDiv = document.getElementById('newsletter-message');
            const submitButton = document.getElementById('newsletter-submit');
            
            // Disable button during submission
            submitButton.disabled = true;
            submitButton.innerHTML = 'Subscribing...';
            
            fetch('/newsletter/subscribe/', {
                method: 'POST',
                body: JSON.stringify({ email: email }),
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    messageDiv.className = 'mt-2 text-success';
                    messageDiv.textContent = data.message;
                    document.getElementById('newsletter-email').value = '';
                } else {
                    messageDiv.className = 'mt-2 text-danger';
                    messageDiv.textContent = data.message;
                }
            })
            .catch(error => {
                messageDiv.className = 'mt-2 text-danger';
                messageDiv.textContent = 'An error occurred. Please try again.';
                console.error('Error:', error);
            })
            .finally(() => {
                // Re-enable button
                submitButton.disabled = false;
                submitButton.innerHTML = 'Subscribe';
            });
        });
    }
});