// Toast notification initialization script 
// Source: https://getbootstrap.com/docs/5.3/components/toasts/#javascript

document.addEventListener("DOMContentLoaded", function () {
    // Show all toasts when the page loads
    // Uses jQuery selector to find all toast elements and trigger their show method
    $('.toast').toast('show');
});