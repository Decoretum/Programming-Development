const http = require('http');
const {readFileSync} = require('fs')

const homepage = readFileSync('../node-express-course/02-express-tutorial/navbar-app/index.html');

//requesting all files from HTML for resources
const homestyle = readFileSync('../node-express-course/02-express-tutorial/navbar-app/styles.css');
const homeimage = readFileSync('../node-express-course/02-express-tutorial/navbar-app/logo.svg');
const homelogic = readFileSync('../node-express-course/02-express-tutorial/navbar-app/browser-app.js');


const server = http.createServer((req, res) => {
//Providing metadata about our response  
//status code, headers 
console.log(req.url)

//Everytime server asks for resources from reading HTML, the server will have multiple connections
if (req.url === '/' || req.url === '/home'){
    res.writeHead(200, {'content-type' : 'text/html'})
    res.write(homepage)
} else if (req.url === '/browser-app.js') {
    res.writeHead(200, {'content-type' : 'text/javascript'})
    res.write(homelogic)
} else if (req.url === '/logo.svg') {
    res.writeHead(200, {'content-type' : 'image/svg+xml'})
    res.write(homeimage)
} else if (req.url === '/styles.css') {
    res.writeHead(200, {'content-type' : 'text/css'})
    res.write(homestyle)
} else {
    res.writeHead(404, {'content-type' : 'text/html'})
    res.write('Resource not Found!')
}

console.log(`End of response!`);
res.end()
})

server.listen(5000);