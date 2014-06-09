$(document).ready(function() {
    // Setting images to hide and first to show
    var images = $("#photos img");
    images.each(function(index, el) {
        if (index == 0) {
            $(this).addClass('main-image');
        } else {
            $(this).addClass('hide');
        }
    });

    // Previous event
    $("#left-arrow").on('click', function(e) {
        var image = $("#photos").find('.main-image');
        var previous_image = image.prev()

        if(previous_image.length > 0) {
            image.toggleClass("main-image hide");
            previous_image.toggleClass("hide main-image");
        } else {
            return false;
        }
    });

    // Next event
    $("#right-arrow").on('click', function(e) {
        var image = $("#photos").find('.main-image');
        var next_image = image.next()

        if(next_image.length > 0) {
            image.toggleClass("main-image hide");
            next_image.toggleClass("hide main-image");
        } else {
            return false;
        }
    });

    // Set shortcuts
    $("body").keydown(function(e) {
        var LEFT = 37;
        var RIGHT = 39;
        if (e.keyCode == LEFT) {
            $("#left-arrow").trigger('click');
        }
        if (e.keyCode == RIGHT) {
            $("#right-arrow").trigger('click');
        }
    });
});
