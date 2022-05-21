from datetime import datetime
from typing import Dict

import matplotlib.pyplot as plt

from fastapi import HTTPException
from wordcloud import WordCloud

from app.constant import FONT_PATH


def wordcloud(content: Dict[str, int], id: str):
    if not content:
        raise HTTPException(status_code=404, detail="Item not found")

    wc = WordCloud(
        max_font_size=200,
        background_color="white",
        width=800,
        height=800,
        font_path=FONT_PATH,
    ).generate_from_frequencies(content)

    plt.figure(figsize=(10, 8))
    plt.imshow(wc)
    plt.tight_layout(pad=0)
    plt.axis("off")

    img_path = f"./app/img/@{id}_{datetime.now()}.png"
    plt.savefig(img_path)

    return img_path
