<template>
  <div class="container">
    <!--<img class="img-fluid" src="../../../../../back_end/python/django-ninja/api/blog/static/img/posts/2021_08_03/download.jpg" alt="Image"/>
    <img class="img-fluid" :src="postImage" alt="Image"/>-->
    <h1>{{ postTitle }}</h1>
    <span v-html="postContent"></span>
	</div>
</template>

<script>
import { blogApi } from '../axiosApi.js'

export default {
  data() {
    return {
      postTitle: null,
      postContent: null,
      postImage: null,
    }
  },
  created(){
    blogApi.get('/post/'+window.location.pathname.replace('/post/', ''),)
    .then(response =>{
      this.postTitle = response.data.title;
      this.postContent = response.data.content;
      this.postImage = '../../../../../back_end/python/django-ninja'+response.data.image;
      /*this.post.push({
        title: response.data.title, 
        content: response.data.content, 
        image:  '../../../../../../back_end/python/django-ninja' + response.data.image,
        date_created: new Date(response.data.date_created),
      })*/
    })
    /*.catch(err=>{
      console.log(err)
    }) */
  }

}
</script>

<style>

</style>