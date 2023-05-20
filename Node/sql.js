const mysql = require('mysql2');
const {readFile, writeFile } = require('fs');
const path = require('path');
const { NONAME } = require('dns');


const passpath = path.join(__dirname, 'password.txt');

//asynchronous code


const password = () => {
    return new Promise((rej, res) =>{
        readFile(passpath, 'utf-8',(err,result)=>{
            if (err){
                rej(err);
            }
            else{
                res(result);
            }
        
        });

    })    
}



let pass = "";

password()
.then((res) => {
    pass = res;
})
.catch((err) => {
    console.log('error')
})

let pass2 = ""
readFile(passpath, 'utf-8',(err,result)=>{
    if (err){
    }
    else{
        console.log(result);
        pass2 = result
        const server = mysql.createConnection({
            host: 'localhost',
            user: 'root',
            password: pass2,
            //port: 3306,
            database: 'TAIWANSTEEL'
        })
        
        server.connect((err) => {
            if (err){
                console.log(err);
            }
            else{
                server.query("SHOW TABLES", (err, result, fields)=> {
                    if (err){
                        console.log(err);
                    }
                    else{
                        server.query("SELECT * FROM Inventory_finalorder", (err,result) => {
                            if (err){
                                console.log(err)
                            }
                            else{
                                console.log(result)
                            }
                        })
                    }
                });
            }
        })
    }

});
 




