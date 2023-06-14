const express = require('express')
const path = require('path')
const app = express()

const {products, people } = require('./data')

app.get('/', (req, res)=>{
    res.send('<h1> Home Page! </h1> <a href="/api/products"> Products </a> ');
})

//Getting objects and giving a JSON response 
app.get('/api/products', (req, res) => {
    console.log(req.query)
    let cleaned = products.map((a) => {
        const {id, name, image, price} = a;
        return {id, name, image, price}
    })

    res.json(cleaned);
})

//Route Parameters for a certain product object
app.get('/api/products/:ProdID', (req, res) => {
    //Represents the parameters of the path of the URL request path
    let params = req.params;
    let cond = false;
    let i = 0;
    while (i < products.length){
        if (products[i].id === Number(params.ProdID)){
            cond = true;
            break;
        }
        i++;
    }

    if (cond === true){
        let chosen = products.find((a) => a.id === Number(params.ProdID))
        res.json(chosen)
    } else {
        res.status(404).send(`<h1> Product of number ${params.ProdID} does not exist`);
    }
})

//route parameters for getting into the description of object
app.get('/api/products/:ProdID/:desc', (req, res) => {
    console.log(req.params)
    if (req.params.desc !== 'description'){
        res.send('The product does not have this property!');
    }
    let chosen = products.find((product) => product.id === Number(req.params.ProdID))
    if (!chosen){
        res.send('This product does not exist!')
    } else if (chosen && chosen.desc === null){
        res.send('This product does not have any description!')
    } else {
        res.send(`
        <h1>Product ${chosen.id} has the following description:</h1> <br><br>
        ${chosen.desc}.
        `)
    }
})

//Query String
//This will obtain query parameters from url 
//format of query=value&query=value and so on
app.get('/api/v1/query', (req, res) => {
    let {name, limit} = req.query
    let persons = []

    if (name === undefined && limit == undefined) {
        console.log('Incorrect Query format')
        let template = [{name: 'ex', id: 'number'}]
        return res.status(404).send(`
        <h1> Query for a person through the following query parameters: <br>
            name=${template[0].name}&id=${template[0].id}
        </h1>   
        `)
    }

    if (name !== undefined && limit === undefined){
        persons = people.filter((person) => {
            return person.name.startsWith(name);
        })
        if (persons.length === 0){
            return res.status(200).send(`<h1> No person starts with the letter ${name[0]} </h1>`);
        } 
        return res.send(persons);
    }

    if (name === undefined && limit !== undefined){
        persons = people.slice(0, Number(limit))
        return res.status(200).send(persons);
    }

    if (name){
        persons = people.filter((person) => {
            return person.name.startsWith(name);
        })
        if (persons.length === 0){
            return res.status(200).send(`<h1> No person exists with that name </h1>`)
        }
    } 
    
    if (limit){
        persons = persons.slice(0, Number(limit));
        return res.status(200).json(persons);
    } 
    
} )

app.listen(5000, ()=>{
    console.log('Server listened!')
})