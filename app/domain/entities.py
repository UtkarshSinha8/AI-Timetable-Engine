from dataclasses import dataclass
from typing import List


@dataclass
class Teacher:
    teacher_id: int
    name: str
    max_daily_load: int
    max_weekly_load: int


@dataclass
class Section:
    section_id: int
    name: str
    batch_id: int


@dataclass
class Subject:
    subject_id: int
    name: str
    required_weekly_minutes: int


@dataclass
class TeacherAvailability:
    teacher_id: int
    day_of_week: int

    start_minute: int
    end_minute: int


@dataclass
class SessionTemplate:
    session_template_id: int

    subject_id: int
    teacher_id: int

    duration_minutes: int

    sessions_per_week: int

    shared_session: bool

    section_ids: List[int]

@dataclass
class TeacherEligibility:
    teacher_id: int
    subject_id: int
    section_id: int


@dataclass
class ScheduledSession:

    session_template_id: int

    teacher_id: int

    subject_id: int

    section_ids: list[int]

    day_of_week: int

    start_minute: int

    end_minute: int

@dataclass
class OptimizationConfig:

    teacher_clustering_weight: int

    subject_spread_weight: int

    student_overlap_weight: int

    same_subject_weight: int

    section_preference_weight: int

@dataclass
class ExpandedSession:

    expanded_session_id: int

    session_template_id: int

    occurrence_index: int

    subject_id: int

    teacher_id: int

    duration_minutes: int

    shared_session: bool

    section_ids: list[int]