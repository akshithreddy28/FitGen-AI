window.addEventListener("scroll", function () {
    const navbar = document.querySelector(".navbar");
    if (window.scrollY > 50) {
        navbar.style.boxShadow = "0 4px 10px rgba(0,0,0,0.2)";
    } else {
        navbar.style.boxShadow = "none";
    }

});

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

const heroButton = document.querySelector(".btn-success");
if (heroButton) {
    heroButton.addEventListener("mouseover", function () {
        heroButton.style.transform = "scale(1.05)";
    });
    heroButton.addEventListener("mouseout", function () {
        heroButton.style.transform = "scale(1)";
    });
}

const featureCards = document.querySelectorAll(".feature-box");
featureCards.forEach(card => {
    card.addEventListener("mouseenter", () => {
        card.style.transform = "translateY(-8px)";
    });
    card.addEventListener("mouseleave", () => {
        card.style.transform = "translateY(0)";
    });
});
window.onload = function () {
    console.log("Welcome to FitGen AI");
};