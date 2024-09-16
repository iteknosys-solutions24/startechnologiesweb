document.addEventListener('DOMContentLoaded', function () {
    var acceptButton = document.getElementById('accept-cookies');
    var rejectButton = document.getElementById('reject-cookies');
    var consentBanner = document.getElementById('cookie-consent');

    if (acceptButton) {
        acceptButton.addEventListener('click', function () {
            document.cookie = "cookie_consent=accepted; max-age=31536000; path=/";
            consentBanner.style.display = 'none';
        });
    }

    if (rejectButton) {
        rejectButton.addEventListener('click', function () {
            document.cookie = "cookie_consent=rejected; max-age=31536000; path=/";
            consentBanner.style.display = 'none';
        });
    }
});
