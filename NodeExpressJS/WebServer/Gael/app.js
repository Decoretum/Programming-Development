const express = require('express')
const path = require('path')
const app = express()

const {products, people } = require('./data')

/*
We used a public folder for our static files for our server
Basically, the server will get resources that the HTML is needing (through hrefs and references)
static allows the server to pick up these resources in one directory
index.html will be AUTOMATICALLY the file as ROOT for an express server

If no resource found on a url path, automatically returns 404 error status code
*/

//app.use(express.static('./public'))

//Requests to serve
app.get('/', (req, res) => {
    // let filepath = path.join(__dirname, '../node-express-course/02-express-tutorial/navbar-app/index.html')
    // res.status(200).sendFile(filepath);
    
    res.json([
        {
        name: 'Gael',
        status: 'Student',
        spec: 'Software Development'
    },
        {
            power: 124
        }
    ])
    

    res.json(products)
        })

app.get('/about', (req, res) => {
    res.status(200).send('About page')
})

//all handles all http methods, whether get, put, or delete
//* represents all requests url paths
app.all('*', (req, res) => {
    res.status(404).send('<h1> Resource not found </h1>')
})

app.listen(5000, () => {
    console.log('Server is listening on port 5000');
})