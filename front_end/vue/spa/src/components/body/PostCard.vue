<template>
    <div class="post-cards">
        <div>
            <h1><b-icon icon="tags-fill"></b-icon> Tags</h1>
        </div>
        <div class="post-feature" @mousedown.left="onMouseDown">
            <vue-horizontal responsive ref="horizontal" class="horizontal" snap="none" :button="false" @scroll="onScroll">
                <div class="card" v-for="item in tags" :key="item.name" style="border: 0px !important;">
                    <b-card :title="'📌'+item.name" style="border: 0px !important;">
                        <!--<img class="img-fluid" src="../../../public/potion.gif" alt="Image" style="width: 25px;"/>-->
                    </b-card>
                </div>
            </vue-horizontal>
        </div>
        <div class="banner-centred">
            <b-card
                overlay
                img-src="https://www.sevenstarwebsolutions.com/wp-content/uploads/2019/06/django-banner-1.png"
                img-alt="Card Image"
            >
            </b-card>
        </div>
        <div>
            <vue-masonry-wall :items="posts" :options="{width: 460, padding: 20}" @append="append">
                <template v-slot:default="{item}">
                    <div class="card-shadow" @click="viewPost(item.id)">
                        <!--<b-card :title="item.title" img-src="../../../../../../back_end/python/django-ninja/api/blog/static/img/posts/2021_08_03/download.jpg" img-alt="Image" img-top> -->
                        <!--<img src="../../../../../../back_end/pyton/django-ninja/static/blog/posts/2021_07_25/img.jpg" alt="Image"/>-->
                        <img class="img-fluid" src="../../../../../../back_end/python/django-ninja/api/blog/static/img/posts/2021_08_03/download.jpg" alt="Image"/>
                        <!--<img class="img-fluid" :src="require(item.image)" alt="Responsive image"/> -->
                        <!--:src="`${item.image}`"  :src="require(`${item.image}`)"  :src="require(`@/xxx/${name}.png`)"-->
                        <b-card :title="item.title"> 
                        <b-card-text>
                            {{item.short_description}}
                        </b-card-text>
                        <b-card-text class="small text-muted">Atualizado em {{ item.date_created }}</b-card-text>
                        <!-- <b-card-text class="small text-muted">Last updated 3 mins ago</b-card-text> -->
                        </b-card>
                    </div>
                </template>
            </vue-masonry-wall>
        </div>
    </div>
</template>

<script>
import { blogApi } from '../../axiosApi.js'

export default {
    name: 'PostCard',
    data() {
      return {
        posts: [],
        posts_featured: [],
        tags: [],
        left: 0,
        originX: 0,
        originLeft: 0,
        }
    },
    created(){
        blogApi.get('/tagposts')
            .then(response =>{
                this.tags = response.data
            })
            .catch(err=>{
                console.log(err)
            }) 
        console.log()

    },
    destroyed() {
        this.onMouseUp()
    },
    methods: {
        append() {
            if(!this.end_items){
                blogApi.get('/posts')
                .then(response =>{
                    let i = 0;
                    for (i; i < response.data.length;) {
                        if(response.data[i].status){
                            this.posts.push({
                                id: response.data[i].id,
                                title: response.data[i].title, 
                                short_description: response.data[i].short_description, 
                                image:  '../../../../../../back_end/python/django-ninja' + response.data[i].image,
                                tags: response.data[i].tags,
                                date_created: new Date(response.data[i].date_created),
                            })
                            if(response.data[i].featured){
                                this.posts_featured.push({
                                    id: response.data[i].id,
                                    title: response.data[i].title, 
                                    tags: response.data[i].tags,
                                    date_created: new Date(response.data[i].date_created),
                                })
                            }
                        }
                        i++
                    }   
                    if(i == response.data.length){
                        //console.log("Total of Posts:"+i)
                        this.end_items = true;
                    }
                    this.posts_featured.reverse()
                })
                .catch(err=>{
                    console.log(err)
                }) 
            }           
        },
        viewPost(id){
            window.location='/post/'+id
        },
        onScroll({left}) {
            this.left = left
        },
        onMouseDown(e) {
            this.originX = e.pageX
            this.originLeft = this.left

            window.addEventListener("mouseup", this.onMouseUp);
            window.addEventListener("mousemove", this.onMouseMove);
        },
        onMouseUp() {
            window.removeEventListener("mouseup", this.onMouseUp);
            window.removeEventListener("mousemove", this.onMouseMove);
        },
        onMouseMove(e) {
            const offset = e.pageX - this.originX
            const left = this.originLeft - offset
            this.$refs.horizontal.scrollToLeft(left, 'auto')
        }
        
    }
}
</script>

<style>
.horizontal:active {
  cursor: grabbing;
  /*user-select: none;*/
}
.post-cards{
    margin-top: 50px;
}
.post-feature, .banner-centred{
    padding-bottom: 50px;
}
.card-shadow {
    /*border: 1px solid rgba(0,0,0,.125);*/
    cursor: pointer;
    -webkit-transition:  box-shadow .4s ease-out;
}
.card-shadow:hover{ 
     box-shadow: 1px 8px 20px grey;
    -webkit-transition:  box-shadow .4s ease-in;
}
</style>