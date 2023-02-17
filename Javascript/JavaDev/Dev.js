//Lets make objects

let Programmer = {
    Name : '',
    University : '',
    Field : '',
    Insights : 0,
    Introduction : function(){
        if(this.University === ''){
            console.log(`My name is ${this.Name} and I\'m a self-taught developer!`);
            console.log(`My field of expertise is ${this.Field}.`)
        }
        else{
            console.log(`My name is ${this.Name} and I\'m a student in ${this.University}.`);
            console.log(`My field of expertise is ${this.Field}.`)
        }       
    },
}

//Instantiate using function
function Developer(Name, Field, University){
    this.Name = Name;
    this.Field = Field;
    this.University = University;
    this.Introduce = 
        console.log(`Hi! My name is ${this.Name}`)
        if (this.University === "Ateneo de Manila University"){
            console.log(`I'm also an eagle! Muwahahaha`);
        }
    }

//using ES6 class

class ITBuilder{
    constructor(Name, Field, University){
        this.Name = Name;
        this.Field = Field;
        this.University = University;
        this.Insights = 0;
    }
    Flex(){
        let pattern = /software development/i;
        if (pattern.test(this.Field)){
            console.log(`I am an IT Developer! I build and develop applications!`);
        }
    }

    Status(){
        if (this.Insights <= 2){
            console.log(`It is still not enough insight! Learn more!`);
        }
    }

    Hate(hate){
        let pattern = /frontend/i;
        if (pattern.test(hate)){
            console.log(`I ABSOLUTELY hate front-end!`);
            console.log(`I prefer BACK-END!`);
        }
    }

    Learn(topic){
        let p1 = /prog/i;
        if (p1.test(topic)){
            this.Insights += 1;
            console.log(`Improving programming skills!`);
            console.log(`Insight level: ${this.Insights}`);
        }
    }
}


const Gael = Object.create(Programmer);
Gael.Field = "Software Development";
Gael.Name = "Gael";
Gael.University = "Ateneo de Manila University";

Gael.Introduction();

let Dam = new Developer("Dan","Software Development","Ateneo de Manila University");
Dam.Introduce;

const Sean = new ITBuilder("Sean","Software Development","UP Diliman");
Sean.Flex();
Sean.Hate('FrontEnD');
Sean.Learn('programming');
Sean.Learn('program');
Sean.Status();
