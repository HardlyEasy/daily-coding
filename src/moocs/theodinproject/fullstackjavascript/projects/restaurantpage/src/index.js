import { createHome, removeHome } from './home';
import { createMenu, removeMenu } from './menu';
import { createContact, removeContact } from './contact';
import { createHeader } from './header'

let currentPage = 'home';

function init() {
    createHeader();
    createHome();
}

function tabHandler(buttonId) {
    // Current page same as button press
    if (buttonId.startsWith(currentPage)) {
        return;
    }
    removeTab();
    renderTab(buttonId)
}

function renderTab(buttonId) {
    if (buttonId === 'home-button') {
        console.log("Rendering home tab...");
        createHome();
        currentPage = 'home';
    }
    else if (buttonId === 'menu-button')  {
        console.log("Rendering menu tab...");
        createMenu();
        currentPage = 'menu';
    }
    else if (buttonId === 'contact-button') {
        console.log("Rendering contact tab...");
        createContact();
        currentPage = 'contact';
    }
}

function removeTab() {
    if (currentPage === 'home') {
        console.log("Removing home tab...");
        removeHome();
    }
    else if (currentPage === 'menu') {
        console.log("Removing menu tab...");
        removeMenu();
    }

    else if (currentPage === 'contact') {
        console.log("Removing contact tab...");
        removeContact();
    }
}

init();

// header.js uses tabHandler in event listeners for navigation tabs
export { tabHandler }