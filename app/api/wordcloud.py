from fastapi import APIRouter, Body
from fastapi.responses import FileResponse

from app.scraper import scraping_velog
from app.wordcloud import wordcloud


router = APIRouter()


@router.post("/search")
async def search(id: str = Body(..., embed=True)):
    content = await scraping_velog(id)
    img_path = wordcloud(content, id)
    return FileResponse(path=img_path, media_type="image/png")
