<template>
    <div class="Form">
        
        <span class="Header">Signup</span> <br>  
        <label for="Email"> Email: </label>
        <input class="inp" type="text" id="Email" v-model="mail">
        <span class="errors">
          <span v-if="mail == '' "> </span>
            <span v-else-if="!mail.includes('@') && mail != '' "> Missing @ identifier </span>
            <span v-else-if="mail.includes('@') && (!mail.includes('gmail') && !mail.includes('yahoo')) "> Missing gmail / yahoo identifier </span>
            <span v-else-if="(mail.includes('gmail') || mail.includes('yahoo')) && !mail.includes('.com')"> Missing .com </span>
            <span v-else> Email Accepted! </span>
        </span>
       
        <br>
 

        <label for="first"> First Name: </label>
        <input class="inp" type="text" id="first" v-model="first"> 
        <span class="errors">
            <span v-if="first.slice(0,1) != first.charAt(0,1).toUpperCase()"> First letter not in uppercase </span>
            <span v-else-if="first.slice(0,1) == first.slice(0,1).toUpperCase() && first != '' && first.length >= 4"> Accepted! </span>

       
        </span>
        
        <br>
        <label for="last"> Last Name: </label>
        <input class="inp" id="last" v-model="last">    
        <span class="errors">
            <span v-if="last.slice(0,1) != last.charAt(0,1).toUpperCase()"> First letter not in uppercase </span>
            <span v-else-if="last.slice(0,1) == last.slice(0,1).toUpperCase() && last != '' && last.length >= 4"> Accepted! </span>

        </span>

        <br>


        <label for="phone"> Phone Number: </label>
        <input class="inp" id="phone" v-model="ph"> 
        <span class="errors">
            <span v-if="ph === '' "> </span>
            <span v-else-if="ph.toString().length < 11 && ph != ''"> Number is missing {{ 11 - ph.toString().length }} more digits </span>
            <span v-else-if="justNumbers(ph.toString()) === false"> Not a number! </span>
            <span v-else-if="ph.toString().length === 11"> Accepted! </span>
            <span v-else-if="ph.toString().length > 11"> Too much digits! </span>
        </span><br>
        
        <button id="sub" @click="getData"> Signup </button>
    </div><br>


    <div class="info">
      <span id="email"> </span> <br>
      <span id="firstn"> </span> <br>
      <span id = "lastn"> </span> <br>
      <span id="pone"> </span> <br>
    </div>

</template>

<script>



export default{
    data(){
        return{
            mail : "",
            first : "",
            last : "",
            ph : "",
        }
    },
        methods:
            {

                getData(e){
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

                  if (p.length < 11 || this.justNumbers(p) === false){
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
                  
                    },

                  justNumbers(string){
                    return /^\d+$/.test(string);
                  },

                }
            }
        




</script>
<style>
.Form > *
{
    margin-top: 0vh;
}

.Form > *:not(.errors){
    position: relative;
    margin-top: 5vh;
}
.errors > *{
    color:black; 
    margin-left: 1vw;
    margin-top: 0vh;
}
.Header{
    font-size: 1.5em;
}
.Form{
    font-family:Verdana;
    border-radius: 9px;
    padding: 10px;
    color: black;
    box-shadow: 4px 4px rgb(138, 99, 95);
    background-color: bisque;
}



</style>