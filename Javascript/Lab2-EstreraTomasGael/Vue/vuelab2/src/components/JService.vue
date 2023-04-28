<script>
import { createDOMCompilerError } from '@vue/compiler-dom';
import { onBeforeUpdate } from 'vue';

export default{
    data(){
        return{
            keeper : [],
            t : ''
        }
    },
    methods: {
        async random(){
            let array = []
            for (let i = 0; i < 5; i++){
                let minimum = Math.ceil(0);
                let maximum = Math.floor(150);
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
        
    },




}


</script>

<template>
    <main>
        <div v-for="i in this.keeper" id="list">
            <button @click="view"> Category ID:{{ i['num'] }}</button>
        </div>

    </main>
</template>