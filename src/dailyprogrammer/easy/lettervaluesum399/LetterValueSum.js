let CHALLENGE_ARR = ["", "a", "z", "cab",
    "excellent", "microspectrophotometries"]

function challenge() {
    for(let i = 0; i < CHALLENGE_ARR.length; i++) {
        let word = CHALLENGE_ARR[i];
        let totalSum = letterSum(word);
        console.log("lettersum(\"" + word + "\") => " + totalSum);
    }
}

function letterSum(word) {
    let totalSum = 0;
    for(let j = 0; j < word.length; j++) {
        totalSum += word.charCodeAt(j) - "`".charCodeAt(0);
    }
    return totalSum;
}

challenge();