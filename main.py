from fastapi import FastAPI
from pythainlp.tag import pos_tag

app = FastAPI()

@app.get("/is_noun/{word}")
async def is_noun(word: str):
    tags = pos_tag([word], corpus="orchid")
    for w, tag in tags:
        if tag == "NCMN":
            return {"word": word, "is_noun": True}
    return {"word": word, "is_noun": False}
