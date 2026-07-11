// ===============================
// FitGen AI - Dashboard JavaScript
// ===============================

// Dashboard Loaded
window.addEventListener("load", () => {

    console.log("Dashboard Loaded Successfully");

    animateCards();

    animateNumbers();

    showDate();

});


// ===============================
// Card Animation
// ===============================

function animateCards() {

    const cards = document.querySelectorAll(".result-card");

    cards.forEach((card, index) => {

        card.style.opacity = "0";

        card.style.transform = "translateY(30px)";

        setTimeout(() => {

            card.style.transition = "0.5s";

            card.style.opacity = "1";

            card.style.transform = "translateY(0)";

        }, index * 200);

    });

}


// ===============================
// Number Animation
// ===============================

function animateNumbers() {

    const numbers = document.querySelectorAll(".animate-number");

    numbers.forEach(number => {

        const target = Number(number.innerText);

        let count = 0;

        const speed = target / 50;

        const update = () => {

            count += speed;

            if (count < target) {

                number.innerText = Math.floor(count);

                requestAnimationFrame(update);

            }

            else {

                number.innerText = target;

            }

        };

        update();

    });

}


// ===============================
// Date & Time
// ===============================

function showDate() {

    const today = new Date();

    const options = {

        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric"

    };

    const date = today.toLocaleDateString("en-IN", options);

    const dateBox = document.getElementById("currentDate");

    if (dateBox) {

        dateBox.innerHTML = date;

    }

}


// ===============================
// Back Button Confirmation
// ===============================

function goHome() {

    if (confirm("Go back to Home Page?")) {

        window.location.href = "/";

    }

}