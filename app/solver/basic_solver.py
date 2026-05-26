from ortools.sat.python import cp_model

from app.constraints.section_conflicts import (
    add_section_conflict_constraints
)

from app.constraints.teacher_conflicts import (
    add_teacher_conflict_constraints
)

from app.constraints.teacher_load import (
    validate_teacher_loads
)

from app.constraints.teacher_subjects import (
    validate_teacher_eligibility
)

from app.domain.entities import (
    SessionTemplate,
    Teacher,
    TeacherAvailability,
    TeacherEligibility,
    Subject,
    ScheduledSession,
    OptimizationConfig
)

from app.solver.slot_mapper import get_valid_start_slots
from app.solver.time_slots import TimeSlot
from app.constraints.subject_load import (
    validate_subject_weekly_minutes
)
from app.objectives.teacher_clustering import (
    build_teacher_clustering_penalties
)

from app.objectives.objective_manager import (
    apply_objective_function
)
from app.objectives.subject_spread import (
    build_subject_spread_penalties
)
from app.solver.session_expander import (
    expand_sessions
)
from app.objectives.occurrence_distribution import (
    build_occurrence_distribution_penalties
)

def solve_basic_timetable(

    sessions: list[SessionTemplate],

    slots: list[TimeSlot],

    granularity_minutes: int,

    teacher_availabilities: list[TeacherAvailability],

    teachers: list[Teacher],

    teacher_eligibilities: list[TeacherEligibility],
    subjects: list[Subject],
    optimization_config: OptimizationConfig

):

   
    # CREATE MODEL
    expanded_sessions = expand_sessions(
    sessions
    )

    model = cp_model.CpModel()

   
    # PRE-SOLVE VALIDATIONS
   

    validate_teacher_loads(
    sessions=sessions,
    teachers=teachers
)

    validate_subject_weekly_minutes(
    sessions=sessions,
    subjects=subjects
)

    validate_teacher_eligibility(
        sessions=expanded_sessions,
        teacher_eligibilities=teacher_eligibilities
    )

   
    # VARIABLE STORAGE
    

    session_slot_variables = {}

    
    # CREATE VARIABLES
   

    for session in expanded_sessions:

        valid_slots = get_valid_start_slots(
            session=session,
            slots=slots,
            granularity_minutes=granularity_minutes,
            teacher_availabilities=teacher_availabilities
        )

        variables = []

        for slot in valid_slots:

            var = model.NewBoolVar(
    f"expanded_session_"
    f"{session.expanded_session_id}_"
    f"slot_{slot.slot_id}"
)

            variables.append(var)

            session_slot_variables[
                (session.expanded_session_id, slot.slot_id)
            ] = var

       
        # EXACTLY ONE SLOT MUST BE CHOSEN
        

        model.Add(sum(variables) == 1)

   
    # SECTION CONFLICTS
    

    add_section_conflict_constraints(
        model=model,
        sessions=expanded_sessions,
        slots=slots,
        granularity_minutes=granularity_minutes,
        session_slot_variables=session_slot_variables,
        teacher_availabilities=teacher_availabilities
    )

   
    # TEACHER CONFLICTS
    
    add_teacher_conflict_constraints(
        model=model,
        sessions=expanded_sessions,
        slots=slots,
        granularity_minutes=granularity_minutes,
        session_slot_variables=session_slot_variables,
        teacher_availabilities=teacher_availabilities
    )

    objective_penalties = []

    teacher_clustering_penalties = (
        build_teacher_clustering_penalties(
            model=model,
            sessions=expanded_sessions,
            slots=slots,
            granularity_minutes=granularity_minutes,
            teacher_availabilities=teacher_availabilities,
            session_slot_variables=session_slot_variables,
            optimization_config=optimization_config
        )
    )

    objective_penalties.extend(
        teacher_clustering_penalties
    )

    subject_spread_penalties = build_subject_spread_penalties(
        model=model,
        sessions=expanded_sessions,
        slots=slots,
        granularity_minutes=granularity_minutes,
        teacher_availabilities=teacher_availabilities,
        session_slot_variables=session_slot_variables,
        optimization_config=optimization_config
    )

    objective_penalties.extend(
        subject_spread_penalties
    )

    occurrence_distribution_penalties = build_occurrence_distribution_penalties(
        model=model,
        sessions=expanded_sessions,
        slots=slots,
        granularity_minutes=granularity_minutes,
        teacher_availabilities=teacher_availabilities,
        session_slot_variables=session_slot_variables,
        optimization_config=optimization_config
    )

    objective_penalties.extend(
        occurrence_distribution_penalties
    )

    apply_objective_function(
        model=model,
        penalties=objective_penalties
    )

    # SOLVE

    solver = cp_model.CpSolver()

    status = solver.Solve(model)
            

    
    # OUTPUT
   

    if status == cp_model.OPTIMAL:

        scheduled_sessions = []

        

        for session in expanded_sessions:

            valid_slots = get_valid_start_slots(
                session=session,
                slots=slots,
                granularity_minutes=granularity_minutes,
                teacher_availabilities=teacher_availabilities
            )

            for slot in valid_slots:

                var = session_slot_variables[
                    (session.expanded_session_id, slot.slot_id)
                ]

                if solver.Value(var) == 1:

                    scheduled_session = ScheduledSession(
                        session_template_id=session.expanded_session_id,
                        teacher_id=session.teacher_id,
                        subject_id=session.subject_id,
                        section_ids=session.section_ids,
                        day_of_week=slot.day_of_week,
                        start_minute=slot.start_minute,
                        end_minute=(
                            slot.start_minute
                            +
                            session.duration_minutes
                        )
                    )

                    scheduled_sessions.append(
                        scheduled_session
                    )

    else:
        raise ValueError(
    "No feasible timetable solution found."
)

    return scheduled_sessions