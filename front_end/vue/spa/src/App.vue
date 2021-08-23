<template>
  <div>
    <NavBar></NavBar>
    <!-- <Slide></Slide>-->
    <div id="app">
      <router-view/>
    </div>
    <!-- <ul>
      <li v-for="profiles in profile" :key="profiles.id">{{ profiles.bio }}</li>
    </ul>
    <ul>
      <li v-for="companys in company" :key="companys.id">{{ companys.company_name }} - {{ companys.cnpj }}</li>
    </ul>
    <div class="body">
      <ProfileCard></ProfileCard>  
      <ProfileImage></ProfileImage>
    </div>-->
  </div>
</template>

<script>
//import { getApi } from './axiosApi.js'
import NavBar from './components/header/NavBar'

export default {
  name: 'App',
  components:{
    NavBar,
  }
}
</script>

<style>

</style>
