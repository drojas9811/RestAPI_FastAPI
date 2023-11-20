from fastapi import Request,APIRouter,Depends,HTTPException,status 
from fastapi.templating import Jinja2Templates
import aiohttp
from starlette.responses import RedirectResponse, Response
from app.token import verify_token

router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="app/templates")

url = "http://localhost:8000"


def get_current_user(request:Request):
    token = request.cookies.get("access_token")
    print("entre",token)
    if not token:
        return None 
    else:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        return verify_token(token,credentials_exception)


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})




@router.get("/salir")
def salir(reponse:Response, request: Request):
    msj = ""
    response = RedirectResponse("/", status_code=302)
    response.delete_cookie("access_token")
    return response

@router.get("/login_web")
def login_web(request: Request):
    msj = ""
    
    return templates.TemplateResponse("login.html", {"request": request,"msj":msj})

@router.post("/login_web")
async def login_web(response:Response, request: Request):
    form = await request.form()
    usuario = {
        "username":form.get('username'),
        "password":form.get('password')
    }
    url_post = f"{url}/login/"
    async with aiohttp.ClientSession() as session:
        response = await session.request(method="POST",url=url_post,data=usuario)
        response_json = await response.json()
        if 'access_token' not in response_json:
            msj = "Usuario o contraseña incorrecto" 
            return templates.TemplateResponse("login.html", {"request": request,"msj":msj})
        response = RedirectResponse("/",status_code=302)
        response.set_cookie(key="access_token",value=response_json["access_token"])
        return response
