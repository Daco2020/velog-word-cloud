from pydantic import AnyUrl, BaseModel


class WordCloudInCreate(BaseModel):
    url: AnyUrl
