from app.solver.overlap import slots_overlap
from app.solver.time_slots import generate_time_slots


slots = generate_time_slots(
    start_hour=8,
    end_hour=22,
    slot_granularity_minutes=30
)


slot_a = slots[0]   # 8:00
slot_b = slots[4]   # 8:20
slot_c = slots[9]   # 8:45


print(
    slots_overlap(
        slot_a,
        duration_a=45,
        slot_b=slot_b,
        duration_b=60
    )
)

print(
    slots_overlap(
        slot_a,
        duration_a=45,
        slot_b=slot_c,
        duration_b=30
    )
)