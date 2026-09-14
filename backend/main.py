import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sentence_transformers import SentenceTransformer

from backend.core.config import (
    ALLOWED_ORIGINS,
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
    SPACY_MODEL_PRIMARY,
    SPACY_MODEL_SECONDARY,
    SENTENCE_TRANSFORMER_MODEL,
)

from backend.api.routes import router


logger = logging.getLogger("ats_resume_scorer")


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Start up begin")

    # Load spaCy model
    import spacy

    try:
        app.state.nlp = spacy.load(SPACY_MODEL_PRIMARY)
    except OSError:
        app.state.nlp = spacy.load(SPACY_MODEL_SECONDARY)

    print("[OK] spaCy model loaded")

    # Load fine-tuned SentenceTransformer model
    print("Loading SentenceTransformer model...")

    model = SentenceTransformer(SENTENCE_TRANSFORMER_MODEL)

    print("[OK] SentenceTransformer model loaded")

    app.state.embedder = model

    yield

    logger.info("Shutting down the API")


app=FastAPI(
    title=APP_TITLE, 
    description=APP_DESCRIPTION, 
    version=APP_VERSION, 
    lifespan=lifespan,
    docs_url='/docs',
    redoc_url='/redoc'
)
    
app.add_middleware(
    CORSMiddleware, 
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True, 
    allow_methods     = ['*'],
    allow_headers     = ['*'],

)

app.include_router(router)

@app.get('/')
async def root():
    return {
        'name':      'ATS Resume Analyzer API',
        'version':   '2.0.0',
        'endpoints': {
            'POST   /api/v1/analyze-resume': 'Analyze a resume',
            'GET    /api/v1/history':        'Get user history',
            'DELETE /api/v1/history/:id':    'Delete a history entry',
            'GET    /api/v1/health':         'Health check',
            'POST   /api/v1/generate-pdf':   'Generate PDF report from data',
        },
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )