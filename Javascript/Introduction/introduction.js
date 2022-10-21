/* operators
=== is strict equality
!== is non-equality
< and > 
results are true and false
*/

// for variables from querySelectors, use textContent 
// for variables from getelementbyid, use innerHTML

// To obtain HTML elements to JS variables, use '.class' or '#idname' through .querySelector


function gael(){
    document.getElementById('gael0').innerHTML='Hi, my name is Gael Estrera!';
    document.getElementById('gael0').style.fontFamily='Verdana';
    document.getElementById('gael0').style.border='none';
    document.getElementById('gael0').style.backgroundColor='transparent';
}

function gaelspecial(){
    document.getElementById('gael0').innerHTML='I can solve a 3x3 Rubik\'s Cube in less than 10 seconds consistently!';
    document.getElementById('gael0').style.fontFamily='Verdana';
    document.getElementById('gael0').style.fontStyle='Italic';
    document.getElementById('gael0').style.border='none';
    document.getElementById('gael0').style.backgroundColor='yellow';

}

function education(){
    document.getElementById('gael0').innerHTML='I\'m currently studying in Ateneo de Manila University as a 3 BS MIS undergraduate!';
    document.getElementById('gael0').style.border='solid';
    document.getElementById('gael0').style.backgroundColor='Teal';
}

const buttons = document.querySelectorAll('button');
for (const a of buttons){
    a.addEventListener('click', gael);
}

const special = document.querySelector('.special');
special.addEventListener('click',gaelspecial);

const geducation = document.querySelector('.education');
geducation.addEventListener('click',education);

focus() //focuses the cursor to an HTML element

const fruitbutton = document.querySelector('.fruits')
const fruitlist1 = document.querySelector('.fruitlist');

const fruits1 = ['apple','banana','mango']; //loop creation and putting in HTML

let no = 0; //reference
function reveal(){
    if (no === 0){
        let empty = []; //we used a function list, an internal list
        for (const a of fruits1){
            empty.push(' '+ a); //appending to list
        }
        let last = empty[empty.length-1]; //last element
        last = ' and ' + last; 
        empty[empty.length-1] = last; //returning and confirming
        
        let array = empty.toString(); //conver array to string
        fruitlist1.textContent = array;
            

       
        fruitlist1.style.border='solid';
        fruitlist1.style.backgroundColor='Teal';
        fruitlist1.style.padding='10px';
        fruitbutton.textContent ='Click here to revert back to Normal!';
        no = 1;
    }
    else {
        fruitbutton.textContent = 'Click here to reveal fruits!';
        fruitlist1.textContent = '';
        fruitlist1.style.backgroundColor = 'transparent';
        fruitlist1.style.border='none';
        no = 0;
    }
    }



fruitbutton.addEventListener('click',reveal);

submitbutton = document.querySelector('.submit');

function display(){
let word = ''
const v = ['a', 'A','e', 'E','i', 'I','o', 'O', 'u','U'];
let Answer = document.querySelector('.answer'); //to obtain values, we can use querySelector() or getElementById() or getElementsbyTagName()[0,1,2,...n]
let name = document.querySelector('.Name').value;
let element = document.querySelector('.Element').value;
let type = document.querySelector('.Archetype').value;
let split = element.split("");
let checker = v.includes(split[0]); //Checking if array includes a certain value
if (checker === true){
    word = ' an ';
}
else{
    word= ' a ';
}

let sentence = 'My name is ' + name + ',' + ' and I\'m' + word + element + ' ' + type + ' mage' + '.';
Answer.textContent ='Classification: ' + sentence; //Does not append since we already added starting string
Answer.style.border='solid'; //we also changed CSS elements
Answer.style.backgroundColor='Orange';
Answer.style.padding='30px';
Answer.style.borderRadius = '8px';
}

submitbutton.addEventListener('click', display);

//alert style
alertbutton = document.querySelector('.alert');
alertmessage= document.querySelector('.alertmessage'); 
alertbutton.onclick=()=>{
let hi = prompt('What is your name?');
message = ('Hello, ' + hi + '!' + ' ' + 'Nice to meet you!');
alert(message);
alertmessage.textContent = message;
}

//objects

