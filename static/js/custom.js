    $(document).on('click', 'a.label', function() {
    if ($(this).popup('is visible')) {
        $(this).popup({
        on: 'click'
        }).popup('hide');
    } else {
    $(this)
       .popup({
            position: "left center",
            html: $(this).data("profile-card"),
            on:'click'
       })
       .popup('show');
    }
});