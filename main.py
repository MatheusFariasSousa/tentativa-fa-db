from fastapi import FastAPI
from routes.user_route import router
from routes.product_route import client
from routes.sale_route import rota
from routes.front_route import front_router
from fastapi.staticfiles import StaticFiles 

app = FastAPI()

@app.get("/health-check")
def health_check():
    return "works"

app.include_router(router=router)
app.include_router(router=client)
app.include_router(router=rota)
app.include_router(router=front_router)


app.mount("/static",StaticFiles(directory="static"),name="static")



