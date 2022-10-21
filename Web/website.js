const object = document.querySelector('.object');
const gael = {
introduction: async function (){
    
}
}


let dataarray = [];
async function Introduction(){
    let intro = prompt('Hi, visitor! What is your name?');
    message = (`Hi, ${intro}! Welcome to Decoretum's site!`);
    alert(message);
    object.style.backgroundColor = 'Teal';
    object.style.padding = '10px';
    object.style.borderRadius = '9px'; 
    object.textContent = `Welcome, ${intro} to Decoretum's site!`;
    return intro;
}

async function GreetingsfromConsole(){ 
    let data = await Introduction();
    let data2 = 'Mediator';
    console.log(data);
    return Promise.all([data, data2]);
}

async function Warning(){
    let array = [];
    let data = await GreetingsfromConsole();
    for (x of data){
        array.push(x);
    }
    let luckycode = `${array[0]} with number ${array[1]}`;
    console.log(`Please be wary, ${array[0]}`);
    return Promise.all([luckycode, array]);
}

async function Code(){
    let array = [];
    let data = await Warning();
    for (x of data){
        array.push(x);
    }
    console.log(`Your code is: ${array[0]}`);
    console.log(array);
    return data;
}

async function Tester(){
    let data = await Code();
    console.log(data);
}



function imposter(string){
    return new Promise((resolve) => {
        let newstring = string + ' oh yes baby';
        let array = [1,2,3,4,5];
        resolve([newstring, array]); // we returned multiple values as a product of resolving
    })
}

async function Taker(){
    let data = await imposter('Gael');
    let num = 5;
    console.log(data);
    return num;
}

async function Solver(){
    let data = await Taker();
    let dataamplifier = ++data; //we took the value of data and incremented it
    console.log(dataamplifier);
}

Solver(); //we called out the latest function since it is waiting for a promise
Tester();

const isitlegit = document.querySelector('.legit');
let count = 0;
function legit(){
        if (count===0){
           document.getElementById('evolved').style.color='Green';
           document.getElementById('evolved').style.fontStyle='italic';
           document.getElementById('evolved').style.fontSize='20px';
           isitlegit.textContent='Click this to revert Back to Orange now!';
           count = 1;
    }
        else{
            document.getElementById('evolved').style.color='Orange';
            document.getElementById('evolved').style.fontSize='20px';
            document.getElementById('evolved').style.fontStyle='italic';
            isitlegit.textContent='Click this to revert Back to Green now!'
            count=0;
        }
}

isitlegit.addEventListener('click',legit);

const button = document.querySelector('.who');
const button1 = document.querySelector('.hobbies');
const button2 = document.querySelector('.relationship');
const info = document.querySelector('.info');


button.addEventListener('click',function know()
{info.textContent='My name is Gael Estrera, and I\'m currently a 3 BS MIS student here in Ateneo de Manila \nUniversity.' + ' ' +
'I intend to focus on the technical side of MIS such as Database administrating and programming!';
info.style.color='black';
});


button1.addEventListener('click',function hobbies(){
document.getElementById('info').innerHTML='I usually play MMORPG and single RPG games such as Skyrim, Everquest 2, and Oblivion.<br> I also play a sandbox game called Minecraft which is my favourite game of all time! I\'m also a speedcuber, someone who could solve a Rubik\'s Cube within seconds from 2v2 to <br> 5v5 variations.';
info.style.color='black';
});

    
button2.addEventListener('click',function relationship(){
document.getElementById('info').innerHTML='As of now, I\'m single! I do want to be in a relationship, I\'m not desperate for it to be honest. <br> My type are girls that are strong, smart, and not superficial. I am an introvert as well, <br> but I am confident with my looks and capabilities.';
info.style.color='black';

});

