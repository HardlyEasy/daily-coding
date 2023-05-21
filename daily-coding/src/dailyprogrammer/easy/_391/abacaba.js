
function sequencer(n) {
    //given number of iterations, returns final sequence
    seq = "";
    for (let i = 1; i <= n; i++) {
        middleAscii = 'a'.charCodeAt(0) + i - 1;
        middle = String.fromCharCode(middleAscii);
        seq = seq + middle + seq;
    }
    return seq;
}

function test() {
    console.log('a'.charCodeAt(0) + 1);
    console.log(String.fromCharCode(98));
}

console.log(sequencer(5));
test();