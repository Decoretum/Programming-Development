import './App.css';
import * as ReactDOM from 'react-dom'
import React, { useEffect, useState } from 'react';
import { createElement } from 'react';
import { Outlet, Link } from "react-router-dom";    
//import { BrowserRouter as Router, Link } from "react-router-dom";

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
            //el.innerHTML += <Link to={`/Clues`}> Button ${this.state.actual[i][0]['num']} </Link>
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
        let one = document.getElementById('one');
        one.innerHTML += this.state.actual[0][0]['num'];
        for (let j = 0; j < this.state.actual[0].length; j++){
            one.dataset.val += JSON.stringify(this.state.actual[0][j]) + "|";
        }
        
        let two = document.getElementById('two');
        two.innerHTML += this.state.actual[1][0]['num'];
        for (let j = 0; j < this.state.actual[1].length; j++){
            two.dataset.val += JSON.stringify(this.state.actual[1][j]);
        }

        let three = document.getElementById('three');
        three.innerHTML += this.state.actual[2][0]['num'];
        for (let j = 0; j < this.state.actual[2].length; j++){
            three.dataset.val += JSON.stringify(this.state.actual[2][j]);
        }

        let four = document.getElementById('four');
        four.innerHTML += this.state.actual[3][0]['num'];
        for (let j = 0; j < this.state.actual[3].length; j++){
            four.dataset.val += JSON.stringify(this.state.actual[3][j]);
        }

        let five = document.getElementById('five');
        five.innerHTML += this.state.actual[4][0]['num'];
        for (let j = 0; j < this.state.actual[4].length; j++){
            five.dataset.val += JSON.stringify(this.state.actual[4][j]);
        }

        let prompt = document.getElementById('prompt');
        prompt.innerHTML = "Data is done Loading!";
    }

        render(){
            return(
                <>
                <div>
                    <h1 id="prompt"> Data is still loading! Wait! </h1>
                    <div id='temp'> 
                        <Link to={`/Clues`} id="one" state={{data: this.state.actual[0]}}> Button  </Link>
                        <Link to={`/Clues`} id="two" state={{data: this.state.actual[1]}}> Button  </Link>
                        <Link to={`/Clues`} id="three" state={{data: this.state.actual[2]}}> Button </Link>
                        <Link to={`/Clues`} id="four" state={{data: this.state.actual[3]}}> Button  </Link>
                        <Link to={`/Clues`} id="five" state={{data: this.state.actual[4]}}> Button  </Link>
                    </div>
                    
                </div>
                <br /><br /><br />
                </>
            )
        }
  


}


export default  Categories;


