const names = require('./names');  //to signifiy you will be using ur own modules within ur own directory
const f1 = require('./utils');
const path = require('path');
const { readFile, writeFile } = require('fs')

readFile('./TextTwo/WhoAmI.txt', 'utf8', (err,result)=>{
    if (err){
        console.log('There is an error!');
        return;
    }
    const newpath = path.join('/TextTwo','Crush.txt');
    const first = result;
    readFile('.' + newpath, 'utf-8',(err,result)=>{
        if (err){
            console.log('Error in 2nd iteration!');
            return;
        }
            const second = result;
            const childpath = path.join('/ChildFolder')
        writeFile(
            "." + childpath + "/" + "verdict.txt",
            `Who is this person? : ${first} + " " + ${second}`,
            (err, result) => {
                if (err){
                    console.log(err);
                    return;
                }
                console.log('Processes finished!');
            }
        )
    })

})

const seek = path.join('/TextTwo','/WhoAmI.txt');

