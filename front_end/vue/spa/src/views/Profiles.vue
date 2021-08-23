<template>
  <div class='profile'>
      <h1>
          CONTAS
      </h1>
      <ul>
        <li v-for="profiles in profile" :key="profiles.id">{{ profiles.bio }}</li>
      </ul>
  </div>
</template>

<script>
import { blogApi } from '../axiosApi.js'

export default {
  name: 'Profile',
  data (){
    return {
      apiData:[],
      profile:null,
      company:null
    }
  },
  components:{
  },
  created (){
    blogApi.get('/profiles',)
      .then(response =>{
        this.profile = response.data
      })
      .catch(err=>{
        console.log(err)
      })
  }
}
</script>

<style>

</style>