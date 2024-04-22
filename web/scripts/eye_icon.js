$(document).ready(function() {
    $("#togglePassword").click(function() {
        const passwordField = $("#password");
        const fieldType = passwordField.attr("type");

        if (fieldType === "password") {
            passwordField.attr("type", "text");
            $(this).find("img").attr("src", "images/close_eye.png")
        } else {
            passwordField.attr("type", "password");
            $(this).find("img").attr("src", "images/open_eye.png")
        }
    });
});
