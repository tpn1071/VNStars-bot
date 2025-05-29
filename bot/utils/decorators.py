from typing import Callable, Any


def try_catch(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Lỗi khi gọi hàm {func.__name__}: {e}")
            # Có thể return giá trị mặc định hoặc None
            return None

    return wrapper


def try_catch_async(func: Callable[..., Any]) -> Callable[..., Any]:
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            print(f"Lỗi khi gọi hàm async {func.__name__}: {e}")
            return None

    return wrapper
