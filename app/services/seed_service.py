import json

from sqlalchemy.orm import Session

from app.core.config import LESSONS_FILE, QUIZ_FILE
from app.models.lesson import LessonDB
from app.models.quiz import QuizQuestionDB, AnswerOptionDB


def seed_lessons(db: Session):
    if db.query(LessonDB).first():
        return

    with LESSONS_FILE.open("r", encoding="utf-8") as f:
        lessons = json.load(f)

    for lesson in lessons:
        db.add(LessonDB(**lesson))

    db.commit()


def seed_quiz_questions(db: Session):
    if db.query(QuizQuestionDB).first():
        return

    with QUIZ_FILE.open("r", encoding="utf-8") as f:
        questions = json.load(f)

    for question in questions:
        question_db = QuizQuestionDB(
            id=question["id"],
            question=question["question"],
            explanation=question["explanation"],
        )

        for answer in question["answers"]:
            question_db.answers.append(
                AnswerOptionDB(
                    id=answer["id"],
                    text=answer["text"],
                    is_correct=answer["isCorrect"],
                )
            )

        db.add(question_db)

    db.commit()