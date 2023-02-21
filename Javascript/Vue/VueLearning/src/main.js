import { createApp } from 'vue' //import ability to create app
import { createPinia } from 'pinia'

// components for app
// we import components from a single-file component

import App from './App.vue' //root components
import router from './router'

import './assets/main.css'

const app = createApp(App)
    
     //instance of application

app.use(createPinia())
app.use(router)


//we mount the app to a DOM element or selector string
app.mount('#app')