Gaelobject = {
name:'Gael', 
position:'3rd Year', 
course:'BS MIS', 
specialization:'Data Science and Analytics'
};

//constants such as consts <var> = <value> 
// must initialize when you declare them
// cant be assigned to new value after theyre initialized

const bird = { species : 'Kestrel'};
console.log(bird.species);  // "Kestrel"

bird.species = 'Striated Caracara';
console.log(bird.species);  // "Striated Caracara"
    

/* number types
integers
float
doubles - more precise version of floats
one data type for numbers, Number 

const decimal = 1.698;
const newdecimal = decimal.toFixed(2) #returns two decimal place
*/

const decimal = 1.698;
const newdecimal = decimal.toFixed(2);
no = document.querySelector('.no')
no.textContent=newdecimal +  ' Rounded off to two decimal';

// Convert string to number
let no1 = document.querySelector('.no1');
let mynumber = '74';
mynumber = Number(mynumber);
no1.textContent = mynumber + ', ' + typeof(mynumber);

//Operations
/* + 
-
* 
/ 
% (remainder)
** exponent */ 

// Increment by 1 by doing variable++ or variable--

//assignment operators
/* +=
-=
*=
/=
*/





const bt = document.querySelector('.calc');
function trying(){
    const what1 = document.querySelector('.what1').value;
    const what2 = document.querySelector('.what2').value;
    const canv = document.querySelector('.no2');
    let selected; // You can't declare/assign variables inside if statements
    const radios = document.querySelectorAll('input[name="ans"]');
    for (const a of radios){
        if (a.checked){
            selected = a.value;
            break;
        }   
    }
    selectedstring = String(selected);
    if (selectedstring==='add'){
        canv.textContent = Number(what1) + Number(what2);
    }
   else if (selectedstring==='sub'){
        canv.textContent = Number(what1) - Number(what2);
}
    else if (selectedstring==='mult'){
        canv.textContent = Number(what1) * Number(what2)
    }
    else if (selectedstring==='div'){
        canv.textContent = Number(what1) / Number(what2);
    }
}
bt.addEventListener('click',trying);

/* comparison operators
!==
===
<
> and you know the rest
*/

/* Some cool strings
 const name = `Gael`; <these are template literals>
 const greetings = `Hi, ${name}!`;
 const one = 'Hello, ';
 const two = 'how are you?';
 const joined = `${one}${two}`; 

 You can use calculations as well1!
 const grade = 90;
 const testname = Math;
 const inform = `Hi! I took the ${testname} a while ago! I got a grade of ${grade/10}, sadly`;

 const break = `You can break lines like 
 this too!`;

 const break1 = 'You can break lines like \nthis too!'; <line breaks if not using template literals>
 */

/* for logical operators
&& = and
|| = or
! = not */







 // String methods   
const string = 'gael';
const length = string.length; // length
const lastlength = string[string.length-1]; //last letter of string
const fetch = document.querySelector('.strings1');
fetch.textContent= `length of string is ${length}. last letter is ${lastlength}`;

const fetch2 = document.querySelector('.strings2');
const get = string.includes('ael') //includes
fetch2.textContent = `Does the string ${string} contains "el"? Answer is ${get}!`;

const fetch3 = document.querySelector('.strings3');
const get1 = string.startsWith('ae'); //starts with
const get2 = string.endsWith('el'); //ends with
fetch3.textContent = `Does Gael start with "ae"? Answer is ${get1}.
Does Gael ends with "el"? Answer is ${get2}.`;

const fetch4 = document.querySelector('.strings4');
const get3 = string.indexOf('el'); // if string does not contain, returns -1 instead
fetch4.textContent=`Index of "el" in ${string} is ${get3}`;

const longstring = 'Gael is the robot of other robots!'
const fetch5 = document.querySelector('.strings5');
const firstget = longstring.indexOf('robot'); //first occurrence
const secondget = longstring.indexOf('of',firstget + 1); //second occurrence wherein we search word starting at index of first occurrence
fetch5.textContent = `Index of first occurrence is ${firstget} while index of second occurrence is ${secondget}`;

