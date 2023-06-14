const express = require('express')
const path = require('path')
const app = express()

const {products, people } = require('./data')
//Using Middleware to do something with request data before it goes to response


app.listen(5000, (req, res) => {
    console.log(`Server is listening at Port 5000`);
})