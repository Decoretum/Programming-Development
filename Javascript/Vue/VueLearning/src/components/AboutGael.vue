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

    hAte() {
        if (this.Hate === ""){
            this.Hate = "Gael always hated front-end such as CSS! It blew his patience away one night!";
        }
    } 
}


let Gael1 = new Gael("Gael","Programming","Ateneo");
Gael1.Insight();
Gael1.hAte();

export default{
    data(){
        return{
            mind : Gael1.Mind,
            hate : Gael1.Hate,
            likes : Gael1.Likes,

            Fear: {
                word : "Absolute Front-end",
                death : "CSS"
            }
        }
    }
}
</script>

<template>

    <h1> Skills </h1>
    Gael was always been <span v-text="mind"> </span><br>
    He is very competent in programming for back-end side of applications as well as Leetcode! <br>
    Gael enjoys: 
    <li v-for="i in likes">
        {{ i }}
    </li> <br>

    {{ hate }}


</template>
