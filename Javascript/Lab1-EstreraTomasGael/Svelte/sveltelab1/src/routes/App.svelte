<script>
export let name = "Gael";

let mail = "";
let first = "";
let last = "";
let phone = ""; 

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

</script>

<main>
    <div class="Form">
        
        <span class="Header">{name}'s Signup</span> <br>  
        <label for="Email"> Email: </label>
        <input class="inp" type=text id="Email" bind:value={mail}>
        <span class="errors">
            {#if mail == ''}
            <span> </span> 

            {:else if !mail.includes('@') && mail != ''}
                <span> Missing @ identifier </span>

            {:else if mail.includes('@') && (!mail.includes('gmail') && !mail.includes('yahoo'))}
                <span> Missing gmail / yahoo identifier </span>

            {:else if (mail.includes('gmail') || mail.includes('yahoo')) && !mail.includes('.com')}
                <span> Missing .com </span>

            {:else}
                <span v-else> Email Accepted! </span> 
            {/if}
        </span>
        <br>
 

        <label for="first"> First Name: </label>
        <input class="inp" type=text id="first" bind:value={first}> 
        <span class="errors">
            {#if first.slice(0,1) != first.charAt(0,1).toUpperCase()}
            <span> First letter not in uppercase </span>

            {:else if first.slice(0,1) == first.slice(0,1).toUpperCase() && first != '' && first.length >= 4}
            <span> Accepted! </span>

            {/if}
        </span>
        
        <br>
        <label for="last"> Last Name: </label>
        <input class="inp" type=text id="last" bind:value={last}>    
        <span class="errors">
            {#if last.slice(0,1) != last.charAt(0,1).toUpperCase()}
            <span> First letter not in uppercase </span>

            {:else if last.slice(0,1) == last.slice(0,1).toUpperCase() && last != '' && last.length >= 4}
            <span> Accepted! </span>

            {/if}
        </span>

        <br>


        <label for="phone"> Phone Number: </label>
        <input class="inp" id="phone" type=text bind:value={phone}> 
        <span class="errors">
            {#if phone === '' }
            <span> </span>

            {:else if phone.toString().length < 11 && phone != ''}
            <span> Number is missing { 11 - phone.toString().length } more digits </span>

            {:else if justNumbers(phone.toString()) === false}
            <span> Not a number! </span>
,
            {:else if phone.toString().length === 11}
            <span> Accepted! </span>

            {:else if phone.toString().length > 11}
            <span> Too much digits! </span>

            {/if}
        </span><br>
        
        <button id="sub" on:click="{getData}"> Signup </button>
    </div><br>


    <div class="info">
      <span id="email"> </span> <br>
      <span id="firstn"> </span> <br>
      <span id = "lastn"> </span> <br>
      <span id="pone"> </span> <br>
    </div>

</main>






                
            
        


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
    max-width: 100%;
    width: 80vw;
}



</style>