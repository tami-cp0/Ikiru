$(document).ready(function () {
    $(document).on('click', '.save-button', function (e) {
        const saveButton = $(this);

        if (saveButton.css('fill') === 'none') {
            saveButton.css('fill', 'var(--primary)');
            saveButton.find('path').css('stroke', 'var(--primary)');
        } else {
            saveButton.css('fill', 'none');
            $(saveButton).find('path').css('stroke', 'var(--grey)');
        }
    });
});
