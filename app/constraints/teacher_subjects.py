from app.domain.entities import (
    SessionTemplate,
    TeacherEligibility
)


def validate_teacher_eligibility(

    sessions: list[SessionTemplate],

    teacher_eligibilities: list[TeacherEligibility]
):

    allowed_combinations = {

        (
            eligibility.teacher_id,
            eligibility.subject_id,
            eligibility.section_id
        )

        for eligibility in teacher_eligibilities
    }

    for session in sessions:

        for section_id in session.section_ids:

            key = (
                session.teacher_id,
                session.subject_id,
                section_id
            )

            if key not in allowed_combinations:

                raise ValueError(
                    f"Teacher {session.teacher_id} "
                    f"is not eligible to teach "
                    f"subject {session.subject_id} "
                    f"for section {section_id}"
                )