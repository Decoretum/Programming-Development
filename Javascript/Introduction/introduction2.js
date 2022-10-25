//Continuation of JavaScript Awesome learning

//string methods
let A1 = 'Hi momma, glad to se momma alive yo mo';
let A1a = A1.charAt(4); // returns character at index position
let A1aa = A1.charCodeAt(4); //returns unicode of char at index
let A1b = A1[4]; //similar also it is property access
console.log(A1a, A1b, A1aa);

//string search
let D1 = A1.match(/mO/gi); //match returns an array, argument is a regular expression
console.log(D1);

let D2 = '9';
console.log( 18 / D2); // since numeric string, it works

let D3 = 9;
let D4 = 9.12312;
let D3a = new Number(9);
console.log(D3 === D3a); //if using triple =, not equal if new object generatd
// comparing two js objects always false

let D3b = D4.toExponential(3); //exponential notation
console.log(D3b);

let D3b1 = D4.toFixed(3); //rounds off at index
console.log(D3b1);

let D3b2 = D4.toPrecision(3) //specified length roudned off at index of last length number
console.log(D3b2);
console.log(D3b2.valueOf());

//some general methods for numbers
//parseint
let parsesample = [{First : 'Gael'},
{First : 'Iris'}];

let parselist = [1,2,3,4,5];

console.log(parseInt("-1231"));
console.log(parseInt("-1231, 9123")); //parses string and returns whole number, only first number returned
console.log(parseInt("-1231.923123, 123"));
console.log(parseInt("yes, asd, -1231"));

console.log(parseFloat("-1231.12314")); //returns float
console.log(parsesample[0].First);

//arrays and their manipulation
let parsearray = [
    123123,
    "yo",
    {First : 'Tomas', Surname : 'Estrera'},
    function adept(){
        return "Yahoo!";
    }
]
for (el of parsearray){
    console.log(el);
}

console.log(parsearray[parsearray.length - 2]); //second to the last

let placeholder = "<ul>";
for (x of parselist){
    placeholder += `<li> ${x} </li>`;
}
placeholder += "</ul>";
let list1 = document.querySelector('.list1');
list1.innerHTML = placeholder;

console.log('\n');

let placeholder2 = '<ul>'
for (x of parsearray){
    if (x.First === 'Tomas'){
        placeholder2 += `<li> ${x.First} ${x.Surname}`;
    }
    else if(typeof(x) === 'function'){
        placeholder2+=`<li> ${x()} </li> `;
    }
    else{
    placeholder2 += `<li> ${x} </li>`;
}
}

placeholder2 += "</ul>";
let list2 = document.querySelector('.list2');
list2.innerHTML = placeholder2;

console.log(Array.isArray(parsearray)); //checks argument if its array or not
console.log(parselist === Array(1,2,3,4,5)); //false
console.log(parsearray instanceof Array); //check if object is instance of array

Array.toString();
//push, pop, these are lasts
//Array.shift(); removes first element and shifts other elements to lower index
//Array.unshift(); add new element to beggining of array

delete Array[0]; //specific index delete

// Array.sort(); alphabetical sort, reverse() is opposite
// Array.sort(function(a-b){return a-b}); to sort numbers ascending

//Compare function = alternative sort order, basically modifications to default sort()

console.log(parselist.sort(function(){return 0.5 - Math.random()})); //random number positioning
console.log(0.5 - Math.random());

const points = [40, 100, 1, 5, 25, 10,999];

/* for (let i = points.length -1; i > 0; i--) {
  let j = Math.floor(Math.random() * (i+1)); //generating random index position value
  let k = points[i]; // current index value
  points[i] = points[j]; //change current index value to value of random generated index position
  points[j] = k; // we assign orig value of current index as the value of collateral index, so we swapped them
} */

console.log(Math.max.apply(null,points)); //max value of array, same as .min.apply()

//a function for finding max, just reverse this to find the min
function myArrayMax(arr) {
    let counter = 0;
    let max = -Infinity;
    let arrlen = arr.length - 1;
    while (counter < arrlen) {
      if (arr[counter] > max) {
        max = arr[counter];
      }
      counter++;
    }
    return max;
  }

console.log(myArrayMax(points));

const cars = [
    {type:"Volvo", year:2016, specialization : "sex"},
    {type:"Saab", year:2001, specialization : "love"},
    {type:"BMW", year:2010, specialization : "care"},
    {type:"SSS", year:2010, specialization : "destruction"}
  ];

let carsSort = cars.sort(function(a,b){
if (a.type < b.type){
    return -1;
}
});

let carfilter = cars.filter(function(a){
  if (a.year >= 2010){
    return a;
  }
})

let carsum = cars.reduce((object, {year, type, specialization})=> {
  if (!object[year]){
    object[year] = {
      Year: year,
      Info: []
    }
  }
  object[year].Info.unshift({type, year, specialization}); //created new objects from appending
  return object
},{});


