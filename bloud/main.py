from fastapi import FastAPI

from bloud.api.word_cloud import router


app = FastAPI()

app.include_router(router, prefix="")
