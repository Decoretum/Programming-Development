<script>
import { onMounted } from 'vue';
import router from '../router'
export default{
    props: ['value'],
    
    data(){
        return{
            data: ""
        }
    },
    mounted(){
        console.log(this.$route.params)
        let ans = this.$route.params;
        let id = document.getElementById('blank');
        id.innerHTML = JSON.stringify(ans)
        let categ = document.getElementById('categ');
        categ.innerHTML += this.$route.params['num'] + "<br><br>"
    }
}


</script>
<template>
    <main>
        <h1 id="categ"> Category </h1>
        <p id="blank">  </p>   
    </main>
</template>