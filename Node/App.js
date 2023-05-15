const names = require('./names');  //to signifiy you will be using ur own modules within ur own directory
const f1 = require('./utils');


array = []
let PKeys = Object.keys(names);
for (let i=0; i < PKeys.length; i++){
    f1(names[PKeys[i]], 'BS MIS', 20, array);
}
console.log(array);


