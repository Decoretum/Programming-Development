const express = require('express')
const path = require('path')
const {functions} = require('./backend')
const global = require('./global')
const authorize = require('./authorize')

const app = express()

//app.use() runs for every router (if url not provided)
//it runs first before router middleware method
//if url provided, then it runs for /path/child1/child2
//sequential

//app.use([global, authorize])
app.use(global)

app.use('/ProductList', functions[1]) //sequential as well, authorized function first
app.use('/about', functions[2])
app.use('/products/:ProdID', functions[3])
app.use('/secrets', [authorize, functions[4]])

//Using Middleware to do something with request data before it goes to response
app.get('/', functions[0], (req, res) => {
    console.log('<h1> hola </h1>')
})
app.get('/ProductList', (req, res) => {})
app.get('/about', (req, res) => {})
app.get('/products/:ProdID', (req, res) => {})
app.get('/secrets', (req, res) => {})

app.listen(5000, (req, res) => {
    console.log(`Server is listening at Port 5000`);
})