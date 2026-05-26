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


def build_occurrence_distribution_penalties(

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

    total_sessions = len(sessions)

    for i in range(total_sessions):

        session_a = sessions[i]

        for j in range(i + 1, total_sessions):

            session_b = sessions[j]

            # SAME TEMPLATE ONLY
            if (
                session_a.session_template_id
                !=
                session_b.session_template_id
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

                    # SAME DAY ONLY
                    if (
                        slot_a.day_of_week
                        !=
                        slot_b.day_of_week
                    ):
                        continue

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

                    pair_penalty = model.NewIntVar(
                        0,
                        weight,
                        f"distribution_penalty_"
                        f"{session_a.expanded_session_id}_"
                        f"{session_b.expanded_session_id}_"
                        f"{slot_a.slot_id}_"
                        f"{slot_b.slot_id}"
                    )

                    # penalty applies only if BOTH selected
                    model.Add(
                        pair_penalty == weight
                    ).OnlyEnforceIf([
                        var_a,
                        var_b
                    ])

                    model.Add(
                        pair_penalty == 0
                    ).OnlyEnforceIf(
                        var_a.Not()
                    )

                    model.Add(
                        pair_penalty == 0
                    ).OnlyEnforceIf(
                        var_b.Not()
                    )

                    penalties.append(
                        pair_penalty
                    )

    return penalties