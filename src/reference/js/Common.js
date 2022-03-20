// I'm aware of these basics, but the grammar/spelling gets forgotten

// LOOPS, FUNCTIONS
for (let i = 0; i < 2; i++) {
    console.log(i) // 0, 1
}

let i = 2;
while (i > 0) {
    console.log(i) // 2, 1
    i--;
}

function myFunc(i) {
    console.log("My func" + i)
}

myFunc(i)

const add = (a, b) => {
    console.log(a.toString() +  ' + ' + b.toString() + ' = ' + (a + b));
    return a + b;
}

add(1, 2)

// ARRAYS, OBJECTS
const a1 = [0]
a1.push(1) // const is mutable
console.log(a1)
a1[3] = 3
console.log(a1)
// a1 = 0  // const var cannot be reassigned

const person = {
    name: 'Bob',
    age: 20
}

const personFactory = (name, age) => {
    const sayHello = () => console.log('hello!');
    return {name, age, sayHello}
}

const anna = personFactory('Anna', 25)

console.log(person)
console.log(anna)