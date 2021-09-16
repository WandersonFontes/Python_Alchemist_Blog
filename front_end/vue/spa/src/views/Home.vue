<template>
  <div>
    <!-- <Slide></Slide> -->
    <div class='container'>
        <JobCard></JobCard>
        <PostCard></PostCard>
    </div>
  </div>
  
</template>

<script>
import JobCard from '../components/body/JobCard'
//import Slide from '../components/header/Slide'
import PostCard from '../components/body/PostCard'


export default {
    name: 'Home',
    components:{
        JobCard,
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