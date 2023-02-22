<template>
    <div class="Form">
        
        <span class="Header">Signup</span> <br>  
        <label for="Email"> Email: </label>
        <input class="inp" type="text" id="Email" v-model="mail">
        <span class="errors">
            <span v-if="!mail.includes('@') && mail != '' "> Missing @gmail or @yahoo </span>
            <span v-else-if="mail == '' "> </span>
            <span v-else-if="mail.includes('@') && !mail.includes('.com') "> Missing .com </span>
            <span v-else> Email Accepted! </span>
        </span>
       
        <br>
 

        <label for="first"> First Name: </label>
        <input class="inp" id="first" v-model="first"> 
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
        <input class="inp" type="text" id="phone" v-model="ph"> 
        <span class="errors">
            <span v-if="ph.length < 11 && ph != ''"> Number is missing {{ 11 - ph.length }} </span>
            <span v-else-if="ph == ''"> </span>
            <span v-else> Number accepted! </span>
        </span><br>
        
        <button id="sub" @click="getData"> Signup </button>
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
                let m = document.getElementById('Email').value;
                let n = document.getElementById('first').value;
                let o = document.getElementById('last').value;
                let p = document.getElementById('phone').value;
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