from app.domain.entities import (
    SessionTemplate,
    ExpandedSession
)


def expand_sessions(

    session_templates: list[SessionTemplate]

) -> list[ExpandedSession]:

    expanded_sessions = []

    expanded_session_id = 1

    for template in session_templates:

        for occurrence_index in range(
            template.sessions_per_week
        ):

            expanded_session = ExpandedSession(

                expanded_session_id=
                expanded_session_id,

                session_template_id=
                template.session_template_id,

                occurrence_index=
                occurrence_index,

                subject_id=
                template.subject_id,

                teacher_id=
                template.teacher_id,

                duration_minutes=
                template.duration_minutes,

                shared_session=
                template.shared_session,

                section_ids=
                template.section_ids
            )

            expanded_sessions.append(
                expanded_session
            )

            expanded_session_id += 1

    return expanded_sessions