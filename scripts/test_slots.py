from app.solver.time_slots import generate_time_slots


slots = generate_time_slots(
    start_hour=8,
    end_hour=22,
    slot_granularity_minutes=30
)

print(f"Total slots generated: {len(slots)}")

print()

for slot in slots[:10]:
    print(slot)