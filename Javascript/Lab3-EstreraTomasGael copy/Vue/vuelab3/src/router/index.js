import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CluesView from '../views/CluesView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      props: {default:true}
    },
    {
      path: '/about',
      name: 'about',
      props: {default:true},
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/Clues/:data/id/:num',
      name: 'clues123',  
      component: CluesView,
      props: {default:true},
      meta:{
        auth: true
      }
      
    }
  ]
})

export default router
