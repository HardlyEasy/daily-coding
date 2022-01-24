import { tabHandler } from './index'

// Creates header div HTML
function createHeader() {
    let headerDiv = document.getElementById("header");
    let headerHtml =
        "<button class=\"text-button\" id=\"home-button\">Home</button>\n" +
        "<button class=\"text-button\" id=\"menu-button\">Menu</button>\n" +
        "<button class=\"text-button\" id=\"contact-button\">Contact</button>";
    headerDiv.innerHTML = headerHtml;
    addListeners()
}

// Navigation tab buttons pass button's HTML ids to tabHandler in index.js
function addListeners() {
    let textButtons = document.querySelectorAll(".text-button");
    for (let i = 0; i < textButtons.length; i++) {
        textButtons[i].addEventListener("click", function() {
            tabHandler(textButtons[i].id)
        });
    }
}

export {
    createHeader
};