// Creates menu div HTML
function createMenu() {
    let menuDiv = document.createElement("div");
    menuDiv.id = "menu";
    menuDiv.innerHTML = "<h1>Menu</h1>";
    menuDiv.innerHTML += '<img src="../img/menu1.jpg" id="home-img">'
    menuDiv.innerHTML +=
        "<p>No topping &nbsp;$1.00</p>" +
        "<p>1 topping &nbsp&nbsp$1.50</p>" +
        "<p>2+ toppings $2.00</p>"
    document.getElementById("main").appendChild(menuDiv)
}

// Removes menu div HTML
function removeMenu() {
    document.getElementById("menu").remove();
}

export {
    createMenu, removeMenu
}