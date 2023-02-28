const navLinks = document.querySelectorAll(".nav-links__item-d");

navLinks?.forEach((navLink) => {
    navLink?.addEventListener("click", () => {
        navLinks.forEach(({ nextElementSibling: sub }) => {
            sub.style.display = "none";
        })

        const sub = navLink.nextElementSibling;

        sub.style.display = sub.style.display === "block" ? "none" : "block";
    });
});