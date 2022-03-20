/*
Same concept as Python solution
 */

/**
 * @param {string} s
 * @return {boolean}
 */
let isValid = function(s) {
    let lefts = []
    // Loop characters
    for (let i = 0; i < s.length; i ++) {
        let c = s.charAt(i);
        if (isLeft(c))
            lefts.push(s.charAt(i));
        else if (lefts.length === 0)
            return false;
        else if (!isMatching(lefts.pop(), c))
            return false;
    }
    return lefts.length === 0;
};

let isLeft = function(c) {
  if (c === '[' || c === '{' || c === '(')
      return true;
};

let isMatching = function(left, right) {
  if (left === '(' && right === ')')
      return true;
  else if (left === '[' && right === ']')
      return true;
  else if (left === '{' && right === '}')
      return true;
};

export { isValid }