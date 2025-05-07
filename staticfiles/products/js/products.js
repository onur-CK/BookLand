/* jshint esversion: 6 */

// Add event listener to sort dropdown to reload page with sort parameters
document.getElementById('sort-selector').addEventListener('change', function() {
    var selector = this;
    var currentUrl = new URL(window.location);

    var selectedVal = selector.value;
    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];
        
        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");
    }
    
    // Preserve other parameters (like category, search term, page)
    window.location.replace(currentUrl);
});