const slice = 'Slices';
const sliced = slice.slice(0,5); //slice with start and end
const slicedshort = slice.slice(1); //slice with only 1 then slice rest
const slicestring = document.querySelector('.strings6');
slicestring.textContent = `Sliced with 2 parameters is ${sliced} while only 1 parameter is ${slicedshort}`;

const fetch7 = document.querySelector('.strings7');
const upcase = slice.toUpperCase(); //upcase
const lowcase = slice.toLowerCase(); //lowcase
fetch7.textContent=`This is upcase: ${upcase} while this is lowcase: ${lowcase}`;

const fetch8 = document.querySelector('.strings8');
const original = 'Superpower';  
const updated = original.replace('power','Mage'); //replaces only first occurrence
fetch8.textContent = `Original word is ${original} while updated one is ${updated}`;

const fetch9 = document.querySelector('.strings9');
const longone = 'Let gael destroy all of the other gael in the land'
const updateall = longone.replaceAll('gael','max'); //replaces second occurrence as well
fetch9.textContent = `This is the original text: ${longone}. 
The next one is the updated one: ${updateall}`;

const arraystring = document.querySelector('.array');
const coolarray = [1,2,3,['gael','iris']];
arraystring.textContent=`Indexed array is ${coolarray[3][1]}.`;
// indexOf() and .push() you know how to use
coolarray.unshift('9');
arraystring.textContent+= ` New element of the array added at start is ${coolarray[0]}`;

const arraystring1 = document.querySelector('.array1');
arraystring1.textContent = `Last element removed in list: ${coolarray} is ${coolarray.pop()}. `;  // removes last element
arraystring1.textContent += `New list is now ${coolarray}`;
coolarray.shift(); //remove first element
arraystring1.textContent += ` With first element removed, new array is ${coolarray}`;

const arraystring2 = document.querySelector('.array2');
const newarray = ['1','4','8','Gael',1];
for (const e of newarray){
    if (typeof(e) !== 'string'){ // using .typeof to get string result of data type
        newarray.splice(newarray.indexOf(e),1); // using splice if you knew (<index of element>,how many elements to remove from there)
    
    } 
}
arraystring2.textContent = `Using the splice() function, the new array is now ${newarray}`;

const arraystring3 = document.querySelector('.array3');
numberarray = [5,1,2,51,22,8];
function arrayf(a){ //function with parameter
    return a += ' number ';
}
function arrayg(a){
    return a * a;
}
const f = numberarray.map(arrayf); // we use map to apply changes to all elements in array
const g = numberarray.map(arrayg);
arraystring3.textContent=`${f}  and   ${g}`;

const arraystring4 = document.querySelector('.array4');
const listcool = ['love','me','like','you','do'];
function lengthcheck(a){
    return a.length >= 3;
}
const longcheck = listcool.filter(lengthcheck); //using filter, similar to map which takes in function
arraystring4.textContent = longcheck;

const arraystring5 = document.querySelector('.array5');
const nonsep = 'gael,justin,iris,yuan,yo';
const ind = nonsep.split(','); //split declares a separator and then returns elements in an array
const joins = ind.join(','); //
arraystring5.textContent = `${ind} and the first one is ${ind[0]} and its data type is ${typeof(ind)}. When joined, it becomes ${joins} and its data type is ${typeof(joins)}`; 

const arraystring6 = document.querySelector('.array6');
const stringlist = ['gael','yonmama','drewholiday'];
const stringconnect = stringlist.join(',');
arraystring6.textContent = `The array became ${stringconnect} and its data type is ${typeof(stringconnect)}`;



let objlist = [
    {Name: 'Gael', Attribute: 'Abyssal', Power: 'To destroy evil!' },
    {Name: 'Alex', Attribute: 'Fire', Power: 'To achieve peace!'},
    {Name: 'Maya', Attribute: 'Ice', Power: 'To bring in devastation!'}
];


const objbutton1 = document.querySelector('.obj1');
const objbutton2 = document.querySelector('.obj2');

objbutton1.addEventListener('click',function format1(){
const objmap = objlist.map(function(a){
return `The name is ${a.Name} with the attribute of ${a.Attribute} with the goal of: ${a.Power}`;
    
});
const objstring = String(objmap);
const removecom = objstring.replaceAll(',','<br>');
document.getElementById('objects').innerHTML= removecom;

});

