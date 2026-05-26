from app.solver.time_slots import TimeSlot


def slots_overlap(
    slot_a: TimeSlot,
    duration_a: int,
    slot_b: TimeSlot,
    duration_b: int
) -> bool:

    # Different days can never overlap
    if slot_a.day_of_week != slot_b.day_of_week:
        return False

    a_start = slot_a.start_minute
    a_end = a_start + duration_a

    b_start = slot_b.start_minute
    b_end = b_start + duration_b

    return not (
        a_end <= b_start
        or
        b_end <= a_start
    )