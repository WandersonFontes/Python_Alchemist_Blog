import Vue from 'vue'
import App from './App.vue'
import router from './routes.js'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueHorizontal from "vue-horizontal";
import VueMasonryWall from "vue-masonry-wall";
import VueObserveVisibility from 'vue-observe-visibility'


Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueHorizontal)
Vue.use(VueMasonryWall)
Vue.use(VueObserveVisibility)



new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
