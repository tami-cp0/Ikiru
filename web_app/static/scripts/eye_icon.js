$(document).ready(function() {
    $("#togglePassword").click(function() {
        const passwordField = $("#password");
        const fieldType = passwordField.attr("type");

        if (fieldType === "password") {
            passwordField.attr("type", "text");
            $("#togglePassword").attr("src", "../static/images/close_eye.png")
        } else {
            passwordField.attr("type", "password");
            $("#togglePassword").attr("src", "../static/images/open_eye.png")
        }
    });
});
