import traceback
import logging
import inspect
from typing import Any, Callable, TypeVar, ParamSpec, cast
from functools import wraps

# Type helpers
P = ParamSpec("P")
R = TypeVar("R")

logger = logging.getLogger("discord_bot")


def catch_all_errors(func: Callable[P, R]) -> Callable[P, R]:
    """
    Decorator để bắt tất cả lỗi trong function (cả async và sync).
    Giữ nguyên metadata của command (dùng functools.wraps).
    """
    if inspect.iscoroutinefunction(func):

        @wraps(func)
        async def async_wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                _log_exception(func, e)
                return None

        return cast(Callable[P, R], async_wrapper)

    else:

        @wraps(func)
        def sync_wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                _log_exception(func, e)
                return None

        return cast(Callable[P, R], sync_wrapper)


def _log_exception(func: Callable[..., Any], e: Exception) -> None:
    logger.error(f"[ERROR] Trong hàm '{func.__name__}': {e}")
    tb = "".join(traceback.format_exception(type(e), e, e.__traceback__))
    logger.error(tb)
