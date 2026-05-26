from app.domain.entities import (
    SessionTemplate,
    Teacher
)


def validate_teacher_loads(
    sessions: list[SessionTemplate],
    teachers: list[Teacher]
):

    for teacher in teachers:

        teacher_sessions = [

            session

            for session in sessions

            if session.teacher_id == teacher.teacher_id
        ]

        total_minutes = sum(
            session.duration_minutes
            for session in teacher_sessions
        )

        if total_minutes > teacher.max_weekly_load:

            raise ValueError(
                f"Teacher {teacher.name} exceeds "
                f"maximum weekly load. "
                f"Assigned: {total_minutes} mins, "
                f"Allowed: {teacher.max_weekly_load} mins."
            )