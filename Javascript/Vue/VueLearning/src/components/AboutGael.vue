<script>
class Gael{
    constructor(Name, Strength, School){
        this.Name = Name;
        this.Strength = Strength;
        this.University = School;
        this.Hate = "";
        this.Mind = "";
        this.Result = "";
        this.Smart = "";
        this.Likes = ["Application","Software","Java"]
        this.Apt = {
            'Java': 0,
            'Python' : 0,
            'Javascript' : 0
        };
        this.Status = "";
    }

    Insight(){
        if (this.Mind === ""){
            this.Result = "None as of Now";
            this.Smart = false;
            this.Mind = "Learning!";
        }
        else{
            this.Smart = true;
        }
        
    }

    Learn(Lang){
        for (let i in this.Apt){
            if (i === Lang){
                this.Apt[i] += 1;
            }
        }
    }

    hAte() {
        if (this.Hate === ""){
            this.Hate = "Gael always hated front-end such as CSS! It blew his patience away one night!";
        }
    } 

    Busy(){
        this.Busy = true;
    }

    Free(){
        this.Busy = false;
    }
}


let Gael1 = new Gael("Gael","Programming","Ateneo");
Gael1.Insight();
Gael1.hAte();
Gael1.Busy();
Gael1.Free();
Gael1.Learn("Java");


export default{
    data(){
        return{
            mind : Gael1.Mind,
            hate : Gael1.Hate,
            likes : Gael1.Likes,
            cond : Gael1.Busy,
            Person: {
                str : Gael1.Strength,
                sch : Gael1.School,
                nam : Gael1.Name,
                apt : Gael1.Apt,
            },

            Fear: {
                word : "Absolute Front-end",
                death : "CSS"
            }
        }
    }
}

//vue directives
/* v-if, v-else-if, v-else
    v-for="x in JS data variable"
    v-bind
    v-on -> listens for events

*/
</script>

<template> 

    <h1> Skills </h1>
    Gael was always been <span v-text="mind"> </span><br>
    He is very competent in programming for back-end side of applications as well as Leetcode! <br>
    Gael enjoys: 
    <li v-for="i in likes"> 
        {{ i }}
    </li> <br>

    {{ hate }} <br>

    Gael's Busy status: {{ cond }} <br>
    <div class="" v-if="cond === true"> Gael is currently programming through different frameworks and Java. For the meantime, you can view his <a href="https://github.com/Decoretum"> Github </a> account. </div>
    <div class="" v-else> Gael is currently free! Feel free to message him at his <a href="https://www.facebook.com/profile.php?id=100011413710230" target="_blank"> Facebook </a> account. </div>
    <div class="" v-bind="Person"> For now, Gael 
        <span class="" v-if="Person.apt.Java < 1"> is still a begginner at Java. </span>  
        <span class="" v-else-if="Person.apt.Java >= 1"> is decently proficient at Java. </span>
        <span class="" v-else-if="Person.apt.Java >= 10"> is adept in Java. </span>
    </div>


</template>
