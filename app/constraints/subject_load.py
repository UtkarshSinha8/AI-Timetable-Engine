from app.domain.entities import (
    SessionTemplate,
    Subject
)


def validate_subject_weekly_minutes(

    sessions: list[SessionTemplate],

    subjects: list[Subject]
):

    for subject in subjects:

        subject_sessions = [

            session

            for session in sessions

            if session.subject_id == subject.subject_id
        ]

        total_minutes = sum(

    session.duration_minutes
    *
    session.sessions_per_week

    for session in subject_sessions
)

        if total_minutes < subject.required_weekly_minutes:

            raise ValueError(
                f"Subject {subject.name} "
                f"requires "
                f"{subject.required_weekly_minutes} mins/week "
                f"but only "
                f"{total_minutes} mins assigned."
            )