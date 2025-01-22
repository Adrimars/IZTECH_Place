import uvicorn
from fastapi import FastAPI
from api.routes import router as api_router

app = FastAPI(
    title = "IZTECH/Place API",
    description= "API for IZTECH/Place project for controlling pixels with the help of MongoDB",
    version= "1.0.0"
)

app.include_router(api_router,prefix="/api",tags=["Pixels"])

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)