objbutton1.addEventListener('click',function format1(){
    const objmap = objlist.map(function(a){
    return `The name is <div class='ind'> ${a.Name} </div> with the attribute of ${a.Attribute} with the goal of: ${a.Power}`;
        
    });
    const objstring = String(objmap);
    const removecom = objstring.replaceAll(',','<br>');
    document.getElementById('objects').innerHTML= removecom;
    
    });

objbutton2.addEventListener('click',function format2(){
const objmap = objlist.map(function(a){
return `The name is ${a.Name} with the attribute of <div class='ind'> ${a.Attribute} </div> with the goal of: ${a.Power}`;
    
});
const objstring = String(objmap);
const removecom = objstring.replaceAll(',','<br>');
document.getElementById('objects').innerHTML= removecom;

});

let arraylist = ['gael','gael'];
let arraynum = [
    {Number: 100},
    {Number: 10000}
];
const arrayconv = Array.from(arraynum);
const arrayadd = arrayconv.reduce(function(total,a){
return total + a.Number;

},0);
const arrayred = arrayconv.reduce(function(a,b){
if (!a[b]){
    a[b] = 0;
}
a[b]++;
return a;
},{});
console.log(arrayadd);
console.log(arrayred);

let numbers = [1,2,4,5,6];
const numbersort = numbers.reduce(function(total,a){
return total * a;
});
console.log(numbersort); //multiplication does not need 0 placeholder

const numbersort1 = numbers.reduce(function(total,a){
return total / a;
});
console.log(numbersort1);

let numbersort2 = numbers.slice().sort(function(a,b){
if (a >b){
    return 1;
}
else{
    return -1;
}

});
console.log(numbersort2);

let nummap = numbers.map(function(a){
return `${numbers.indexOf(a)} : ${String(a)}`;

});
console.log(nummap);

const reg = document.querySelector('.reg');
const testlist = ['Gael can also be gael'];
let regobj = new RegExp('Gael','gi');
let match = testlist[0].match(regobj, 'gi'); //we matched
reg.textContent= `Matches are: "${match}" is howdy`;



const set = document.querySelector('.sets');
const setreal = document.querySelector('.setsreal');

const samplearray = [1,2,3,4]
let arraysampling = samplearray.map(x => {return x});
let objsampling = objlist.map(x => {return `${x.Name} has the attribute of ${x.Attribute} with the power of ${x.Power}`});
let newsampling = objsampling.join(',');
let lastsampling = newsampling.replaceAll(',','<br>');

set.innerHTML = lastsampling;







//Maps
//new Map([iterable]) – creates the map, with optional iterable (e.g. array) of [key,value] pairs for initialization.
//map.set(key, value) – stores the value by the key, returns the map itself.
//map.get(key)-- returns the value by the key, undefined if key` doesn’t exist in map.
//map.has(key) – returns true if the key exists, false otherwise.
//map.delete(key) – removes the value by the key, returns true if key existed at the moment of the call, otherwise false.
//map.clear() – removes everything from the map.
//map.size – returns the current element count.

let gaelmap = new Map();
gaelmap.set('Level',1) //can take any values as keys
gaelmap.set('Age',19);
gaelmap.set(true, 69)

//to iterate over keys
for (let about of gaelmap.keys()){
setreal.innerHTML += `<br>Properties: ${about}`;

};

//to iterate over values
for (let about of gaelmap.values()){
setreal.innerHTML += `<br>Values: ${about}`;

};
//to iterate over keyvalues
for (let a of gaelmap){
setreal.innerHTML += `<br>${a}`;
};

//using forEach, similar to Nodelists or arrays
gaelmap.forEach((value,key,map) => {
setreal.innerHTML += `<br>${key} : ${value}`;

}) 

//using a bigger map and getting the value of a key in a map
let biggermap = new Map([
['Name','Gael'],
['Course','MIS'],
['Specialization','Data Science and Analytics']
])
setreal.innerHTML += `<br>${biggermap.get('Name')}`;

//converting an object into a map using Object.entries()
let convertedobj = new Map(Object.entries(Gaelobject)); //object.entries returns array of key - value
setreal.innerHTML += ` <br>${convertedobj.get('course')}`;

