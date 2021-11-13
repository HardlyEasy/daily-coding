const wrapper = document.querySelector('#wrapper');

// Toggle drawing
let toggleDraw = true;
window.addEventListener('keydown', (event) => {
    if ((event.key === 'd' || event.key === "D") && toggleDraw === true ) {
        toggleDraw = false;
        console.log("draw off");
    }
    else {
        toggleDraw = true;
        console.log("draw on");
    }
})

function makeGridItems(gridSize) {
    const container = document.createElement('div');
    container.id = "grid-container";
    container.setAttribute('style', 'grid-template-columns: repeat(' +  gridSize + ', 1fr);');
    // Create 4x4, 16 div size grid
    for(let i = 1; i <= (gridSize * gridSize); i++) {
        const div = document.createElement("div");
        div.classList.add("grid-item");
        div.id = "grid-item" + i;
        //div.textContent = i;
        container.appendChild(div);
    }
    wrapper.appendChild(container);
    // Add mouseover event listeners to all grid-item divs
    let gridItems = document.querySelectorAll(".grid-item");
    gridItems.forEach((gridItem) => {
        gridItem.addEventListener('mouseover', () => {
            if (toggleDraw === true)
                gridItem.setAttribute('style', 'background-color:black;');
        });
    });
    
}


function clearFunction() {
    const gridItems = document.querySelectorAll(".grid-item");
    for (let i = 0; i < gridItems.length; i++) {
        gridItems[i].style.backgroundColor = "lightblue";
    }
    gridSize = prompt("Enter new grid size");
    console.log(gridSize);
    let container = document.getElementById("grid-container");
    container.remove();
    makeGridItems(gridSize);
}

makeGridItems(16);

// Clear button
const clearButton = document.querySelector("#clear-button");
clearButton.addEventListener('click', clearFunction);