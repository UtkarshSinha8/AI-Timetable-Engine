from ortools.sat.python import cp_model

from app.domain.entities import (
    ExpandedSession,
    OptimizationConfig
)

from app.solver.slot_mapper import (
    get_valid_start_slots
)

from app.solver.time_slots import (
    TimeSlot
)


def build_subject_spread_penalties(

    model: cp_model.CpModel,

    sessions: list[ExpandedSession],

    slots: list[TimeSlot],

    granularity_minutes: int,

    teacher_availabilities,

    session_slot_variables,

    optimization_config: OptimizationConfig
):

    penalties = []

    weight = (
        optimization_config
        .subject_spread_weight
    )

    if weight == 0:

        return penalties

    for session in sessions:

        valid_slots = get_valid_start_slots(

            session=session,

            slots=slots,

            granularity_minutes=
            granularity_minutes,

            teacher_availabilities=
            teacher_availabilities
        )

        for slot in valid_slots:

            var = session_slot_variables[
                (
                    session.expanded_session_id,
                    slot.slot_id
                )
            ]

            penalty_value = (
                slot.day_of_week
                *
                weight
                *
                100
            )

            penalty_var = model.NewIntVar(
                0,
                100000,
                f"subject_spread_penalty_"
                f"{session.expanded_session_id}_"
                f"{slot.slot_id}"
            )

            model.Add(
                penalty_var == penalty_value
            ).OnlyEnforceIf(var)

            model.Add(
                penalty_var == 0
            ).OnlyEnforceIf(var.Not())

            penalties.append(
                penalty_var
            )

    return penalties