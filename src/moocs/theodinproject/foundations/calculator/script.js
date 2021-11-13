let display = 0;
let first = null;
let operator = null;
let second = null;
const displayText = document.querySelector("#display-text");

// Adds event listeners to all buttons
function prepare() {
    let buttons = document.querySelectorAll("button");
    buttons.forEach((button) => {
        button.addEventListener('click', () => {
            // Handler does actions based on buttonId and buttonClass
            handler(button.id, button.className);
        });
    });
}
prepare();

// Just some basic calculation functions
function add(x, y) {
    return x + y;
}
function subtract(x, y) {
    return x - y;
}
function multiply(x, y) {
    return x * y;
}
function divide(x, y) {
    return x / y;
}
function operate(x, operator, y) {
    let answer;
    switch (operator) {
        case '+':
            answer = add(x, y);
            break;
        case '-':
            answer = subtract(x, y);
            break;
        case '*':
            answer = multiply(x, y);
            break;
        case '/':
            answer = divide(x, y);
    }
    console.log(answer);
}

// Handler does actions based on buttonId and buttonClass
function handler(buttonId, buttonClass) {
    if (buttonId === 'clear') {
        displayClear();
    }
    else if (buttonClass === 'number') {
        displayNumber(buttonId);
    }
    else if (buttonClass === 'operation') {
        first = Number(display);
        displayOperation(buttonId);
    }
}

function displayClear() {
    display = 0;
    displayText.textContent = display;
}

function displayNumber(number) {
    if(display === 0)
        display = number;
    else
        display = display.toString() + number;
    displayText.textContent = display;
}

function displayOperation(buttonId) {
    switch (buttonId) {
        case 'add':
            display = display.toString() + '+';
            break;
        case 'subtract':
            display = display.toString() + '-';
            break;
        case 'multiply':
            display = display.toString() + '*';
            break;
        case 'divide':
            display = display.toString() + '/';
            break;
        case 'remainder':
            display = display.toString() + '%';
    }
    displayText.textContent = display;
}