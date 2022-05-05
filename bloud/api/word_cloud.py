from fastapi import APIRouter, Body

from bloud.api.scraper import test_request


router = APIRouter()


@router.post("/search", tags=["word-cloud"])
async def create_word_cloud(url: str = Body(..., embed=True)):
    result = test_request(url)
    return {"result": result}
