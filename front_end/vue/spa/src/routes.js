import Vue from 'vue';
import VueRouter from 'vue-router' 
import Home from './views/Home'
import About from './views/About'
import Profiles from './views/Profiles'
import Post from './views/Post'


Vue.use(VueRouter)

export default new VueRouter({
    mode:'history',
    base: process.env.BASE_URL,
    routes:[
        {
            path:'/',
            name: 'home',
            component: Home,
        },
        {
            path:'/about',
            name: 'about',
            component: About,
        },
        {
            path:'/profile',
            name: 'profiles',
            component: Profiles,
        },
        {
            path:'/post/:id',
            name: 'post',
            component: Post,
        },

    ]
})