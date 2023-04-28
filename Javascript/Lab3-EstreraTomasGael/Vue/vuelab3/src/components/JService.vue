<script>
import { RouterLink, RouterView } from 'vue-router'
import { createDOMCompilerError } from '@vue/compiler-dom';
import { onBeforeUpdate } from 'vue';
import router from '../router';

export default{
    data(){
        return{
            keeper : [],
            keys : [],
            t : '',
            props: [this.keeper]
        }
    },
    methods: {
        async random(){
            let array = []
            for (let i = 0; i < 5; i++){
                let minimum = Math.ceil(0);
                let maximum = Math.floor(300);
                let res = Math.floor((Math.random() * (maximum-minimum) + minimum)); 
                array.push(res);
            }
            return array;
        },

        async randomWithin(end){        
            let minimum = Math.ceil(0);
            let maximum = Math.floor(end-1);
            let res = Math.floor((Math.random() * (maximum-minimum) + minimum)); 
            
            return res;
        },

        async Do(){
            console.log('Data should be fetched at this point through fetch API!')
            let data = await this.random();
            for (let i = 0; i < 5; i++){
                this.keys.push(i);
                let fetchy = await fetch(`http://jservice.io/api/clues?category=${data[i]}`);
                let converted = await fetchy.json();
                let randomy = await this.randomWithin(converted.length)
                let arr = {
                    list : [],
                    num : data[i]
                }
                for (let i of converted){
                    arr['list'].push(i);
                }
                this.keeper.push(arr);
                
            }
        },


        view(e){
            console.log(this.keeper)
            for (let i of this.keeper){
                if (Number(e.target.innerHTML.replace("Category ID:","")) === Number(i['num'])){
                    let u = []
                    for (let j of i['list']){
                        u.push(Object.entries(j))
                    }
                    for (let k of u){
                        e.target.innerHTML += k + "<br><br>";
                    }
                }
            }

        }
        
    },

    mounted(){
        this.Do();
        console.log(this.keeper)
        
    },
}


</script>

<template>
    <main>
        <div v-for="i in this.keeper" id="list">
                <button @click="$router.push({ name: 'clues123', params: {num: i['num'] ,data: JSON.stringify(i)}})" :data-val=JSON.stringify(i)> Category ID:{{ i['num'] }}</button>
        </div>

    </main>
</template>