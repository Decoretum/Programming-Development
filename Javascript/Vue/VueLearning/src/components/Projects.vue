<script>
let Ongoing = ["Web Inventory Order Application"]
let Projects = ["POS System","SQL CRUD Application","Election Web Application"]

let total = Projects.concat(Ongoing);
Ongoing = []
Projects = []
let Projects1 = total.map(function(i){
    let orig = i;
    if (i.slice(-4) === "tion"){
        i = "Application: " + i;
        if (Ongoing.includes(orig)){
            Ongoing.push(i);
            return i;
        }
        else{
            Projects.push(i);
            return i;

        }
    }
    else if (i.slice(-4) === "stem"){
        i = "System: " + i;
        if (Ongoing.includes(orig)){
            Ongoing.push(i);
            return i;

        }
        else{
            Projects.push(i);
            return i;

        }
    }
})


console.log(Projects1);


export default{
    data(){
        return {
            P : Projects1,
            O : Ongoing
        }
    }
}
</script>

<template>
    <h1> Past Projects </h1>
        <li v-for="p in P">
        {{ p }}
        </li>
    

    <h1> Ongoing Project </h1>
    <li v-for="o in O">
        {{ o }}
    </li>


</template>