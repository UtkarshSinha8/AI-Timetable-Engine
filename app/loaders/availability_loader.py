from app.domain.entities import (
    TeacherAvailability
)

from app.loaders.json_utils import (
    load_json_file
)


def load_teacher_availabilities(

    file_path: str

) -> list[TeacherAvailability]:

    raw_data = load_json_file(file_path)

    availabilities = []

    for item in raw_data:

        availability = TeacherAvailability(

            teacher_id=item["teacher_id"],

            day_of_week=item["day_of_week"],

            start_minute=item["start_minute"],

            end_minute=item["end_minute"]
        )

        availabilities.append(availability)

    return availabilities