let carcheck = cars.every(function(a){
  if (a.year >= 2000){
    return a;
  }
})

let carsome = cars.some(function(a){if (a.type.length >= 6){return a;}})

console.log(carsSort);
console.log(carfilter);
console.log(carsum);
console.log(carcheck);
console.log(carsome);

//finding first index, modify to find last index
function findFirst(array){
let poslist =[]
let pos = 0;
let min = '';
for (obj of array){
  if (obj.year >= 2001 && obj.specialization === "care"){
    //console.log(cars.indexOf(obj));
    pos = array.indexOf(obj);
    poslist.unshift(pos);
  }
}
for (x of poslist){
min = x;
if (x < min){
  x = min;
        }
    }
console.log(min);
}

findFirst(cars);


let finding = points.find(function(a){if(a >= 0){return a;}});
console.log(finding);

let findindex = points.findIndex(function(a){ //shortcut to find index of first occurrence
return a < 91;
});

console.log(findindex);


//we find index of first occurrence without findindex
let aryan = 0;
  for (x of points){
  if (x >= 91 && aryan === 0){
    aryan = 1;
    console.log(points.indexOf(x));
  }
}

let findobjectarray = cars.find(function(a){
  return a.specialization === "sex" && a.year > 2010;
});

console.log(findobjectarray);

console.log(Array.from("Y|es123NoWhy"));

//Array.keys() returns array iterator object 0... n
//Object.entries() return array iterator object with values (position, value)
let matchy = points.entries();
for (x of matchy){
  console.log(x);
}

//dates
let date = new Date(); //current date of computer, date objects are static
let gaeldate=  new Date(2003, 1, 7, 0, 0, 0, 0); //js counts months from 0 to 11, if excess, will add to overflow only, same to days
//creating date can also include only 2 arguments minimum, year and month
let archexam = new Date(2022, 9, 27,3,30);
let motherdate = new  Date(86, 0, 24); //interpreted from previous century
console.log(`Enterprise Architecture exam: ${archexam}`);
console.log(`Mother's Birthday: ${motherdate}`);
console.log(`Gael's Bday: ${gaeldate}`);

let Break2022 = new Date("December 20, 2022 12:00:00:00"); //we made custom date using string
console.log("Break: ", Break2022);

//JavaScript stores dates as number of milliseconds since January 01, 1970, 00:00:00 UTC (Universal Time Coordinated).

let totalmilli = new Date(0); //origin date, meaning date of 0 time plus 0 milliseconds
console.log(date);
console.log(date - totalmilli); //total number of milliseconds that have passed

let oldDate = new Date(5000000);
let olderDate = new Date(-50000000); //older date since negative
console.log(oldDate);
console.log(olderDate);

//One day (24 hours) is 86 400 000 milliseconds.

//Date Displays

console.log(gaeldate.toUTCString());
console.log(gaeldate.toDateString());
console.log(gaeldate.toISOString());

console.log(new Date("2003-02-07")); // ISO 8601 international standard for input, can also only accept year and month or year only

//ISO dates can be written with added hours, minutes, and seconds (YYYY-MM-DDTHH:MM:SSZ):

console.log(new Date("1981-06-20T03:20:45Z")); //date and time separated by "T", Z represents UTC time

console.log(new Date("01/03/1986")); //short date
console.log(new Date("January 3 1986")); //long date

//Date parsing - returns value of milliseconds between time 0 and date

let momandson = Date.parse("1986-01-03");
let gaelolddate = Date.parse(gaeldate);
console.log(momandson);

//we can convert milliseconds to date object
let newdate = new Date(gaelolddate);
console.log(newdate);



//get methods from dateobjet
console.log(gaeldate.getDate());
console.log((Date.now()/31536000000))


//set date methods
let nowdate = new Date();
nowdate.setDate(nowdate.getDate() + 61);
console.log(nowdate);

console.log("\n\n\n");

//Math Object - static, no need to make objects for it
//Properties (some)
console.log(Math.E);
console.log(Math.PI);

//methods
console.log(Math.round(8.124));
console.log(Math.ceil(8.124)); //rounded up
console.log(Math.floor(8.124)); //rounded down
console.log(Math.trunc(8.125)); //returns integer part of argument
console.log(Math.sign(8.124)); //returns if argument is negative (-1), positive (+1), or null (0)
console.log(Math.pow(2,4));
console.log(Math.sqrt(64));
console.log(Math.abs(8.124));
console.log(Math.sin(301 * Math.PI / 180)); //returns sin of argument radians, same as cos()
//Math.min() and Math.max() used to find min and max

console.log(Math.random()*2); //random value between 0 and 1

//Math.log() returns natural logarithm of argument

//good random function

function Random(min,max){
  return Math.floor(Math.random() * (max-min)) + min;
}




//Boolean

console.log("\n\n\n\n");
let x5125 = 0;
console.log(Boolean(52<12));
console.log(Boolean(x5125)); //false since no value number, same as with -0
console.log(Boolean("")); //same as with undefined, null, and NaN

