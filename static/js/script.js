// ===============================
// FitGen AI - script.js
// ===============================

// Navbar shadow on scroll
window.addEventListener("scroll", function () {

    const navbar = document.querySelector(".navbar");

    if (window.scrollY > 50) {
        navbar.style.boxShadow = "0 4px 10px rgba(0,0,0,0.2)";
    } else {
        navbar.style.boxShadow = "none";
    }

});


// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        if (target) {

            target.scrollIntoView({
                behavior: "smooth"
            });

        }

    });

});


// Hero button animation
const heroButton = document.querySelector(".btn-success");

if (heroButton) {

    heroButton.addEventListener("mouseover", function () {

        heroButton.style.transform = "scale(1.05)";

    });

    heroButton.addEventListener("mouseout", function () {

        heroButton.style.transform = "scale(1)";

    });

}


// Feature card hover animation
const featureCards = document.querySelectorAll(".feature-box");

featureCards.forEach(card => {

    card.addEventListener("mouseenter", () => {

        card.style.transform = "translateY(-8px)";

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform = "translateY(0)";

    });

});


// Welcome message
window.onload = function () {

    console.log("Welcome to FitGen AI");

};