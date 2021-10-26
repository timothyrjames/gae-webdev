// Slide 19:
// single line comments are easy in Apps Script
// everything following "//" is ignored

// the comment ends at the end of the line

// adding // is an easy way to "block" processing of lines
// console.log("Some text.");


// Slide 20:
/* This is a multiple line comment in Apps Script.
   It can go on for a long time and everything inside of it
   is ignored.  */

/* Multiple line comments start with forward-slash asterisk and end with asterisk forward-slash.

They can span multiple empty lines too.
*/


// Slide 21:
function firstFunction() {
    console.log("Functions don't have to return values.");
}

function secondFunction() {
    console.log("Functions *can* return values, though.");
    return 1;
}

function thirdFunction(a, b, c) {
    console.log("They can also take parameters.");
    return a + b + c;
}

function fourthFunction() {
    console.log("There is also an arguments array that can be used for ");
    console.log("variable numbers of parameters.");
    return arguments.length;
}


// Slide 22:
function whitespace() {
    let x = "One space is alright.";
    let  y  =     "More than one is atypical, but OK too."    ;
    let z =		"That also goes for tabs.";


    let a = "Many blank lines are also OK.";
}


// Slide 24:
function operators() {
    console.log(3 + 3);
    console.log(9 - 4);
    console.log(7 * 6);
    console.log(9 / 4);
    console.log(Math.floor(9 / 4)); 
}


// Slide 26:
function booleanOperators() {
    console.log(3 > 5);
    console.log(3 > 5);
    console.log(12 / 2 == 6);
    console.log(12 / 3 != 4);
    console.log(7 <= 3);
    console.log(4 == 2 * 2 && 2 == 3 / 2);
    console.log(false || true);
    console.log(true && true);

    // In JavaScript, there's the === operator for equivalence in value & type
    console.log(3 == '3');
    console.log(3 === '3');
    console.log(3 != '3');
    console.log(3 !== '3');
}


// Slides: https://docs.google.com/presentation/d/1JXUldBgTZZMV1JY99EyiamWXEau0vd9VDFBpZt47yh0/edit
// Slide 29:
function strings() {

    var s = 'abcdefghijklmnopqrstuvwxyz'
    console.log(s.length);
    console.log(s.charAt(12));
    console.log(s.substring(-1));    // anything < 0 will be treated as 0
    console.log(s.substring(2, 4));
    console.log(s.substring(13));
    console.log(s.substring(0, 8));
    console.log(s.substring(-1, 3)); // again, < 0 becomes 0.
    console.log(s.substring(0, -4)); // this basically does nothing.

}


// Slide 33:
function variables() {

    // in JavaScript, we use "var" to declare variables
    var num = 4;
    var word = 'cats';

    // "let" declares a variable, but with checking.  Probably better.
    let otherNum = 3.2;

    // for example, try uncommenting the following line:
    // let num = 5.0;
    
    // in JavaScript, if we don't declare a variable, it becomes global.
    sentence = num + ' ' + word;

    console.log(sentence);
}


// Slide 34:
function types() {
  
    console.log(typeof(true));
    console.log(typeof(3));
    console.log(typeof(98.6));
    console.log(typeof('A string'));
    console.log(typeof(null));

    // probably as important in JavaScript is instanceof - see Objects.
}


// Slide 37:
function ifStatements() {
    let x = 10;
    let y = 13;

    let num = prompt('Enter a number.');

    if (num > 1000) {
        console.log('That\'s a really big number!.');
        if (num > 10000) {
        console.log('That\'s a really really big number!');
        }
    }

    num = prompt('Enter another number.');

    if (num < 0) {
        console.log(num + ' is negative.');
    } else if (num > 0) {
        console.log(num + ' is positive.');
    } else {
        console.log(num + ' is zero.');
    }
}


// Slide 39:
function whileLoops() {
    let i = 0;
    while (i < 10) {
        console.log(i);
        i++;                // JavaScript supports the ++ operator
    }

    while (i >= 0) {
        console.log(i);
        if (i > 2) {
            i /= 2;
        } else {
            i -= 2;
        }
    }
}


