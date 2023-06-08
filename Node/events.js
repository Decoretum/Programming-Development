const EventEmitter = require('events');
const http = require('http');


const customEmitter = new EventEmitter(); //instance of an event emitter

//Order matters in how events and emitters 

//We listen for a response event
customEmitter.on('response', ()=>{
    console.log(`Here is my response!`);
})

customEmitter.on('response', (name, course)=>{
    console.log(`Hello! I am ${name} from ${course}.`);
})

//We emit a response event
customEmitter.emit('response', 'Gael', 'BS MIS');