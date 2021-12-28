let COINS = [500, 100, 25, 10, 5, 1]

function change(money) {
    let num_coins_list = []
    for(let i = 0; i < COINS.length; i++) {
        let coin = COINS[i]; // select highest change coin
        let leftover = money % coin;
        let num_coins = Math.floor(money/coin);
        num_coins_list.push(num_coins);
        money = leftover
    }
    let sum = 0
    for(let i = 0; i < num_coins_list.length; i++) {
        sum += num_coins_list[i]
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