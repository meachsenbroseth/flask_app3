document.addEventListener("DOMContentLoaded", () => {
    const pwd = document.querySelector('input[name="password"]');
    if (!pwd) return;

    pwd.addEventListener("input", () => {
        const msg = document.querySelector("#passwordHelp");
        if (!msg) return;

        const v = pwd.value;

        const strong =
            v.length >= 8 &&
            /[A-Z]/.test(v) &&
            /[a-z]/.test(v) &&
            /[0-9]/.test(v) &&
            /[!@#$%^&*(),.\/;\"\'\[\]\-_=+]/.test(v);

        msg.textContent = strong
            ? "Strong password ✔"
            : "Password must include upper, lower, number and special character.";
        
        msg.className = strong ? "form-text text-success" : "form-text text-danger";
    });
});

const darkMode = document.getElementById("darkMode");
const lightMode = document.getElementById("lightMode");
const html = document.documentElement;

// ----- Load saved theme from localStorage -----
const savedTheme = localStorage.getItem("theme");

if (savedTheme === "dark") {
    html.classList.add("dark");
    darkMode.style.display = "none";
    lightMode.style.display = "block";
} else {
    html.classList.remove("dark");
    darkMode.style.display = "block";
    lightMode.style.display = "none";
}

// ----- Click handling -----
document.addEventListener("click", (e) => {

    // Switch to DARK mode
    if (e.target.closest("#darkMode")) {
        html.classList.add("dark");
        localStorage.setItem("theme", "dark");
        darkMode.style.display = "none";
        lightMode.style.display = "block";
    }

    // Switch to LIGHT mode
    if (e.target.closest("#lightMode")) {
        html.classList.remove("dark");
        localStorage.setItem("theme", "light");
        lightMode.style.display = "none";
        darkMode.style.display = "block";
    }

});

