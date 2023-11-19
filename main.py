from fastapi import FastAPI 
import uvicorn 
from app.db.database import Base,engine
from app.routers import user,auth,web

app = FastAPI()
app.include_router(user.router)

app.include_router(auth.router)
app.include_router(web.router)
