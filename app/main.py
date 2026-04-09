from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Lane Detection API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/health")
def health():
    return {"status": "healthy"}