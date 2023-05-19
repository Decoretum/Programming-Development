const names = require('./names');  //to signifiy you will be using ur own modules within ur own directory
const f1 = require('./utils');
const path = require('path');
const { readFileSync, writeFileSync, write } = require('fs')

const http = require('http');

array = []
for (let i=0; i < names.names.length; i++){
    f1(names.names[i], 'BS MIS', 20, array);
}
console.log(array);


const FilePath1 = path.join('/ChildFolder','Child1.js')
const base1 = path.basename(FilePath1);
const absolute = path.resolve(__dirname, 'ChildFolder','Child1.js')

const server = http.createServer((req,res)=>{ //request, response
    if (req.url == "/"){
        res.write('Root page!');
        res.write("/n");
        res.write('Will be filled with main!');
        res.end();
    }
    else if (req.url == "/about"){
        res.write("Gael is a developer!")
        res.end();
    }
    
    else{
    res.write(
        `
        <h1> There is no information for here yet! </h1>
        <p> Try again a later date for this page! </p>
        <a href="/"> Back to Home </a>
        `,
        (err) => {
            console.log('There is an error!');
            res.end(err)
        },
    )
    }
})

server.listen(2019);