from dataclasses import dataclass
from typing import List


@dataclass
class TimeSlot:
    slot_id: int

    day_of_week: int

    start_minute: int
    end_minute: int


def generate_time_slots(
    start_hour: int,
    end_hour: int,
    slot_granularity_minutes: int,
    days_per_week: int = 7
) -> List[TimeSlot]:

    slots = []

    slot_id = 0

    start_minute_of_day = start_hour * 60
    end_minute_of_day = end_hour * 60

    for day in range(days_per_week):

        current = start_minute_of_day

        while current < end_minute_of_day:

            slot = TimeSlot(
                slot_id=slot_id,
                day_of_week=day,
                start_minute=current,
                end_minute=current + slot_granularity_minutes
            )

            slots.append(slot)

            slot_id += 1

            current += slot_granularity_minutes

    return slots