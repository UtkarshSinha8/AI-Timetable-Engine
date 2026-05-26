from ortools.sat.python import cp_model


def apply_objective_function(

    model: cp_model.CpModel,

    penalties: list
):

    total_penalty = sum(penalties)

    model.Minimize(total_penalty)