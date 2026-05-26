# building deep copy of the state to further use in upstream

from copy import deepcopy


def create_state_snapshot(state):  # type: ignore

    return deepcopy(  # type: ignore
        state.model_dump()  # type: ignore
    )
