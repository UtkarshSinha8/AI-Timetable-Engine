from app.loaders.eligibility_loader import (
    load_teacher_eligibilities
)


eligibilities = load_teacher_eligibilities(
    "data/teacher_eligibility.json"
)


print(eligibilities)