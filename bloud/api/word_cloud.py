from fastapi import APIRouter

from bloud.api.scraper import test_request
from bloud.schemas import WordCloudInCreate


router = APIRouter()


@router.post("/word-cloud", tags=["word-cloud"])
async def create_word_cloud(url_in: WordCloudInCreate):
    r = test_request(url_in.url)
    return {"message": r}
