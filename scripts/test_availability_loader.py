from app.loaders.availability_loader import (
    load_teacher_availabilities
)


availabilities = load_teacher_availabilities(
    "data/teacher_availability.json"
)


print(availabilities)