from fastapi import FastAPI

from app.api.routes.documents import router as documents_router
from app.core.config import settings
from app.api.routes.chat import router as chat_router


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

app.include_router(documents_router, prefix="/documents")
app.include_router(chat_router, prefix="/chat")


@app.get("/")
def root():
    return {"message": "PalmMind RAG API is running"}