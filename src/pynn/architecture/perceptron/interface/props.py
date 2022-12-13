from typing import Any


def props(obj: object, *args: Any, **kwargs: Any) -> None:
    print(obj, args, kwargs)
