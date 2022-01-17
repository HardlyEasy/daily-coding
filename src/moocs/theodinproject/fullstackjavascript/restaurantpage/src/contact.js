// Creates contact div HTML
function createContact() {
    let contactDiv = document.createElement("div");
    contactDiv.id = "contact";
    contactDiv.innerHTML = "<h1>Contact</h1>"
    contactDiv.innerHTML += "123-456-7890"
    document.getElementById("main").appendChild(contactDiv)
}

// Removes menu div HTML
function removeContact() {
    document.getElementById("contact").remove();
}


export {
    createContact, removeContact
}