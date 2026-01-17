from fastapi import FastAPI
from .routes import base

app = FastAPI()
app.include_router(base.base_router)

def run_dev():
    import uvicorn
    uvicorn.run("production_rag.main:app", host="0.0.0.0", port=5000, reload=True)