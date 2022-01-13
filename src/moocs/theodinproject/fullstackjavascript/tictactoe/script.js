// Model, View, Controller pattern used

// Models
const playerFactory = function(name, symbol) {
    return { name, symbol };
};

const boardModule = (function() {
    const board = ['0', '1', '2', '3', '4', '6', '7', '8', '9'];
    // Update board, return true for success or false
    const update = function(i, player) {
        if (board[i] !== 'X' && board[i] !== 'O') {
            board[i] = player.symbol;
            return true;
        }
        else
            return false;
    };
    // Return list of indexes of win or null
    const getWin = function() {
        // Horizontal
        if (board[0] === board[1] && board[0] === board[2])
            return [0, 1, 2];
        else if (board[3] === board[4] && board[3] === board[5])
            return [3, 4, 6];
        else if (board[6] === board[7] && board[6] === board[8])
            return [6, 7, 8];
        // Vertical
        else if (board[0] === board[3] && board[0] === board[6])
            return [0, 3, 6];
        else if (board[1] === board[4] && board[1] === board[7])
            return [1, 4, 7];
        else if (board[2] === board[5] && board[2] === board[8])
            return [2, 5, 8]
        // Diagonal
        else if (board[0] === board[4] && board[0] === board[8])
            return [0, 4, 8];
        else if (board[2] === board[4] && board[2] === board[6])
            return [2, 4, 6];
        // None
        else
            return null;
    };
    const reset = function() {
        for (let i = 0; i < board.length; i++) {
            board[i] = i.toString();
        }
    }
    return { board, update, getWin, reset };
})();

// View
const viewModule = (function() {
    const gridItems = document.getElementById("board").children;
    const status = document.getElementById("status")
    const init = function () {
        // Tells controller grid item was clicked
        for (let i = 0; i < gridItems.length; i++) {
            gridItems[i].addEventListener("click", function() {
                controlModule.click(i);
            })
        }
        // Show initial player 1 turn status
        status.innerHTML = 'Player X goes first!';
    };
    // Update X or O in HTML
    const update = function(i, player) {
        let gridItem = document.getElementById("i" + i);
        gridItem.innerHTML = boardModule.board[i];
        status.innerHTML = player.name + ' turn';
    };
    // Show which player won
    const statusWin = function(player) {
        status.innerHTML = player.name + ' won!!!';
    };
    const statusTie = function() {
        status.innerHTML = 'Tied!!!';
    }
    const reset = function() {
        for (let i = 0; i < gridItems.length; i++) {
            let gridItem = document.getElementById("i" + i);
            gridItem.innerHTML = '';
        }
        status.innerHTML = 'Player X goes first!';
    }
    return { init, update, statusWin, statusTie, reset };
})();

// Controller
const controlModule = (function() {
    const p1 = playerFactory('Player X', 'X');
    const p2 = playerFactory('Player O', 'O');
    // Will be incremented from 1 to 9
    let turn = 1;
    const init = function() {
        viewModule.init();
    };
    // Click is called from View
    const click = function(i) {
        // Game ended
        if (turn === 0) {
            console.log('Winner determined already')
            return;
        }
        let currPlayer = p1;
        if (turn % 2 === 0)
            currPlayer = p2;
        let wasUpdated = boardModule.update(i, currPlayer);
        if (wasUpdated) {
            viewModule.update(i, currPlayer);
            turn++;
            this.handleWin(currPlayer)
            return;
        }
    };
    const handleWin = function(currPlayer) {
        let winIndexes = boardModule.getWin();
        if (winIndexes === null) {
            return;
        }
        viewModule.statusWin(currPlayer);
        turn = 0;
    };
    const reset = function() {
        console.log("Resetting ...")
        boardModule.reset();
        viewModule.reset();
        turn = 1;
    }
    return { init, click, handleWin, reset };
})();

controlModule.init();
document.getElementById("reset-button").addEventListener(
    "click", controlModule.reset);