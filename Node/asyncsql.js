const mysql = require('mysql2');
const {readFile, writeFile } = require('fs');
const path = require('path');
const http = require('http');


const passpath = path.join(__dirname, 'password.txt');

async function getPass(){
    return new Promise((resolve, reject)=>{
        readFile(passpath, 'utf-8',(err,result)=>{
            if (err){
                console.log(err);
                return;
            } else{
                resolve(result);
            }          
        });

    })
}

async function WebServer(){ 
    const data = await getPass();
    const server = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: data,
        //port: 3306,
        database: 'TAIWANSTEEL'
    })

    server.connect((err)=>{
        if (err){
            console.log(err);
            return;
        } else {         
            const web = http.createServer((req, res)=>{
                if (req.url === "/"){
                    res.write(`
                    <br>
                    <h1> Node JS Server and MySQL Database </h1>
                    <p> Click the buttons below for actions! </p>
                    <a href="/orders"> Orders </a>
                    `)
                    res.end();
                } else if (req.url === "/orders"){
                    server.query("SELECT * FROM Inventory_finalorder", (err,result)=>{
                        if (err){
                            console.log(err);
                        } else {
                            res.write(`
                            <a href="/"> Back to Home </a><br><br>
                            `)
                            for (let i of result){
                                let c = ""
                                server.query(`SELECT Name FROM Inventory_consignee WHERE id = ${i.BL_id}`,(err,result)=>{
                                    if (err){
                                        console.log(err)
                                    } else {
                                        c = result[0].Name
                                        res.write(`
                                        <div style="border:solid; padding: 15px; color: black;">
                                        Order ID: ${i.id}: <br> 
                                        Total Cost: $${i.TotalCost} <br>
                                        Place and Date of Issue: ${i.PlaceDate} <br>
                                        Port of Loading: ${i.Portload} <br>
                                        Port of Discharge: ${i.Portdis} <br>
                                        Consignee: ${c} <br>
                                        Prepaid: ${i.Prepaid} <br>
                                        
                                        </div>
                                        <br>
                                        `)
                                    }

                                })
                            }
                            //res.end();
                        }
                        
                    })
                }
            })
            web.listen(2019);
            
        }
    })


}

WebServer();