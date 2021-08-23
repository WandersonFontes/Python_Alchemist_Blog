<template>
  <div>
    <!-- <Slide></Slide> -->
    <div class='container'>
        <PyJobCard></PyJobCard>
        <PostCard></PostCard>
    </div>
  </div>
  
</template>

<script>
import PyJobCard from '../components/body/PyJobCard'
//import Slide from '../components/header/Slide'
import PostCard from '../components/body/PostCard'


export default {
    name: 'Home',
    components:{
        PyJobCard,
        PostCard,
        //Slide   
    },
}
</script>

<style>
.container{
  margin-top: 100px;
  padding-left: 80px;
  padding-right: 80px;
}

</style>