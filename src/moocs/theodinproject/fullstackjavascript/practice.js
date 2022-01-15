// FUNCTION BINDING
// Functions are bound to context at call time, not declaration time
let person = {
    name: "Person",
    sayHi: function() {
        console.log(`My name is ${this.name}`)
    }
};

// person.printName() executes the function
person.sayHi();
// person.printName is the function itself
setTimeout(person.sayHi, 500);


let animal = {
    name: "Fluffy",
    speak: function(phrase) {
        console.log(`${this.name} says ${phrase}`)
    }
}

// function cat.sayMeow is bound to cat
let speak = animal.speak.bind(animal);
// bound function can be called alone
speak("meow");
// bound function can be passed with context in proper place
setTimeout(speak, 1000, "bark");

animal = {
    name: "Chompers",
    speak: function(phrase) {
        console.log(`${this.name} yells ${phrase}`)
    }
}
// reference to old animal objects speak function
speak("baa")
// reference to new animal object speak function
animal.speak("neigh");

class Pet {
    constructor(name) {
        this.name = name;
    }
    speak() {
        console.log(`${this.name} makes a noise`)
    }
}

class Dog extends Pet {
    bark() {
        console.log(`${this.name} barks`)
    }
}

let doggo = new Dog("Max");
doggo.bark();
doggo.speak();