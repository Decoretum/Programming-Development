import './App.css'
import React from 'react';
import Formresult from './Formresult';


let name = "Gael";

function justNumbers(string){
    return /^\d+$/.test(string);
  }

function getData(e){
    let cond = true;
      //getters
    let m = document.getElementById('Email').value;
    let n = document.getElementById('first').value;
    let o = document.getElementById('last').value;
    let p = document.getElementById('phone').value;

    //output
    let q = document.getElementById('email');
    let r = document.getElementById('firstn');
    let s = document.getElementById('lastn');
    let t = document.getElementById('pone');

      if (m != ''){
        console.log(m);
            }  
      if (n != ''){
        console.log(n);
      }
      if (o != ''){
        console.log(o)
      }
      if (p != ''){
        console.log(p)
      }

      if (m.includes('@') && (!m.includes('gmail.com') && !m.includes('yahoo.com'))){
        alert('Your Email has missing identifiers such as gmail.com/yahoo.com');
        cond = false;
      }
      else if (!m.includes('@')){
        alert('Your Email has missing identifiers such as @gmail/@yahoo and/or .com');
        cond = false;
      }
      
      if (o.slice(0,1) != o.slice(0,1).toUpperCase() || n.slice(0,1) != n.slice(0,1).toUpperCase()){
        alert('Name inputs should have a starting uppercase letter!');
        cond = false;
      }
      else if (o.length < 4 || n.length < 4){
        alert('Name is too short!');
        cond = false;
      }

      if (p.length < 11 || justNumbers(p) === false){
        alert('Number is too short and/or provided number contains letters');
        cond = false;
      }
      if (cond === true){
        alert('Account successfully created!');
        q.innerHTML = "Email: " + m;  
        r.innerHTML = "First Name: " + n;
        s.innerHTML = "Last Name: " + o;
        t.innerHTML = "Phone Number: " + p;

      }
      
        }


class Form extends React.Component {
    constructor(props){
        super(props);
        this.state={
            first: "",
            last:"",
            mail:"",
            phone:"",
            errors:""
        }
        this.emailFunc = this.emailFunc.bind(this);
        this.fnameFunc = this.fnameFunc.bind(this);
        this.lnameFunc = this.lnameFunc.bind(this);
        this.justNumbers = this.justNumbers.bind(this);
        this.pnameFunc = this.pnameFunc.bind(this);
    }

    //functions in class for input
        emailFunc(event){
        this.setState({mail: event.target.value});
            }

        fnameFunc(event){
            this.setState({first: event.target.value});
        }

        lnameFunc(event){
            this.setState({last: event.target.value});
        }

        justNumbers(string){
            return /^\d+$/.test(string);
        }

        pnameFunc(event){
            this.setState({phone: event.target.value});
        }


    

    render(){
        let errors = "";
        let errorsf = "";
        let errorsl = "";
        let errorsp = "";
        if (this.state.mail === ''){
            errors = <span></span>
        }
        else if (!this.state.mail.includes('@') && this.state.mail !== ''){
            errors = <span> Missing @ identifier </span>
        }
        else if (this.state.mail.includes('@') && (!this.state.mail.includes('gmail') && !this.state.mail.includes('yahoo'))){
            errors = <span> Missing gmail / yahoo identifier </span>
        }
        else if ((this.state.mail.includes('gmail') || this.state.mail.includes('yahoo')) && !this.state.mail.includes('.com')){
            errors = <span> Missing .com </span>
        }
        else{
            errors = <span> Email Accepted! </span>
        }  
        
        if (this.state.first.slice(0,1) !== this.state.first.charAt(0,1).toUpperCase()){
            errorsf = <span> First letter not in uppercase </span>
        }

        else if (this.state.first.slice(0,1) === this.state.first.slice(0,1).toUpperCase() && this.state.first !== '' && this.state.first.length >= 4){
            errorsf = <span> Accepted! </span>
        }

        if (this.state.last.slice(0,1) !== this.state.last.charAt(0,1).toUpperCase()){
            errorsl = <span> First letter not in uppercase </span>
        }

        else if (this.state.last.slice(0,1) === this.state.last.slice(0,1).toUpperCase() && this.state.last !== '' && this.state.last.length >= 4)
            errorsl = <span> Accepted! </span>

        
        if (this.state.phone.toString().length < 11 && this.state.phone !== ''){
            errorsp = <span> Number is missing {11 - this.state.phone.length} more digits </span>
        }

        else if (this.justNumbers(this.state.phone.toString()) === false && this.state.phone !== ''){
            errorsp = <span> Not a number! </span>
        }

        else if (this.state.phone.toString().length === 11){
            errorsp = <span> Accepted! </span>
        }

        else if (this.state.phone.toString().length > 11){
            errorsp = <span> Too much digits! </span>
        }

        
        return(
            <><div className='Form'>
                <span className="Header">{name}'s Signup Sheet</span> <br></br>
                <label for="Email"> Email: </label>
                <input className="inp" type="text" id="Email" value={this.state.mail} onChange={this.emailFunc} />
                <span className="errors">
                    {errors}
                </span>

                <br></br>

                <label for="first"> First Name: </label>
                <input className="inp" type="text" id="first" value={this.state.first} onChange={this.fnameFunc} />
                <span className="errors">
                    {errorsf}
                </span>

                <br></br>

                <label for="last"> Last Name: </label>
                <input className="inp" id="last" value={this.state.last} onChange={this.lnameFunc} />
                <span className="errors">
                    {errorsl}
                </span>

                <br></br>

                <label for="phone" /> Phone Number:
                <input className="inp" id="phone" value={this.state.phone} onChange={this.pnameFunc} />
                <span className="errors">
                    {errorsp}
                </span>

                <br></br>

                <button id="sub" onClick={getData}> Signup </button> <br></br><br></br>

                <span id="email" name="email"> </span><br></br>
                <span id="firstn" name="firstn"> </span><br></br>
                <span id="lastn" name="lastn"> </span><br></br>
                <span id="pone" name="pone"> </span>

            </div><br></br></>
            
        
    
    
            
    
        ); 
    }
    
}

export default Form;