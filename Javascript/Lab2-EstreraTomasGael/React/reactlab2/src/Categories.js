import './App.css';
import * as ReactDOM from 'react-dom'
import React, { useEffect, useState } from 'react';
import { createElement } from 'react';

let globally = []
async function random(){
    let array = []
    let counter = []
    for (let i = 0; i < 5; i++){
        let minimum = Math.ceil(0);
        let maximum = Math.floor(300);
        let res = Math.floor((Math.random() * (maximum-minimum) + minimum)); 
        array.push(res)
    }

    return array;
}

async function randomWithin(end){        
    let minimum = Math.ceil(0);
    let maximum = Math.floor(end-1);
    let res = Math.floor((Math.random() * (maximum-minimum) + minimum)); 
    
    return res;
}






class Categories extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            actual : []
        };
        
        this.Do = this.Do.bind(this);
        this.getval = this.getval.bind(this);
        this.after = this.after.bind(this);
    }

    getval(e){
        for (let i of this.state.actual){
            if (Number(i[0]['num']) === Number(e.target.innerHTML.replace("Button ",""))){
                let list = []
                console.log(i)
                e.target.innerHTML += '<br></br>'
                for (let j of i){
                    e.target.innerHTML += j.cont + "<br><br><br>"
                }
            }
        }
    }

    async Do () {
        console.log('Data should be fetched at this point through fetch API!')
        let data = await random();
        let more = []
        console.log(data)
        for (let j = 0; j < 5; j++){ //${data[j]}
            let fetchy = await fetch(`http://jservice.io/api/category?id=${data[j]}`);
            let converted = await fetchy.json();
            let cluelist = []
            for (let i of converted.clues){        
                let text = {
                    num : i.category_id,
                    cont : i.category_id + " " + i.id + " " + i.question + " " + " " + i.airdate + " " + i.answer + " " + i.category_id + " " + i.question + " " + i.value}
                cluelist.push(text)
               
            } 
            more.push(cluelist)
        }
        return more;
    }

    after() {
        let value = "";
        let el = document.getElementById('temp')
        for (let i = 0; i < this.state.actual.length; i++){
            for (let j of this.state.actual[i]){
                value += j;
            }

            //el.innerHTML += `<button> Button ${this.state.actual[i][0]} </button>` 
            const url = String(this.state.actual[i][0]['num']);
            const site = "http://jservice.io/api/category?id=" + url;
            let web = `"location.href="${site}"`;
            el.innerHTML += `<button onclick="${web}"> Button ${this.state.actual[i][0]['num']} </a> </button>`       
        }
    }

    componentDidMount(){
        this.Do().then(res => {
            this.setState({
                actual: res
            })
            //this.state.actual = res          
        })

    }

    componentDidUpdate(){
        this.after();
    }

        render(){
            return(
                <>
                <div>
                    <div id='temp' onClick={this.getval}> 
                 
                    </div>
                </div>
                </>
            )
        }
  


}


export default  Categories;