//converting a map into an object using Object.fromEntries(), returns iterable object
let convertedmap = Object.fromEntries(convertedobj); //doing convertedobj.entries() will return an iterable pairs of array
setreal.innerHTML += `<br>${convertedmap.specialization}`;



// sets
// new Set(iterable) – creates the set, and if an iterable object is provided (usually an array), copies values from it into the set.
// set.add(value) – adds a value, returns the set itself.
// set.delete(value) – removes the value, returns true if value existed at the moment of the call, otherwise false.
// set.has(value) – returns true if the value exists in the set, otherwise false.
// set.clear() – removes everything from the set.
// set.size – is the elements count.

const s = document.querySelector('.set');
sampleset = new Set();
let obj1 = {name: 'Gael', Power:'Smart'};
let obj2 = {name: 'Gael', Power:'Stupid'};
let obj3 = {name: 'Iris', Power: 'Great', Attribute: 'Powerful'};
sampleset
.add(obj1)
.add(obj2)
.add(obj3);
console.log(sampleset); // will not return duplicate objects

//iterating over sets
for (let v of sampleset){
s.innerHTML += `<br>${v.name} with ${v.Power}`;
};

sampleset.forEach((value, valueAgain, set) =>
{
s.innerHTML += `<br>${value.name} with an attribute of ${value.Attribute}`;

});

//has same methods as map for iterations as well

for (let v of sampleset.entries()){
s.innerHTML += `<br>${v}`;
};

console.log(sampleset.values());

// also has Object.fromEntries() and Object.entries()

//remove duplicates in array

dupearray = [1,2,1,1,1,1,6,7];
let removedup = new Set((dupearray));
console.log(removedup);
for (v of removedup){
    console.log(v);
}
console.log("\n");
for (let a of removedup){
s.innerHTML += String(a);
console.log(String(a));
}; //we removed duplicates, wow!

//Question 1

const q1 = document.querySelector('.q1');
let arr = ["nap", "teachers", "cheaters", "PAN", "ear", "era", "hectares"];

function aclean(array){
let emptylist = [];
firstarray = array.sort(function(a,b){
if (a.length === b.length){
 a = b;
 emptylist.push(a);   
}
});
let newarray = new Set(emptylist);
for (let word of newarray){
    q1.textContent += ` ${word},`;
    console.log(word);
}
};
console.log(aclean(arr)); //this removes duplicates

//Question 2
let emptylist2 = [];
let map = new Map();
map.set("name", "John");
let keys = map.keys();
for (let key of keys){
emptylist2.push(key);
console.log(key);
};

// Error: keys.push is not a function
emptylist2.push("more");
console.log(emptylist2);


//training with reduce function
let list01 = [
    {Name: 'Tassadar', Race: 'Protoss', Faction: 'Conclave'},
    {Name: 'Zeratul', Race: 'Protoss', Faction: 'Dark Templar'},
    {Name: 'Adun', Race: 'Protoss', Faction: 'Conclave'}
]
let reduction = list01.reduce((reducer, {Name, Race, Faction}) => {
if (!reducer[Race]){
    reducer[Race] = { // will be equiavalent to an object representing a group specified with condition
        Racial: Race,
        Residents : []
    }
}   
reducer[Race].Residents.push(`${Name}, ${Faction}`)

return reducer; //accumulated

},{});
console.log(reduction)

let addlist = [
    {Name: 'Gael', Numer: 50},
    {Name: 'Iris', Numer: 121},
    {Name: 'Sam', Numer: 21}
]
let numberreducer1 = addlist.reduce((total, {Numer}) => {return total + Numer},0);
let sum = 0

let numberreducer2 = addlist.reduce((total, {Numer}) => {
 sum += Numer
 total = {
    sumlist : sum  //Logic is that, this whole bracket object is applied for the first iteration, hence, sum for first iteration is simply 0 if addition is put after this object
}
return total;
},{});
console.log(numberreducer1)
console.log(numberreducer2)

let mojo = dupearray.reduce((function(total,x){
return total + x;

}))
console.log(mojo);

