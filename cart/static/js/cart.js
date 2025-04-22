// Update quantity on click
$('.update-link').click(function(e) {
    e.preventDefault();
    $(this).closest('.update-form').submit();
});

// Remove item and reload on click
$('.remove-item').click(function(e) {
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/cart/remove/${itemId}/`;

    $.post(url)
     .done(function() {
         location.reload();
     });
});