const fs = require('fs');

const stream = fs.createReadStream('./TextOne/About.txt', {highWaterMark: 10});
const stream2 = fs.createReadStream('./TextOne/Skills1.txt', {highWaterMark: 40000});

stream.setEncoding('utf-8');
stream2.setEncoding('utf-8');

stream.on('data', (data) => {
    console.log(data);
    stream2.on('data', (datum) => {
        console.log(datum);
    })
})

stream.on('error', (err)=>{
    console.log(err);
})

stream2.on('error', (err)=>{
    console.log(err);
})