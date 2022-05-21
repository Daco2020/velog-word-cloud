# import matplotlib.font_manager as fm
from datetime import datetime
from typing import Dict

import matplotlib.pyplot as plt

from wordcloud import WordCloud


def wordcloud(content: Dict[str, int], id: str):
    wc = WordCloud(
        max_font_size=200,
        background_color="white",
        width=800,
        height=800,
        font_path="/Users/daco/Library/Fonts/KoPub Dotum Bold.ttf",
    ).generate_from_frequencies(content)

    plt.figure(figsize=(10, 8))
    plt.imshow(wc)
    plt.tight_layout(pad=0)
    plt.axis("off")
    img_path = f"./app/img/@{id}_{datetime.now()}.png"
    plt.savefig(img_path)
    return img_path
