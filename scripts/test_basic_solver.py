from app.solver.basic_solver import (
    solve_basic_timetable
)

from app.solver.time_slots import (
    generate_time_slots
)

from app.loaders.teacher_loader import (
    load_teachers
)

from app.loaders.subject_loader import (
    load_subjects
)

from app.loaders.session_loader import (
    load_sessions
)

from app.loaders.availability_loader import (
    load_teacher_availabilities
)

from app.loaders.eligibility_loader import (
    load_teacher_eligibilities
)
from app.domain.entities import (
    OptimizationConfig
)



# LOAD DATA


teachers = load_teachers(
    "data/teachers.json"
)

subjects = load_subjects(
    "data/subjects.json"
)

sessions = load_sessions(
    "data/sessions.json"
)

teacher_availabilities = load_teacher_availabilities(
    "data/teacher_availability.json"
)

teacher_eligibilities = load_teacher_eligibilities(
    "data/teacher_eligibility.json"
)
optimization_config = OptimizationConfig(

    teacher_clustering_weight=1,

    subject_spread_weight=7,

    student_overlap_weight=0,

    same_subject_weight=0,

    section_preference_weight=0
)


# GENERATE TIME SLOTS


slots = generate_time_slots(
    start_hour=8,
    end_hour=22,
    slot_granularity_minutes=30
)



# RUN SOLVER


scheduled_sessions = solve_basic_timetable(
    sessions=sessions,

    slots=slots,

    granularity_minutes=30,

    teacher_availabilities=teacher_availabilities,

    teachers=teachers,

    teacher_eligibilities=teacher_eligibilities,

    subjects=subjects,
    optimization_config=optimization_config
)

print("\nGENERATED TIMETABLE\n")

for scheduled_session in scheduled_sessions:

    print(scheduled_session)