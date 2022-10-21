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


console.log(Array.from("Y|es123NoWhy"));

//Array.keys() returns array iterator object 0... n
//Object.entries() return array iterator object with values (position, value)
let matchy = points.entries();
for (x of matchy){
  console.log(x);
}

