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

//modal view

let currentIndex = 0;
const images = document.querySelectorAll(".gallery-image");

function openModal(image) {
  currentIndex = Array.from(images).indexOf(image);
  showModal(image.src, image.alt);
}

function showModal(src, alt) {
  const modal = document.getElementById("imageModal");
  const modalImage = document.getElementById("modalImage");
  const caption = document.getElementById("caption");

  modal.style.display = "flex"; // Use flex to center the modal
  modalImage.src = src;
  caption.innerHTML = alt;
}

function closeModal() {
  const modal = document.getElementById("imageModal");
  modal.style.display = "none";
}

function changeImage(direction) {
  currentIndex = (currentIndex + direction + images.length) % images.length; // Loop back to start or end
  showModal(images[currentIndex].src, images[currentIndex].alt);
}

// Close the modal when clicking on the close button
document.querySelector(".close").onclick = closeModal;

// Close the modal when clicking outside of the image
document.getElementById("imageModal").onclick = function (event) {
  if (event.target === this) {
    closeModal();
  }
};

//Scroll Top

window.onscroll = function () {
  const button = document.getElementById("topButton");
  if (document.body.scrollHeight - window.scrollY <= window.innerHeight + 100) {
    button.style.display = "block"; // Show button when near bottom
  } else {
    button.style.display = "none"; // Hide button otherwise
  }
};
