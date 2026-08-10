from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

@asynccontextmanager
async def lifespan(app):
    print("1")

    import spacy
    spacy.load("en_core_web_md")
    print("2")

    from sentence_transformers import SentenceTransformer
    print("3")

    SentenceTransformer("ml_model/sbert_resume_matcher")
    print("4")

    yield

app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        reload=False,
    )