AI-Timetable-Engine

Production-oriented AI-powered timetable optimization engine for coaching institutes using Python and Google OR-Tools CP-SAT.

This project focuses on solving real-world academic scheduling problems using:

hard constraints
configurable soft constraints
recurrence scheduling
multi-objective optimization
scalable solver architecture

The system is designed to evolve into a complete production-grade scheduling platform with:

FastAPI
MySQL integration
frontend admin controls
optimization tuning sliders
timetable persistence and analytics
Features
Hard Constraints

The solver guarantees that all hard constraints are always satisfied.

Teacher Conflict Prevention

A teacher cannot conduct two overlapping sessions simultaneously.

Section Conflict Prevention

A section cannot attend multiple overlapping sessions.

Teacher Availability Enforcement

Sessions can only be scheduled within teacher availability windows.

Teacher Eligibility Mapping

Teachers can only teach:

mapped subjects
mapped sections
Subject Weekly Load Validation

Ensures required weekly academic load is satisfied.

Teacher Weekly/Daily Load Validation

Ensures teacher load limits are not exceeded.

Recurring Session Expansion

Supports:

multiple occurrences per week
recurrence-based scheduling

Example:

Math:
5 sessions/week

becomes:

Math occurrence 1
Math occurrence 2
Math occurrence 3
Math occurrence 4
Math occurrence 5

Each occurrence is independently schedulable.

Soft Constraints (Optimization Objectives)

The system supports configurable weighted optimization objectives.

Teacher Session Clustering

Prefers compact teacher schedules with fewer idle gaps.

Subject Spread Optimization

Attempts to distribute occurrences more evenly across the week.

Occurrence Distribution Optimization

Discourages excessive same-day concentration of recurring sessions.

Configurable Optimization Weights

Every soft constraint can be:

enabled
disabled
weighted dynamically

Future frontend sliders can directly control optimization priorities.

Example:

OptimizationConfig(
    teacher_clustering_weight=10,
    subject_spread_weight=5
)
Tech Stack
Current
Python
Google OR-Tools CP-SAT
JSON-based data ingestion
Planned
FastAPI
MySQL
SQLAlchemy
Docker
Frontend Admin Dashboard
Project Architecture
AI-Timetable-Engine/

├── app/
│
├── constraints/
│   ├── section_conflicts.py
│   ├── teacher_conflicts.py
│   ├── teacher_load.py
│   ├── teacher_eligibility.py
│   └── subject_load.py
│
├── objectives/
│   ├── teacher_clustering.py
│   ├── subject_spread.py
│   ├── occurrence_distribution.py
│   └── objective_manager.py
│
├── solver/
│   ├── basic_solver.py
│   ├── session_expander.py
│   ├── slot_mapper.py
│   ├── overlap.py
│   └── time_slots.py
│
├── loaders/
│   ├── session_loader.py
│   ├── teacher_loader.py
│   ├── subject_loader.py
│   ├── eligibility_loader.py
│   └── availability_loader.py
│
├── domain/
│   └── entities.py
│
├── data/
│   ├── sessions.json
│   ├── teachers.json
│   ├── subjects.json
│   ├── teacher_availability.json
│   └── teacher_eligibility.json
│
├── scripts/
│   ├── test_basic_solver.py
│   └── test_session_expansion.py
│
└── README.md
Solver Flow
Input Data
    ↓
Loaders
    ↓
Domain Entities
    ↓
Session Expansion
    ↓
Constraint Modeling
    ↓
Objective Modeling
    ↓
CP-SAT Optimization
    ↓
Scheduled Sessions
Recurrence Scheduling Architecture

The engine separates:

SessionTemplate

Represents:

weekly academic requirement

Example:

Physics
5 sessions/week
ExpandedSession

Represents:

one schedulable occurrence

Example:

Physics occurrence #3

This architecture allows:

realistic recurrence scheduling
recurrence-aware optimization
future advanced distribution algorithms
Optimization Engine Design

The system is built as a configurable optimization engine rather than a fixed timetable generator.

Hard constraints define:

feasible solution space

Soft constraints define:

solution quality

The solver minimizes weighted penalties using:

model.Minimize(total_penalty)

This enables different timetable behaviors without changing solver logic.

Performance Notes

The solver currently performs best with:

30-minute slot granularity

Using very fine granularity (e.g. 5-minute slots) dramatically increases:

variable count
pairwise constraints
optimization complexity
Example Optimization Tradeoff

High clustering weight:

teacher_clustering_weight=10
subject_spread_weight=1

Produces:

compact teacher schedules

High spread weight:

teacher_clustering_weight=1
subject_spread_weight=10

Produces:

more distributed weekly schedules
Future Roadmap
Database Integration
MySQL
SQLAlchemy repositories
persistent timetable storage
FastAPI Integration
timetable generation endpoint
optimization config endpoint
Frontend
admin dashboard
optimization sliders
timetable visualization
Advanced Optimization
student overlap minimization
section time preferences
dynamic batching
timetable analytics
Installation
Clone Repository
git clone https://github.com/YOUR_USERNAME/AI-Timetable-Engine.git
Create Virtual Environment
python -m venv venv
Activate Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
Install Dependencies
pip install ortools
Run Solver
python -m scripts.test_basic_solver
Example Output
ScheduledSession(
    session_template_id=1,
    teacher_id=1,
    subject_id=1,
    section_ids=[1],
    day_of_week=0,
    start_minute=480,
    end_minute=540
)
Key Engineering Concepts Used
Constraint Programming
CP-SAT Optimization
Multi-objective optimization
Recurrence scheduling
Weighted penalty systems
Scheduling heuristics
Optimization tradeoffs
Feasibility vs optimality
Domain-driven architecture
License

MIT License
