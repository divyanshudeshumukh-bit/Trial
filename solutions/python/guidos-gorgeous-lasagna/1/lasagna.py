EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Return remaining bake time."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Return preparation time based on layers."""
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return total elapsed time (prep + baking)."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time