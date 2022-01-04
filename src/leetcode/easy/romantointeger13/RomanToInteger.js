let singlesDict = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}
let doublesDict = {
    'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
    'CD': 400, 'CM': 900
}

/**
 * @param {string} s
 * @return {number}
 */
function romanToInt(s) {
    if (s.length === 1)
        return singlesDict[s]
    let total = 0
    let li = 0, ri = 1 // Left index, right index
    while (li < s.length) {
        if (ri < s.length) { // Guard against out of bounds
            let double = s.substring(li, ri + 1)
            let doubleVal = doublesDict[double]
            if (typeof doubleVal === 'number') { // Double match found
                total += doublesDict[double]
                li += 2
                ri += 2
                continue
            }
        }
        let single = s.substring(li, li + 1)
        total += singlesDict[single]
        li += 1
        ri += 1
    }
    return total
}; // end method romanToInt()

console.log(romanToInt('III'))
console.log(romanToInt('LVIII'))
console.log(romanToInt('MCMXCIV'))