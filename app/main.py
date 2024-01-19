from fastapi import FastAPI
from router.company_routes import router as company_router  # Dizin yapısına göre güncellenmiş içe aktarma

app = FastAPI()

app.include_router(company_router, prefix="/api/v1/companies", tags=["companies"])

@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI"}