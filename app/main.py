from fastapi import FastAPI 
import uvicorn 
from app.api.login.service.routes import login
from app.api.users.service.routes import users
from app.frontend.login.routes import loginWeb
from app.frontend.users.routes import usersWeb

app = FastAPI()
app.include_router(users)
app.include_router(login)
app.include_router(loginWeb)
app.include_router(usersWeb)

##
##app.mount(Routes.REGISTER, paquetes_app)  # /api/v1.0.0/signup
##app.mount(Routes.ACCOUNTS, accounts_app)  # /api/v1.0.0/accounts
##