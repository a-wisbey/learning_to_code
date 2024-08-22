let raceNumber = Math.floor(Math.random() * 1000);

// Create a variable that indicates whether a runner registered early or not. Set it equal to a Boolean value
let registeredEarly = true;

// Create a variable for the runner's age and set it equal to a number
const age = 18;

// Create a control flow statement that checks whether the runner is an adult AND registered early.
if (age > 18 && registeredEarly === true) {
    raceNumber = raceNumber + 1000;
}

// Create a separate control flow statement that checks age and registration time to determine race time.
if (age > 18 && registeredEarly === true) {
    let raceTime = '9:30am';
    console.log(`Your race time is ${raceTime}!`);
    console.log(`Your race number is: ${raceNumber}`);
} 
// Else statement for if the runner is over 18 and did not register early
else if (age > 18 && !registeredEarly) {
    let raceTime = '11:00am';
    console.log(`Your race time is ${raceTime} and your race number is ${raceNumber}`);
} 
// Log a statement for people under 18, telling them they'll race at 12:30pm
else if (age < 18) {
    sole.log(`The Youth race is at 12:30pm. Your race number is ${raceNumber}`);
} 
// Add an 'else' statement that logs a statement to the console telling the runner to see the registration desk if they're exactly 18
else if (age === 18) {  // Use '===' for comparison
    sole.log(`Report to the registration desk.`);
}
