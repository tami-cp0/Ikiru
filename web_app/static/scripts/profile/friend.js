$(document).ready(function () {
    $(document).on('click', '.add-friend', function () {
        const buttonText = $(this).find('p');

        if (buttonText.text() === 'Add Friend') {
            buttonText.text('Unfriend');
            $(this).find('img').attr('src', '../static/images/unfriend.svg')
        } else {
            buttonText.text('Add Friend');
            $(this).find('img').attr('src', '../static/images/friend_icon.svg')
        }
    });
});
