import os
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

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Get the assigned PORT
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
