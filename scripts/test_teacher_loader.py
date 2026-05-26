from app.loaders.teacher_loader import (
    load_teachers
)


teachers = load_teachers(
    "data/teachers.json"
)


print(teachers)