//make Boolean object
let joke = new Boolean(124<4);
//comparing two javascript objects always result to false

//comparisons

let condition = (gaeldate > oldDate) ? "Current is nigh!":"Did we Time travel?";
console.log(condition);

//nullish coalescing operator - for null or undefined
let whamper = null;
let condition1 = whamper ?? "This aint even exist!";
console.log(condition1);

//optional chaining operator - returns undefined if object is undefined or null
console.log(condition1?.name);


//javascript switches - basically the one in Java

let synt = [1,2,54,"Yo"];
switch(synt[3]){
case "Yo":
  console.log("Yo is here!");
  break;
case 0:
  console.log("0 bro");
  break;
case 1:
  console.log("Problem?");
  break;
default:
  console.error("No Index of that sort");
}

//break keyword used to break out of the switch case block
//default keyword used if no case matches it - if its not in the last, add break to it. 

//common code blocks that use same output

switch(Math.floor(Math.random() * 10)){
  default:
    console.log("What you think this number gon be?");
    break;
  case 0:
    console.log("Bottom bro");
    break;
  case 1:
    console.log("Still down but good");
    break;
  case 2:
  case 3:
  case 4:
  case 5:
      console.log("Growing! Still down.");
}

//if multiple case values match the expression, first case for that value is selected


//loops
//for loop

for (let i=0, text = '', placeholder="||"; i < synt.length; i++){ //you can initialize as much in expression 1, you can also leave it blank with ;
  text += String(synt[i] + placeholder);
}


//you can also leave expression 2 and 3 blank
// for 2, you need to provide break though if thats the case. If expression 2 returns true, loop continues

for (let i=0, text = '', pd="||"; ;i++){
  text += String(synt[i] + pd);
  if (i === synt.length-1){
    console.log(text);
    break
  }
}

//for in - more on keys of arraylist or iterable, also on properties of objects
for (key in synt){ //index of arraylist
  console.log(key);
}

let deadperson = {
  first : "Gael",
  last : "Estrera",
  hobby : "Gaming"
}

for (key in deadperson){ //to iterate over properties, but no need really
  console.log(`${key} : ${deadperson[key]}`);
}

//forEach
let haha = '';
synt.forEach(function(a){
haha += " " + String(a) + " LOL";
})
console.log(haha);

//for of you know too much already



//while loops

//normal while loop, too ez


//do while loop

let i = 0;
do {
  if (i === 0){
    console.log("Here it goes!");
  }
  console.log("Skadooshy");
  i++;
}
while(i < 5);

//breaks

let fun = [
  {first : "Gael", second : "Cool", Power : "Thunder", Desire : "Power"},
  {first : "Decoretum", second : "Scary", Power : "Abyss", Desire : "Lust"}
]

for (x of fun){
  if (x.first === "Decoretum"){
    console.log(`Fine! The lewd one here has the desire of ${x.Desire}`);
    break;
  }
  console.log(`${x.first}, ${x.second}, power of ${x.Power}`)
}

function ObjectPurifier(ObjectArray){
  for (obj of ObjectArray){
    if (obj.Desire === "Lust" || obj.Desire === "Power"){
      obj['WARNING'] = `This user has the inappropriate desire: ${obj.Desire}`;
    }
  }
  console.log(ObjectArray)
}

function Verdict(array){
for (x of array){
  if (typeof x === "string"){
    console.log(`HA! The suspect "${x}" is at index ${array.indexOf(x)}`)
    break;
  }
}
}

function Smart(ObjectArray){
  let list = [];
  for (x of ObjectArray){
    if (x.Desire === "Power"){
      continue;
    }
    list.unshift(x);
  }
  console.log(list);
}


ObjectPurifier(fun);
Verdict(synt);
Smart(fun);


//Javascript labels

//you can limit code blocks and break out of any of them using "break <label>;"



//Maps (review lol, its basically Java's hashmap)
let gaelmap = new Map();
gaelmap.set("Authenticity",0)
.set("Power",0)
.set("Credentials","Active")
.set("Name","Gael")
.set("Ability","Lackluster");


function CheckMap(map){ //hashmap
  let list = [];
for (key of map.keys()){
  if (map.get(key) === "Lackluster"){
    map.set("Verdict","Needs more tuning");
    map.delete(key);
  }
  else if (key === "Power" && map.get(key) === 0){
    map.set("Power Assurance","Stable and Qualified");
  }
  else if (key === "Authenticity" && map.get(key) === 0){
    list.unshift("This is a valid list for credentials");
    map.set("Credentials",list);
  }
}
return map;
}
//testiong
console.log(CheckMap(gaelmap));

//Sets (review again, lol)

let testarray = [1,1,1,2,3,4];
let nomore = new Set(testarray);
console.log(nomore);
console.log(nomore.values());

//.add to add, .iterator() to create object containing all values/elements of set