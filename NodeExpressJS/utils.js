const PersonClass = require('./models');

function CreateObject(Name, Course, Age, array){
    const person = new PersonClass.C1(Name,Course,Age);
    array.push(person);
}

module.exports = CreateObject