$(document).ready(function () {
    $(document).on('click', '#mute_notif', function () {
        if ($(this).attr('src') === 'images/mute_notif.png') {
            $(this).attr('src', 'images/notification_icon.svg')
        } else {
            $(this).attr('src', 'images/mute_notif.png')
        }
    });
});
