

def __init_create_meet():
    from functools import partial
    from storage.runtime import meet_store, user_store
    from ops.meets import create_meets_for_user
    create_meets_for_user = partial(create_meets_for_user, user_store, meet_store)


create_meets_for_user = __init_create_meet()
