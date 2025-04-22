/**
 * Toast notification handler for BookLand
 * Provides functions to create and manage toast notifications
 */

// Create a programmatic toast (can be used from JS if needed)
function showToast(message, type = 'info') {
    // Create toast element
    const toastEl = document.createElement('div');
    toastEl.className = `toast align-items-center text-white bg-${type} border-0 mb-2`;
    toastEl.setAttribute('role', 'alert');
    toastEl.setAttribute('aria-live', 'assertive');
    toastEl.setAttribute('aria-atomic', 'true');
    
    // Icon based on message type
    let icon = 'info-circle-fill';
    if (type === 'success') {
        icon = 'check-circle-fill';
    } else if (type === 'danger' || type === 'error') {
        icon = 'exclamation-circle-fill';
    } else if (type === 'warning') {
        icon = 'exclamation-triangle-fill';
    }
    
    // Create toast content
    toastEl.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                <div class="d-flex align-items-center">
                    <i class="bi bi-${icon} me-2"></i>
                    ${message}
                </div>
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
    `;
    
    // Add toast to container
    const container = document.querySelector('.message-container');
    if (container) {
        container.appendChild(toastEl);
        
        // Initialize and show the toast
        const toast = new bootstrap.Toast(toastEl, {
            autohide: true,
            delay: 3000
        });
        
        toast.show();
        
        // Remove toast from DOM after it's hidden
        toastEl.addEventListener('hidden.bs.toast', function() {
            container.removeChild(toastEl);
        });
    }
}