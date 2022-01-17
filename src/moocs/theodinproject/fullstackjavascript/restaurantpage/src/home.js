// Creates home div HTML
function createHome() {
    let homeDiv = document.createElement("div");
    homeDiv.id = "home";
    homeDiv.innerHTML = "<h1>Pizza Palace</h1>" +
        "Pizza palace has the best pizza in town!<br><br>"
    homeDiv.innerHTML +=
        '<img src="../img/home.jpg" id="home-img">'
    homeDiv.innerHTML +=
        "<h2>About:</h2>" +
        "We have been open for over 20 years"
    homeDiv.innerHTML +=
        "<h2>Hours:</h2>" +
        "Monday: 9am-5pm<br>" +
        "Tuesday: 9am-5pm<br>" +
        "Wednesday: 9am-5pm<br>" +
        "Thursday: 9am-5pm<br>" +
        "Friday: 9am-5pm"
    homeDiv.innerHTML +=
        "<h2>Location:</h2>" +
        "123 Unreal Road, Weirdsville, Alaska"
    document.getElementById("main").appendChild(homeDiv)
}

// Removes home div HTML
function removeHome() {
    document.getElementById("home").remove();
}

export {
    createHome, removeHome
}