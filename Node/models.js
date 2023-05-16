class Person{
    constructor(Name, Course, Age){
        this.Name = Name;
        this.Course = Course;
        this.Age = Age;
    }

    intro(){
        return `Hi, my name is ${this.Name}! I'm currently in ${this.Course}, and I'm ${this.Age} years old!`;
    }
}

module.exports.C1 = Person