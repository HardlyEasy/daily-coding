// Returns array of people (name, score) objects
function score(tally) {
    let persons = [
        {name: 'a', score: 0},
        {name: 'b', score: 0},
        {name: 'c', score: 0},
        {name: 'd', score: 0},
        {name: 'e', score: 0},
    ];

    for (let ch of tally) {
        let curr_person; // person object
        for (let i = 0; i < persons.length; i ++) {
            if (persons[i].name == ch.toLowerCase()) {
                curr_person = persons[i]
                break;
            }
        }
        if (ch == ch.toLowerCase())  // tally character is lowercase
            curr_person.score += 1
        else // tally character is uppercase
            curr_person.score -=1

    }
    return persons
} // end score()

// Sorts array of people from highest score to lowest
function sortHighLow(persons) {
    return persons.sort((a, b) => b.score - a.score);
}

function main() {
    tallys = ['abcde', 'dbbaCEDbdAacCEAadcB', 'EbAAdbBEaBaaBBdAccbeebaec'];
    for (let i = 0; i < tallys.length; i++) {
        curr_tally = tallys[i]
        let persons = score(curr_tally)
        console.log(sortHighLow(persons))
    }
} // end main()

main();