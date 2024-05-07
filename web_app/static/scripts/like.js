$(document).ready(function () {
    $(document).on('click', '.like-button', function (e) {
        const likeButton = $(this);

        if (likeButton.css('fill') === 'none') {
            likeButton.css('fill', 'var(--like)');
            likeButton.find('path').css('stroke', 'var(--like)');
        } else {
            likeButton.css('fill', 'none');
            $(likeButton).find('path').css('stroke', 'var(--grey)');
        }
    });
});


