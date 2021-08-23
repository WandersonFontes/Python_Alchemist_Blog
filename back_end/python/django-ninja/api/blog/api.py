from typing import List
from django.shortcuts import get_object_or_404
from ninja.router import Router
from ninja.orm import create_schema
from ninja.files import UploadedFile
from .schema import ProfileBody
from .models import Post, Profile, TagPost

router = Router()
ProfileSchema = create_schema(Profile)
PostSchema = create_schema(Post, depth=1)
TagPostSchema = create_schema(TagPost)

#PROFILES
@router.get("/profiles", response=List[ProfileSchema])
def list_profiles(request):
    'Get all profiles of blog' 
    data = Profile.objects.all()
    return data

@router.get("/profile/{id}", response=ProfileSchema)
def profile(request, id: int):
    'Get profile for user id' 
    data = Profile.objects.get(id=id)
    return data

@router.post("/profile/create/", response=ProfileSchema)
def create_profile(request, payload: ProfileSchema):
    'Create profile in blog'
    try:
       data = Profile.objects.get(user_id=payload.user)
    except Profile.DoesNotExist:
        data = Profile.objects.create(
            user_id=payload.user, 
            website=payload.website, 
            bio=payload.bio
        )
    data.save()
    return data

@router.put("/profile/{id}/edit", response=ProfileSchema)
def update_profile(request, id: int, payload: ProfileSchema):
    'Edit profile for user id' 
    try:
        data = Profile.objects.get(id=id)
        data.user_id = payload.user
        data.website = payload.website
        data.bio = payload.bio
        data.save()
        return data
    except Profile.DoesNotExist:
        return {"Profile Not Exist!"}
    

@router.delete("/profile/{id}/delete/")
def delete_profile(request, id: int):
    'Delete profile for user id' 
    try:
        data = Profile.objects.get(id=id)
        data.delete()
        return {"success": True, "return": "Profile Removed Sucessfuly!"}
    except Profile.DoesNotExist:
        return {"Profile Not Exist!"}
    

#POSTS
@router.get("/posts", response=List[PostSchema])
def list_posts(request):
    'Get all posts of blog' 
    data = Post.objects.all()
    return data

@router.get("/post/{id}", response=PostSchema)
def post(request, id: int):
    'Get posts for user id' 
    data = Post.objects.get(id=id)
    return data

@router.post("/post/create/", response=PostSchema)
def create_posts(request, payload: PostSchema):
    'Create posts in blog'
    data = Post.objects.create(
        slug=payload.slug,
        title=payload.title, 
        image = payload.image,
        short_description=payload.short_description,
        content=payload.content,
        date_created=payload.date_created,
        date_modified=payload.date_modified,
        publish_date=payload.publish_date,
        featured=payload.featured,
        status=payload.status,
        author=payload.author,
        tags=payload.tags,
    )
    data.save()
    return data

@router.put("/posts/{id}/edit", response=PostSchema)
def update_posts(request, id: int, payload: PostSchema):
    'Edit profile for user id' 
    data = Post.objects.get(id=id)
    data.title=payload.user, 
    data.website=payload.website, 
    data.slug=payload.slug,
    data.body=payload.body,
    data.meta_description=payload.meta_description,
    data.date_created=payload.date_created,
    data.date_modified=payload.date_modified,
    data.publish_date=payload.publish_date,
    data.published=payload.published,
    data.author = payload.author_id,
    data.tags=payload.tags,
    data.save()
    return data

@router.delete("/posts/{id}/delete/")
def delete_posts(request, id: int):
    'Delete profile for user id' 
    data = Post.objects.get(id=id)
    data.delete()
    return {"success": True}

#TAGPOSTS
@router.get("/tagposts", response=List[TagPostSchema])
def list_posts(request):
    'Get all posts of blog' 
    data = TagPost.objects.all()
    return data

@router.get("/tagpost/{id}", response=TagPostSchema)
def post(request, id: int):
    'Get posts for user id' 
    data = TagPost.objects.get(id=id)
    return data

@router.post("/tagpost/create/", response=TagPostSchema)
def create_tagposts(request, payload: TagPostSchema):
    'Create tagposts in blog'
    try:
        data = TagPost.objects.get(name=payload.name)
    except TagPost.DoesNotExist:
        data = TagPost.objects.create(
            name=payload.name, 
            status=payload.status
        )
        data.save()
    return data

@router.put("/tagposts/{id}/edit", response=TagPostSchema)
def update_tagposts(request, id: int, payload: TagPostSchema):
    'Edit profile for user id' 
    data = TagPost.objects.get(id=id)
    data.name = payload.name
    data.status = payload.status
    data.save()
    return data

@router.delete("/tagposts/{id}/delete/")
def delete_tagpost(request, id: int):
    'Delete profile for user id' 
    data = TagPost.objects.get(id=id)
    data.delete()
    return {"success": True}