let total = 0;
let samplepromise = new Promise((resolve,reject)=>{
    for (i = 0; i < addlist.length; i++){
    console.log(`This is ${addlist[i].Numer * addlist[i].Numer}`);
    }
    resolve('Done'); 
    reject(new Error('Oh shit!')); //resolve and reject values we are passing 
    
    })
    .then(FirstStep(), error => console.log("Error"))
    .then(SecondStep(), error => console.log("Error"))
    .then(mediator())
    .then(mediator2())
    .then(Isitokay(), error => console.log("Error")) //if promise result is not yet released, put () in functions to pass result
    .then(Almost(), failure => console.log(failure))
    .then(ready(),error => console.log(error)) 
    .then(result => console.log(result),failure => console.log(failure))  //////
    .finally() //A finally handler “passes through” the result or error to the next suitable handler. Generic cleanup no matter outcome
    .then(Finale, failure => console.log(failure)) //after the result of the promise, no need for functions to carry the value anymore
    .then((setTimeout(feel, 1000)), error => console.log('Mistake!'))  //After 10 seconds, this shit happens. Cool
    .finally()
    .then(setTimeout(ending, 1000), error => console.log(error))
    .then(setTimeout(SecondStep,1000))
    .finally();

    //You can also use .catch which is also .then(null,f) for catching only errors
  

    
    
/*
    let finalpromise = new Promise((resolve, reject) => {
        throw new Error("error");
      })
        .finally(() => setTimeout(console.log("Promise ready"),5000)) // triggers first
        .catch(err => console.log(err));  // <-- .catch shows the error

*/

        function ready(){
            console.log('readying data');
        }
        function feel(){
            console.log("Feel this awesomeness!");
        }
        function ending(){
            console.log("End");
        }
        function mediator(){
            console.log('This is a mediator function for finally! Wow!')
        }
        function mediator2(){
            console.log('This is the last function before the result of the promise, wow!')
        }
        function Isitokay(){
            console.log('So far, it is okay')
        }
    
        function Finale(){
            console.log('Hence, sleep child.')
        }

        function Almost(){
            console.log("Almost there!");
        }


    function FirstStep(){
    let varOne = 19023;
    let Combined = varOne * 69;
    console.log(Combined);
}

    function SecondStep(){
    let Data = 12;
    let result = `Result is ${Data}`;
    console.log(result);
    return;
};

    function howyoudo(){
        console.log("Doing well!");
    }

    function damn(){
        console.log("Damn, you got me hanging!");
    }

    function damn2(){
        console.log("Why you leave me pre?");
    }
    function keyPressed(){
        console.log("Key pressed");
    }
/* onchange	An HTML element has been changed
onclick	- The user clicks an HTML element
onmouseover	- The user moves the mouse over an HTML element
onmouseout - The user moves the mouse away from an HTML element
onkeydown - The user pushes a keyboard key
onload */
console.log(SecondStep instanceof Object);
let hover = document.querySelector('.Damn');
let hover2 = document.querySelector('.Damn1');
hover.addEventListener('mouseover',damn);
hover2.addEventListener('mouseout', damn2);
window.addEventListener('keydown', keyPressed);

//continuation of string methods
let none = document.querySelector('.none');
none.textContent = 'Hello \
Bro!';

let splicesample = 'Yo parechong puta parechong';
let splicing = splicesample.slice(0,6); //last index of word not included
let subsplciing = splicesample.substring(-10,6); //first index is always 0
let insensitive = splicesample.replace(/pAreChong/i,'Pre'); //to replace anything with case insensitive, add / /i
let insensitive1 = splicesample.replace(/pAreChong/ig,'Global pre'); // to replace anything global and case insensitive
console.log(splicing);
console.log(subsplciing);
console.log(insensitive);
console.log(insensitive1);

let A1 = 'Puta';
let A2 = 'Yo';
let T1 =  A1.concat(' ',A2); //concat
console.log(T1);

let A3 = ' Preeee      ';
let T2 = A3.trim(); //remove whitespaces from both side
console.log(T2 + T2.length); //trimStart() only removes whitespaces from start of string, similar to trimEnd()

let P1 = String(5);
let P11 = P1.padStart(5,'x'); //pads number from start, similar with padEnd()
console.log(P11);








