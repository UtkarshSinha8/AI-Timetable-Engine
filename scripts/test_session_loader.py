from app.loaders.session_loader import (
    load_sessions
)


sessions = load_sessions(
    "data/sessions.json"
)


print(sessions)