from ninja.main import NinjaAPI
from  api.blog.api import router as posts_router
from  api.jobs.api import router as jobs_router

api = NinjaAPI()
api.add_router('homologation/', posts_router)
#api.add_router('homologation/', jobs_router)
