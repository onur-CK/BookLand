/* jshint esversion: 6 */

// Initialize all modals when the page loads
document.addEventListener('DOMContentLoaded', function() {
    // Check if testimonial content exceeds container height and add truncated class if needed
    document.querySelectorAll('.testimonial-content').forEach(function(content) {
        // If the scroll height is greater than the client height, it means content is overflowing
        if (content.scrollHeight > content.clientHeight) {
            content.classList.add('truncated');
        } else {
            content.classList.remove('truncated');
        }
    });
});