
document.addEventListener("DOMContentLoaded", function () {

    // Automatically display the current year
    const year = document.getElementById("year");
    year.textContent = new Date().getFullYear();

    // Back-to-top button
    const topButton = document.getElementById("topButton");

    window.addEventListener("scroll", function () {
        if (window.scrollY > 300) {
            topButton.classList.add("show");
        } else {
            topButton.classList.remove("show");
        }
    });

    // Scroll to the top when the button is clicked
    topButton.addEventListener("click", function () {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });

    // Smooth scrolling for internal navigation links
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
        link.addEventListener("click", function (event) {
            const targetId = this.getAttribute("href");
            const target = document.querySelector(targetId);

            if (target) {
                event.preventDefault();
                target.scrollIntoView({
                    behavior: "smooth"
                });
            }
        });
    });

    console.log("Data Science Portfolio is ready!");
});
