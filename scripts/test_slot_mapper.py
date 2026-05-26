from app.domain.entities import SessionTemplate
from app.solver.slot_mapper import get_valid_start_slots
from app.solver.time_slots import generate_time_slots


slots = generate_time_slots(
    start_hour=8,
    end_hour=22,
    slot_granularity_minutes=30
)


physics_session = SessionTemplate(
    session_template_id=1,
    subject_id=1,
    teacher_id=1,
    duration_minutes=45,
    sessions_per_week=3,
    shared_session=True,
    section_ids=[1, 2]
)


valid_slots = get_valid_start_slots(
    session=physics_session,
    slots=slots,
    granularity_minutes=30
)


print(f"Valid start slots: {len(valid_slots)}")

print()

for slot in valid_slots[:10]:
    print(slot)