let buttonupdate = 0;
const updatebutton = document.querySelector('.whatsnewbutton');
const whatsnew = document.querySelector('.whatsnew');
updatebutton.addEventListener('click',function update(){
    if (buttonupdate === 1){
        document.getElementById('whatsnew').innerHTML = ''
        whatsnew.style.borderColor = 'none';
        whatsnew.style.backgroundColor = 'transparent';
        buttonupdate = 0;
    }
    else if (buttonupdate === 0) {
        document.getElementById('whatsnew').innerHTML = 'Gael has learned new Python packages such as Pandas and SKlearning (Scikit-learning) for data science.<br>He also learned basic to intermediate javascript! (As of 9/11/2022) Pytorch (As of 10/3/2022)';
        whatsnew.style.backgroundColor = 'teal';
        whatsnew.style.borderColor = 'teal';
        whatsnew.style.padding = '10px';    
        buttonupdate = 1;
    }



});

function randomizer(array,array1){
    const randomnum = Math.floor(Math.random()*array.length);
    const randomnum1 = Math.floor(Math.random()*array1.length);
    return array[randomnum] + '<br>' + array1[randomnum1];
    
} 


const randominfo = document.querySelector('.randominfo');
const randombutton = document.querySelector('.randombutton');

randombutton.addEventListener('click',function randomize(){
const list1 = ['Gael is still a virgin!','Gael likes to sleep late!','Gael is a night owl!','Gael is very handsome in real life!'];
const list2 = ['Gael is a kind and just man, <br>but he is also perverted as well!','Gael is really good at programming!','Gael is financially a middle-class boy!','Gael likes spicy food!'];
const listone = randomizer(list1,list2);
document.getElementById('randominfo').innerHTML = listone;
randominfo.classList.add('shrink');

})


let gaelobject = 
{Name:'Decoretum',
Attribute: 'Abyssal',
Affinity: 'Good'
};

/* object.textContent = `${gaelobject.Name}, with the Attribute of ${gaelobject.Attribute} on the side of ${gaelobject.Affinity}`;
object.style.backgroundColor = 'Teal';
object.style.padding = '10px';
object.style.borderRadius = '9px'; */


let testing = document.querySelector('.timer1');
function time(){
    let timearea = '';
    const now = new Date();
    let seconds = now.getSeconds();
    let minutes = now.getMinutes();
    let hours = now.getHours();

    if (seconds < 10){
        seconds = '0' + now.getSeconds();
    }
    if (minutes < 10){
        minutes = '0' + now.getMinutes();
    }
    if (hours < 10){
        hours = '0' + now.getHours();
    }

    if (hours >= 12){
        timearea = 'PM';
    }
    else{
        timearea = 'AM';
    }
    testing.textContent = `${hours} : ${minutes} : ${seconds} ${timearea}`;
    testing.classList.add('timer');
};

setInterval(time,1000);

let listofsomuch =[
    {Name: 'Gael', Power: 'Cool', Attribute: 'Abyss'},
    {Name: 'Lob', Power: 'Might', Attribute: 'Darkness'},
    {Name: 'Mystrus', Power: 'Cool', Attribute: 'Aqua'},
    {Name: 'Jeff', Power: 'Might', Attribute: 'Light'}
]

let counter4 = listofsomuch.reduce((object, {Name, Power, Attribute}) => {
    if (!object[Power]){
        object[Power] = { statement : `Group of ${Power}`, info : []}
    }
    object[Power].info.push({Name, Attribute}); //we use braces to create an object as we push
    return object;
},{});

let RandomObject = [{
        Name : 'Gael',
        School : 'ADMU',
        Course : 'BS MIS',
        Process : function(){
            return `I am ${this.Name} studying in ${this.School} with the course of ${this.Course}`; }
     },
    {
        Name : 'Raine',
        School : 'ADMU',
        Course : 'BS MIS',
        Process : function(){
            return `I am ${this.Name} studying in ${this.School} with the course of ${this.Course}`;
        }
    },
    {
        Name : 'Abbey',
        School : 'ADMU',
        Course : 'BS MIS',
        Process : function(){
            return `I am ${this.Name} studying in ${this.School} with the course of ${this.Course}`;
        }
    }
]
for (x of RandomObject){
    console.log(`${x.Process()}, from ${x.Name}`);
}
console.log(counter4)




