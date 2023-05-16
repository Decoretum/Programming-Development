const names = require('./names');  //to signifiy you will be using ur own modules within ur own directory
const f1 = require('./utils');

array = []
for (let i=0; i < names.names.length; i++){
    f1(names.names[i], 'BS MIS', 20, array);
}
console.log(array);


