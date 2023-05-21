const mysql = require('mysql2');
const {readFile, writeFile } = require('fs');
const path = require('path');
const { NONAME } = require('dns');
const http = require('http');


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
                const web = http.createServer((req,res) => {
                    if (req.url === "/"){
                        server.query("SHOW TABLES",(err,result) => {
                            if (err){
                                console.log(err)
                            }
                            else{
                                res.write(` 

                                <a href="/orders"> Orders </a>
                                <br>
                                <h1> Database Tables </h1>
                                
                                `)
                                for (let i of result){
                                    res.write(`                 
                                    <br><br>
                                    `)
                                    res.write(i.Tables_in_taiwansteel)
                                }
                                res.end()
                            }
                        })
                    }

                    else if (req.url === "/orders"){
                        server.query("SELECT * FROM Inventory_finalorder", (err,result)=>{
                            if (err){
                                console.log(err)
                            }
                            else{
                                res.write(`
                                    <a href="/"> Back to Home </a>
                                `)
                                for (let i = 0; i < result.length; i++){
                                        server.query(`SELECT Name FROM Inventory_consignee WHERE id = ${result[i].BL_id}`, (err, name)=>{
                                            if (err){
                                                console.log(err)
                                            }
                                            else{
                                                let consignee = name[0].Name;
                                                if (result[i].Prepaid === 'Yes'){
                                                    res.write(`
                                                    <div style="border:solid; padding: 15px; color: black;">
                                                    Order ID: ${result[i].id}: <br> 
                                                    Total Cost: $${result[i].TotalCost} <br>
                                                    Place and Date of Issue: ${result[i].PlaceDate} <br>
                                                    Port of Loading: ${result[i].Portload} <br>
                                                    Port of Discharge: ${result[i].Portdis} <br>
                                                    Prepaid: ${result[i].Prepaid} <br>
                                                    Consignee: ${consignee} <br>
                                                    </div>
                                                    <br>
                                                    `);   
                                                }
                                                else{
                                                    res.write(`
                                                    <div style="border:solid; padding: 15px; color: black;">
                                                    Order ID: ${result[i].id}: <br> 
                                                    Total Cost: $${result[i].TotalCost} <br>
                                                    Place and Date of Issue: ${result[i].PlaceDate} <br>
                                                    Port of Loading: ${result[i].Portload} <br>
                                                    Port of Discharge: ${result[i].Portdis} <br>   
                                                    Collect: ${result[i].Collect}
                                                    Consignee: ${consignee} <br>
                                                    </div>
                                                    <br>
                                                `);
                                                }
                                            //res.end()
                                            }    
                                            //res.end()          
                                        })     
                                        //res.end()                  
                                }   

                                //res.end()
                            }
                            //res.end()
                        })
                        
                    }
                    

                    else{
                        res.write(`
                        <h1> No information regarding Database yet! </h1>
                        <p> Come back at a later time! </p>
                        `)
                    }
                    //res.end()
                })

                web.listen(2019);
            }            
        })
    }

});
 




