/* jshint esversion: 6 */
/* global bootstrap */

document.addEventListener("DOMContentLoaded", function () {
    // Initialize all toasts with the Bootstrap toast method
    var toastElements = document.querySelectorAll('.toast');
    
    // Convert NodeList to Array and create Toast instances
    var toasts = Array.prototype.slice.call(toastElements).map(function (toastEl) {
        return new bootstrap.Toast(toastEl, {
            autohide: true,
            delay: 5000 // Auto-hide after 5 seconds
        });
    });
    
    // Show all toasts
    toasts.forEach(function(toast) {
        toast.show();
    });
});