from app.domain.entities import SessionTemplate

from app.loaders.json_utils import load_json_file


def load_sessions(
    file_path: str
) -> list[SessionTemplate]:

    raw_data = load_json_file(file_path)

    sessions = []

    for item in raw_data:

        session = SessionTemplate(

            session_template_id=item[
                "session_template_id"
            ],

            subject_id=item["subject_id"],

            teacher_id=item["teacher_id"],

            duration_minutes=item[
                "duration_minutes"
            ],

            sessions_per_week=item[
                "sessions_per_week"
            ],

            shared_session=item[
                "shared_session"
            ],

            section_ids=item["section_ids"]
        )

        sessions.append(session)

    return sessions