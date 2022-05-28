from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.scraper import scraping_velog
from app.wordcloud import wordcloud


router = APIRouter()


@router.get("/search/{velog_id}")
async def search(velog_id: str, limit: int = 3):
    content = await scraping_velog(id=velog_id, limit=limit)
    img_path = wordcloud(content=content, id=velog_id)
    return FileResponse(path=img_path, media_type="image/png")
