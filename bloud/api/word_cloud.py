from fastapi import APIRouter

from bloud.api.scraper import test_request


router = APIRouter()


@router.post("/word-cloud", tags=["word-cloud"])
async def create_word_cloud():

    mock_url = "https://velog.io/@locked/Flutter-3D-Layer-Card"
    r = test_request(mock_url)

    return {"message": r}
