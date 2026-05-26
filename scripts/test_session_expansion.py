from app.loaders.session_loader import (
    load_sessions
)

from app.solver.session_expander import (
    expand_sessions
)


session_templates = load_sessions(
    "data/sessions.json"
)


expanded_sessions = expand_sessions(
    session_templates
)


for session in expanded_sessions:

    print(session)