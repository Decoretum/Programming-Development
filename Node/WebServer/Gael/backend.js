const {products, people } = require('./data')

const func1 = (req, res, next) => {
    if (req.method === 'GET'){
        console.log(`Request GET is done!`);
        res.status(200).send(
        `<h1> Howdy! This will feature all of the data for Products :) </h1>
        <br>
        <a href='/ProductList'> Products </a><br><br>
        <a href='/about'> About </a>    
        
        `)
    }
    next()
}

const func2 = (req, res, next) => {
    if (req.method === 'GET'){
        let content = ""
        for (let i =0; i < products.length; i++){
            let prod = products[i];
            content = content + 
            `<h1> Product ${prod.id}: ${prod.name} </h1>
            <a href = '/products/${prod.id}'> Details </a>
            `
        }
        content += `<br><br><br><br> <a href= '/'> Back to Home </a>`
        res.send(content);
    }
    next()
}

const about = (req, res, next) => {
    if (req.method === 'GET'){
        res.send(`
        <h1> About </h1>
        <p> This is Gael's Express JS Server </p>
        <a href='/'> Back to Home </a>
        `)
    }
}

const detail = (req, res, next) => {
    if (req.method === 'GET'){
        let {ProdID} = req.params
        let obj = products.find((product) => product.id === Number(ProdID))
        res.status(200).send(`
        <h1> Product ${obj.id}: ${obj.name} </h1>
            <p> 
                ${obj.image} <br><br>
                Description: <br>
                ${obj.desc} <br>
                Price: ${obj.price} <br>
            </p>
        `)
    }
    next()
}

const secret = (req, res, next) => {
    res.status(200).send(`
    <h1> Secrets to ${req.params.get('name')}! </h1>
    `)
}

module.exports.functions = [func1, func2, about, detail, secret]