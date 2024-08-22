let userName = " ";

// Create a ternary expression that decides wwhat to do if the user enters a name or not.
userName.trim() ? console.log(`Hello, ${userName.trim()}!`) : console.log('Hello!');


// Create a variable named userQuestion. The value of the variable should be a string that is the question the user wants to ask the Magic Eight Ball.

let userQuestion = "Will it rain tomorrow?";

// Write a console.log() for the userQuestion, stating what was asked. 

console.log(userQuestion); // not sure this is right

// Generate a random number between 0 and 7
let randomNumber = Math.floor(Math.random() * 8);

// Create one more variable named eightBall, and set it equal to an empty string. 
let eightBall = " ";

// Create a control flow that takes in the randomNumber we made in step 5, and then assigns eightBall to a reply that a Magic Eight Ball would return. 
switch (randomNumber) {
  case 0:
    eightBall = 'It is certain';
    break;
  case 1:
    eightBall = 'It is decidedly so';
    break;
  case 2:
    eightBall = 'Reply hazy try again';
    break;
  case 3:
    eightBall = 'Cannot predict now';
    break;
  case 4:
    eightBall = 'Do not count on it';
    break;
  case 5:
    eightBall = 'My sources say no';
    break;
  case 6:
    eightBall = 'Outlook not so good';
    break;
  case 7:
    eightBall = 'Signs point to yes';
    break;
  default:
    eightBall = 'My psychic powers are broken at this time. Try again.';
    break;
}

// Log the eightBall response
console.log(eightBall);

// Now amend the above switch statement to an if/else if/else statement

if (randomNumber === 0) {
  eightBall = 'It is certain';
} else if (randomNumber === 1) {
    eightBall = 'It is decidedly so';
  } else if (randomNumber === 2) {
    eightBall = 'Reply hazy try again';
  } else if (randomNumber === 3) {
    eightBall = 'Cannot predict now';
  } else if (randomNumber === 4) {
    eightBall = 'Do not count on it';
  } else if (randomNumber === 5) {
    eightBall = 'My sources say no';
  } else if (randomNumber === 6) {
    eightBall = 'Outlook not so good';
  } else if (randomNumber === 7) {
    eightBall = 'Signs point to yes';
  } else { eightBall = 'My psychic powers are broken at this time. Try again.';
  }

// Log the eightBall response
console.log(eightBall);
