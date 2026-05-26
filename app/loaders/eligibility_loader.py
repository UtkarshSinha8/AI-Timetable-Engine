from app.domain.entities import (
    TeacherEligibility
)

from app.loaders.json_utils import (
    load_json_file
)


def load_teacher_eligibilities(

    file_path: str

) -> list[TeacherEligibility]:

    raw_data = load_json_file(file_path)

    eligibilities = []

    for item in raw_data:

        eligibility = TeacherEligibility(

            teacher_id=item["teacher_id"],

            subject_id=item["subject_id"],

            section_id=item["section_id"]
        )

        eligibilities.append(eligibility)

    return eligibilities