from fastapi import FastAPI

from app.api.word_cloud import router


app = FastAPI()

app.include_router(router, prefix="")
