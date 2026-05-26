from app.loaders.subject_loader import (
    load_subjects
)


subjects = load_subjects(
    "data/subjects.json"
)


print(subjects)