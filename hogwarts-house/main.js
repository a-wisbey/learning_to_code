// create an age variable
const age = 12;

// create a variable that asks for their sorting house
let house = "ravenclaw";

//create an if/else statement that checks if someone is old enough for hogwarts
if (age < 11) {
    console.log(
        "Sorry, you're too young for Hogwarts. Look out for your letter next year."
    );
} else if (age >= 11 && age < 18) {
    console.log(
        "You're of age now, let's get you sorted into your house!"
    );
} else if (age >= 18) {
    console.log(
        "Looks like your owl got lost delivering post - you're too old for Hogwarts now."
    );
} else {
    console.log(
        "Hmm. I cannot determine your age...please try again"
    );
}

if (house === "slytherin") {
    console.log(
        "Your house is Slytherin - spare nothing to ensure the good of that which is pure."
    );
} else if (house === "hufflepuff") {
    console.log(
        "Your house is Hufflepuff - nobler than royalty are friends of true loyalty."
    );
} else if (house === "gryffindor") {
    console.log(
        "Your house is gryffindor - where dwell the brave at heart."
    );
} else if (house === "ravenclaw") {
    console.log(
        "Your house is Ravenclaw - wit beyond measure is man's greatest treasure."
    );
} else {
    console.log(
        "Pick a house! (in lowercase with perfect spelling, or you'll break my code"
    );
}
