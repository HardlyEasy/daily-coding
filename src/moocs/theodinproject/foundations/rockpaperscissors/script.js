// Old code from popup version of game
/*
function playerPlay() {
    let move = prompt("Enter move: ", "rock")
    move = move.toLowerCase()
    return move
}
*/

function computerPlay() {
    let i = Math.floor(Math.random() * 3)
    switch(i) {
        case 0: return "rock"
        case 1: return "paper"
        case 2: return "scissors"
    }
}

function playRound(playerSelection, computerSelection) {
    let tie = false
    let playerWon = false
    let computerWon = false
    if(playerSelection === "rock") {
        switch(computerSelection) {
            case "rock": 
                tie = true
                break
            case "paper": 
                computerWon = true
                break
            case "scissors": 
                playerWon = true
        }
    }
    else if (playerSelection === "paper") {
        switch(computerSelection) {
            case "rock": 
                playerWon = true
                break
            case "paper": 
                tie = true
                break
            case "scissors": 
                computerWon = true
        }
    }
    else if (playerSelection === "scissors") {
        switch(computerSelection) {
            case "rock": 
                computerWon = true
                break
            case "paper": 
                playerWon = true
                break
            case "scissors": 
                tie = true
        }
    }
    if (tie === true) {
        return "Tie! " + playerSelection + " ties " + computerSelection
    }
    else if (playerWon === true) {
        return "You win! " + playerSelection + " beats " + computerSelection
    }
    else if (computerWon === true) {
        return "You lose! " + playerSelection + " loses " + computerSelection
    }
}

// Old code from popup version of game
/*
function game(numRounds) {
    let playerScore = 0
    let computerScore = 0
    let playerSelection
    let computerSelection
    let resultMsg
    for(let i = 0; i < numRounds; i++) {
        playerSelection = playerPlay()
        computerSelection = computerPlay()
        resultMsg = playRound(playerSelection, computerSelection)
        console.log(resultMsg)
        if(resultMsg.includes("win"))
            playerScore++
        else if(resultMsg.includes("lose"))
            computerScore++
    }
    if(playerScore > computerScore)
        console.log("Player wins! " + playerScore + ":" + computerScore)
    else if(computerScore > playerScore)
        console.log("Computer wins! " + playerScore + ":" + computerScore)
    else if(computerScore === playerScore)
        console.log("Tie! " + playerScore + ":" + computerScore)
}
*/
// buttons.forEach(myFunction)
//  array.forEach(function(currentValue, index, arr), thisValue)

let playerScore = 0;
let computerScore = 0;

// const prevents object reference from changing, not value itself
const results = document.querySelector('#game-results');
const h1 = document.createElement('h1');
h1.appendChild(document.createTextNode('Player Score : Computer Score'));
results.appendChild(h1);
const h2 = document.createElement('h2');
h2.appendChild(document.createTextNode(playerScore + " : " + computerScore));
results.appendChild(h2);
const h3 = document.createElement('h3');
h3.appendChild(document.createTextNode('Play 5 games to win'));
results.appendChild(h3);

const buttons = document.querySelectorAll('button');
buttons.forEach((button) => {
    button.addEventListener('click', () => {
        if (playerScore === 5 || computerScore === 5)
            return;
        let resultMsg = playRound(button.id, computerPlay());
        h3.innerText = resultMsg;
        if(resultMsg.includes("win"))
            playerScore++
        else if(resultMsg.includes("lose"))
            computerScore++
        h2.innerText = playerScore + " : " + computerScore;
        if (playerScore === 5)
            h3.innerText = "Player wins!";
        else if (computerScore === 5)
            h3.innerText = "Computer wins!";
    });
});

