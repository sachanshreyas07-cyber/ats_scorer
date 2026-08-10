import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.config import(
    ALLOWED_ORIGINS, 
    APP_DESCRIPTION, 
    APP_TITLE, 
    APP_VERSION, 
    SPACY_MODEL_PRIMARY, 
    SPACY_MODEL_SECONDARY, SENTENCE_TRANSFORMER_MODEL
)
from backend.api.routes import router

logger=logging.getLogger('ats_resume_scorer')

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Start up begin")

    import spacy

    try:
        app.state.nlp = spacy.load(SPACY_MODEL_PRIMARY)
    except OSError:
        app.state.nlp = spacy.load(SPACY_MODEL_SECONDARY)

    print("Before importing SentenceTransformer")

    print("Importing torch...")
    import torch
    print("✓ torch")

    print("Importing transformers...")
    import transformers
    print("✓ transformers")

    print("Importing sentence_transformers...")
    import sentence_transformers
    print("✓ sentence_transformers")

    print("Importing SentenceTransformer...")
    from sentence_transformers import SentenceTransformer
    print("✓ SentenceTransformer")

    print("Loading model...")
    model = SentenceTransformer("ml_model/sbert_resume_matcher")
    print("✓ Model loaded")

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