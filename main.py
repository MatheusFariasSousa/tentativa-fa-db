from fastapi import FastAPI
from routes.user_route import router
from routes.product_route import client

app = FastAPI()

@app.get("/health-check")
def health_check():
    return "works"

app.include_router(router=router)
app.include_router(router=client)




