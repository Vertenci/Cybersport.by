document.addEventListener("DOMContentLoaded", function () {
    const loader = document.getElementById("loader");

    loader.style.display = "flex";

    window.addEventListener("load", function () {
        loader.style.display = "none";
    });
});