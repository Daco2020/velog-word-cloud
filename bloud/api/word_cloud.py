from fastapi import APIRouter, Body

from bloud.scraper import scraping_velog


router = APIRouter()


@router.post("/search")
async def search(id: str = Body(..., embed=True), limit: int = 50):
    result = await scraping_velog(id, limit)
    return {"result": result}
