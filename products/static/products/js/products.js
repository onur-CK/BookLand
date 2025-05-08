/* jshint esversion: 6 */


// Add event listener to sort dropdown to reload page with sort parameters
// Source: https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams
document.getElementById('sort-selector').addEventListener('change', function() {
    var selector = this;
    var currentUrl = new URL(window.location);

    var selectedVal = selector.value;
    if(selectedVal != "reset"){
        // Source: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split
        // Splitting the selected value to extract sort field and direction
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];
        
        // Source: https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams/set
        // Setting URL search parameters for sorting
        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");
    }
    
    // Preserve other parameters (like category, search term, page)
    window.location.replace(currentUrl);
});