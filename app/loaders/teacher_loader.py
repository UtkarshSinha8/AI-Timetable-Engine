from app.domain.entities import Teacher

from app.loaders.json_utils import load_json_file


def load_teachers(file_path: str) -> list[Teacher]:

    raw_data = load_json_file(file_path)

    teachers = []

    for item in raw_data:

        teacher = Teacher(

            teacher_id=item["teacher_id"],

            name=item["name"],

            max_daily_load=item["max_daily_load"],

            max_weekly_load=item["max_weekly_load"]
        )

        teachers.append(teacher)

    return teachers