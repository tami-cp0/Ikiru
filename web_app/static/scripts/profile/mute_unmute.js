$(document).ready(function () {
    $(document).on('click', '#mute_notif', function () {
        if ($(this).attr('src') === '../static/images/mute_notif.png') {
            $(this).attr('src', '../static/images/notification_icon.svg')
        } else {
            $(this).attr('src', '../static/images/mute_notif.png')
        }
    });
});
