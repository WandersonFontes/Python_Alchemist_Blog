from typing import List
from django.shortcuts import get_object_or_404
from ninja.router import Router
from ninja.orm import create_schema
from .models import Company, Jobs, TagJobs

router = Router()

CompanySchema = create_schema(Company)
@router.get("/companys", response=List[CompanySchema])
def list_profile(request):
    'Get all profiles of blog'
    data = Company.objects.all()
    return data

@router.get("/company/{id}", response=CompanySchema)
def profile(resquest, id:int):
    'Get profile of blog for id'
    data = get_object_or_404(Company, id=id)
    return data

JobsSchema = create_schema(Jobs)
@router.get("/jobs", response=List[JobsSchema])
def list_posts(resquest):
    data = Jobs.objects.all()
    return data

@router.get("/job/{id}", response=JobsSchema)
def post(resquest, id:int):
    data = get_object_or_404(Jobs, id=id)
    return data

TagJobsSchema = create_schema(TagJobs)
@router.get("/tagJobs", response=List[TagJobsSchema])
def list_tagPosts(resquest):
    data = TagJobs.objects.all()
    return data

@router.get("/tagJob/{id}", response=TagJobsSchema)
def tagPost(resquest, id:int):
    data = get_object_or_404(TagJobs, id=id)
    return data
