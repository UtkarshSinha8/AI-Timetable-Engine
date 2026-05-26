from ortools.sat.python import cp_model

from app.domain.entities import (
    ExpandedSession,
    TeacherAvailability
)

from app.solver.overlap import (
    slots_overlap
)

from app.solver.slot_mapper import (
    get_valid_start_slots
)

from app.solver.time_slots import (
    TimeSlot
)


def add_teacher_conflict_constraints(

    model: cp_model.CpModel,

    sessions: list[ExpandedSession],

    slots: list[TimeSlot],

    granularity_minutes: int,

    session_slot_variables,

    teacher_availabilities:
    list[TeacherAvailability]

):

    total_sessions = len(sessions)

    for i in range(total_sessions):

        session_a = sessions[i]

        for j in range(i + 1, total_sessions):

            session_b = sessions[j]

            # Skip if different teachers
            if (
                session_a.teacher_id
                !=
                session_b.teacher_id
            ):
                continue

            valid_slots_a = get_valid_start_slots(

                session=session_a,

                slots=slots,

                granularity_minutes=
                granularity_minutes,

                teacher_availabilities=
                teacher_availabilities
            )

            valid_slots_b = get_valid_start_slots(

                session=session_b,

                slots=slots,

                granularity_minutes=
                granularity_minutes,

                teacher_availabilities=
                teacher_availabilities
            )

            for slot_a in valid_slots_a:

                for slot_b in valid_slots_b:

                    if slots_overlap(

                        slot_a,

                        session_a.duration_minutes,

                        slot_b,

                        session_b.duration_minutes
                    ):

                        var_a = session_slot_variables[
                            (
                                session_a.expanded_session_id,
                                slot_a.slot_id
                            )
                        ]

                        var_b = session_slot_variables[
                            (
                                session_b.expanded_session_id,
                                slot_b.slot_id
                            )
                        ]

                        model.Add(
                            var_a + var_b <= 1
                        )