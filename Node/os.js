const os = require('os'); //built-in

//info about current user
const user = os.userInfo()
console.log(user)

//return system uptime in seconds
console.log(`The system uptime is ${os.uptime()}`)

const currentOS = {
    name: os.type(),
    release: os.release(),
    totalMem: os.totalmem(),
    freeMem: os.freemem()
}

console.log(currentOS);