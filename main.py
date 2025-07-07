import uvicorn
from fastapi import FastAPI

from api.v1.generator import router as generator_router

app = FastAPI()


app.include_router(
    generator_router,
    prefix="/api/v1/generator",
    tags=["generator"]
)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
