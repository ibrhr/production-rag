from fastapi import FastAPI, APIRouter

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
async def root():
    return {"message": "Welcome to the Production RAG API"}
