const names = require('./names');  //to signifiy you will be using ur own modules within ur own directory
const f1 = require('./utils');
const path = require('path');
const { readFileSync, writeFileSync, write } = require('fs')

array = []
for (let i=0; i < names.names.length; i++){
    f1(names.names[i], 'BS MIS', 20, array);
}
console.log(array);


const FilePath1 = path.join('/ChildFolder','Child1.js')
const base1 = path.basename(FilePath1);
const absolute = path.resolve(__dirname, 'ChildFolder','Child1.js')
