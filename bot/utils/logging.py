import logging
import inspect
from typing import Callable, TypeVar, ParamSpec, cast, Any
from functools import wraps  # 🔥

P = ParamSpec("P")
R = TypeVar("R")

logger = logging.getLogger("discord_bot")


def log_function_call(func: Callable[P, R]) -> Callable[P, R]:
    msg = f"[CALL] {func.__name__}"

    if inspect.iscoroutinefunction(func):

        @wraps(func)
        async def async_wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
            print(msg)
            logger.info(msg)
            return await func(*args, **kwargs)

        return cast(Callable[P, R], async_wrapper)
    else:

        @wraps(func)
        def sync_wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
            print(msg)
            logger.info(msg)
            return func(*args, **kwargs)

        return cast(Callable[P, R], sync_wrapper)
