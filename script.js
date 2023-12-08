// script.js

document.addEventListener("DOMContentLoaded", function () {
    const privacyLink = document.querySelector("#privacyLink");
    const termsLink = document.querySelector("#termsLink");
    const cookiesLink = document.querySelector("#cookiesLink");
    const modal = document.querySelector("#modal");
    const modalContent = document.querySelector(".modal-content");

    const closeModal = () => {
        modal.style.display = "none";
    };

    privacyLink.addEventListener("click", () => {
        modalContent.innerHTML = "<h2>Política de Privacidade</h2><p>Seu conteúdo aqui...</p>";
        modal.style.display = "block";
    });

    termsLink.addEventListener("click", () => {
        modalContent.innerHTML = "<h2>Termos de Serviço</h2><p>Seu conteúdo aqui...</p>";
        modal.style.display = "block";
    });

    cookiesLink.addEventListener("click", () => {
        modalContent.innerHTML = "<h2>Configurações de Cookies</h2><p>Seu conteúdo aqui...</p>";
        modal.style.display = "block";
    });

    window.addEventListener("click", (event) => {
        if (event.target === modal) {
            closeModal();
        }
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            closeModal();
        }
    });
});
