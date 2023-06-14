const names = require('./names');  //to signifiy you will be using ur own modules within ur own directory
const f1 = require('./utils');
const path = require('path');
const { readFileSync, writeFileSync, write } = require('fs')

//Synchronous File read/write
const intro = readFileSync('./TextOne/About.txt','utf-8');
const skills = readFileSync('./TextOne/Skills.txt','utf-8');
const seek = path.join('/TextTwo','WhoAmI.txt')

writeFileSync(
    './TextTwo/WhoAmI.txt',
    `${intro}, ${skills}`
)

writeFileSync(
    '.' + seek,
    'This is just an addition!',
    {flag: 'a'}
)

//console.log(readFileSync('./TextTwo/WhoAmI.txt','utf8'));


