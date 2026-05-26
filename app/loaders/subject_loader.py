from app.domain.entities import Subject

from app.loaders.json_utils import load_json_file


def load_subjects(file_path: str) -> list[Subject]:

    raw_data = load_json_file(file_path)

    subjects = []

    for item in raw_data:

        subject = Subject(

            subject_id=item["subject_id"],

            name=item["name"],

            required_weekly_minutes=item[
                "required_weekly_minutes"
            ]
        )

        subjects.append(subject)

    return subjects