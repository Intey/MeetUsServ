"""
Inject dependencies, and hide real functions
"""

def __init_create_meet():
    from functools import partial
    from storage.runtime import meet_store, user_store
    from ops.meets import create_meets_for_user as f
    return partial(f, user_store, meet_store)


def __init_user_meets():
    from functools import partial
    from storage.runtime import meet_store, user_store
    from ops.meets import get_meets_of_user as f
    return partial(f, user_store, meet_store)


create_meets_for_user = __init_create_meet()
get_meets_of_user = __init_user_meets()
