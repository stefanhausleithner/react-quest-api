from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.db import Base, engine
from app.models import LessonDB, QuizQuestionDB, AnswerOptionDB
from app.core.config import FRONTEND_ORIGIN
from app.routers import lessons, quiz
from app.core.db import SessionLocal
from app.services.seed_service import seed_lessons, seed_quiz_questions

app = FastAPI(title="React Quest API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_ORIGIN],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(lessons.router)
app.include_router(quiz.router)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        seed_lessons(db)
        seed_quiz_questions(db)
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "React Quest API is running."}