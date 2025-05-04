// Toast notification initialization script for Bootstrap 5
document.addEventListener("DOMContentLoaded", function () {
    // Find all toast elements
    const toastElList = document.querySelectorAll('.toast');
    
    // Initialize each toast and show it
    toastElList.forEach(function (toastEl) {
        const toast = new bootstrap.Toast(toastEl, {
            autohide: true,
            delay: 5000
        });
        toast.show();
    });
    
    // Add click event listeners to all checkout buttons inside toasts
    const checkoutButtons = document.querySelectorAll('.toast .btn-dark');
    checkoutButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            window.location.href = this.getAttribute('href');
        });
    });
});