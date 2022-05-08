from fastapi import APIRouter, Body

from bloud.api.scraper import test_request


router = APIRouter()

VELOG_URL_PREFIX = "https://velog.io/@"


@router.post("/search", tags=["word-cloud"])
async def create_word_cloud(id: str = Body(..., embed=True)):
    url = VELOG_URL_PREFIX + id
    result = await test_request(url)
    return {"result": result}
