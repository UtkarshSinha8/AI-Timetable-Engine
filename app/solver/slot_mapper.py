from typing import List

from app.domain.entities import (
    SessionTemplate,
    TeacherAvailability
)

from app.solver.time_slots import TimeSlot


def get_valid_start_slots(
    session: SessionTemplate,

    slots: List[TimeSlot],

    granularity_minutes: int,

    teacher_availabilities: List[TeacherAvailability]
) -> List[TimeSlot]:

    required_slots = (
        session.duration_minutes // granularity_minutes
    )

    valid_slots = []

    total_slots = len(slots)

    
    # Get teacher availability for this teacher
    

    teacher_windows = [

        availability

        for availability in teacher_availabilities

        if availability.teacher_id == session.teacher_id
    ]

    for i in range(total_slots):

        start_slot = slots[i]

        end_index = i + required_slots - 1

        if end_index >= total_slots:
            continue

        end_slot = slots[end_index]

       
        # Must stay on same day
       

        if start_slot.day_of_week != end_slot.day_of_week:
            continue

        expected_end = (
            start_slot.start_minute
            +
            session.duration_minutes
        )

        if end_slot.end_minute != expected_end:
            continue

        
        # Check teacher availability
        

        fits_teacher_window = False

        for window in teacher_windows:

            if (
                start_slot.day_of_week
                ==
                window.day_of_week
            ):

                if (
                    start_slot.start_minute
                    >=
                    window.start_minute
                ) and (
                    expected_end
                    <=
                    window.end_minute
                ):

                    fits_teacher_window = True
                    break

        if not fits_teacher_window:
            continue

        valid_slots.append(start_slot)

    return valid_slots