// script.js

document.addEventListener("DOMContentLoaded", function () {
  const cookieBanner = document.getElementById("cookie-banner");
  const acceptCookiesBtn = document.getElementById("accept-cookies");
  const declineCookiesBtn = document.getElementById("decline-cookies");

  // Check if the user has already accepted or declined cookies
  if (!localStorage.getItem("cookieConsent")) {
    cookieBanner.style.display = "block"; // Show banner if no consent is found
  }

  // Hide the banner with animation after clicking accept/decline
  function hideBanner() {
    cookieBanner.classList.add("hide");
    setTimeout(() => {
      cookieBanner.style.display = "none"; // Completely hide after animation
    }, 500); // Match the animation duration
  }

  // Accept cookies
  acceptCookiesBtn.addEventListener("click", function () {
    localStorage.setItem("cookieConsent", "accepted");
    hideBanner(); // Hide banner after accepting
  });

  // Decline cookies
  declineCookiesBtn.addEventListener("click", function () {
    localStorage.setItem("cookieConsent", "declined");
    hideBanner(); // Hide banner after declining
  });
});