// Slides: https://docs.google.com/presentation/d/1slwUNP4W0-YZuHwXP4p1bjQIVKyex_DtYLwtP18UhhY/edit
// Slide 5:
function forLoops() {

  for (var i = 0; i < 10; i++) {
    console.log(i * 10);
  }

  // count from 50 up to 100 (noninclusive) by 5
  for (var i = 50; i < 100; i += 5) {
    console.log(i);
  }

  // print every character in the string 'words' as upper case
  for (var i = 0; i < 'words'.length; i++) {
    console.log('words'[i].toUpperCase());
  }
}


// Slide 11
function arrays() {
  let names = ["Kanye", "Eminem", "Jay-Z"];
  console.log(names);

  let myList = new Array();
  myList.push(5);             // use "push" instead of "append"
  myList.push(3.2);
  myList.push(true);
  myList.push('something');

  console.log(myList);

  let numList = [];           // just like in Python, this is common

  for (var i = 0; i < 10; i++) {
    numList.push(i * 100);
  }

  console.log(numList);
  console.log(numList.slice(3, 5));
  console.log(numList.slice(3));
}


// Slide 13
function objectsAsMaps() {
  
  // Map is a new construct in JavaScript; historically
  // people have used plain old objects.

  let states = {
    "NY": "Newyork",
    "NJ": "New Jersey",
    "IA": "Iowa",
    "PA": "Pennsylvania"
  };

  console.log(states);

  states["NY"] = "New York";
  console.log(states);

  states["CT"] = "Connecticut";
  console.log(states);

  // "in" also works in JavaScript
  console.log("NY" in states);
  console.log("New York" in states);

  // note that order here will _probably_ be the order in which these keys
  // were defined.
  for (var stateCode in states) {
    console.log(stateCode + ": " + states[stateCode]);
  }
}  


// Slide 14
function maps() {
  
    // you declare differently
    let states = new Map();

    // you *must* use the set / get methods or this doesn't work properly.
    states.set('NY', 'Newyork');
    states.set('NJ', 'New Jersey');
    states.set('IA', 'Iowa');
    states.set('PA', 'Pennsylvania');
    
    console.log(states);

    states.set('NY', 'New York');
    console.log(states);

    // this will not give you an error, but won't work the way you hope.
    states["CT"] = "Connecticut";
    console.log(states);

    // don't use 'in' here
    console.log('NY' in states);
    console.log(states.has('NY'));

    // we need to do this iteration a bit differently.
    for (const stateCode of states.keys()) {
        console.log(stateCode + ": " + states.get(stateCode));
    }
}


// Slide 24
function Person(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.getFullName = function() {
        return this.firstName + ' ' + this.lastName;
    }
    this.getGreeting = function() {
        return 'Hello, ' + this.getFullName();
    }
}

function objects1() {
    let joe = new Person('Joseph', 'Smith');
    let sam = new Person('Samantha', 'Jones');
    console.log(joe.getGreeting());
    console.log(sam.getGreeting());
}


// Slide 25
function objects2() {
  function Pet(name, age) {
    this.name = name;
    this.age = age;

    this.toString = function() {
      return this.name + ' is ' + this.age;
    };
  }


  let pets = [
    new Pet('Fido', 4),
    new Pet('Spot', 7),
    new Pet('Bubbles', 1)
  ];

  console.log(pets[0].toString());
  console.log(pets[1] instanceof Object);
  console.log(pets[2] instanceof Pet);
}



// Slide 26
function dates() {

    // date with current time
    let d = new Date();
    console.log(d);

    // date with year, month, day
    let ymd = new Date(2021, 9, 1); // note: months start with 0
    console.log(ymd);

    // date with year, month, day, hour, minute
    let minutes = new Date(2021, 9, 1, 14, 45);
    console.log(minutes);
}

