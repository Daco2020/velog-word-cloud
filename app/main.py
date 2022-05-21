from fastapi import FastAPI

from app.api.wordcloud import router


app = FastAPI()

app.include_router(router, prefix="")
