$(document).ready(function () {
    $(document).on('click', '.switch-button', function () {
        const buttonText = $(this).find('p');

        if (buttonText.text() === 'Public') {
            buttonText.text('Anonymous');
        } else {
            buttonText.text('Public');
        }

        // console.log('Clicked on switch button');
    });
});
