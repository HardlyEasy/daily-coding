let COINS = [500, 100, 25, 10, 5, 1]

// Gives number of coins needed to make optimal change from money
function change(money) {
    let numCoinsList = []
    for(let i = 0; i < COINS.length; i++) {
        let coin = COINS[i]; // select highest change coin
        let leftover = money % coin;
        let numCoins = Math.floor(money/coin);
        numCoinsList.push(numCoins);
        money = leftover
    }
    let sum = 0
    for(let i = 0; i < numCoinsList.length; i++) {
        sum += numCoinsList[i]
    }
    return sum
}

function main() {
    console.log('change(0) => ' + change(0))
    console.log('change(12) => ' + change(12))
    console.log('change(468) => ' + change(468))
    console.log('change(123456) => ' + change(123456))
}

main();