import asyncio
from datetime import datetime
from threading import Timer
from time import time
from typing import Callable

from loguru import logger


def debounce(interval: float):
    """
    Decorator that will postpone a functions
    execution until after wait seconds
    have elapsed since the last time it was invoked.
    https://gist.github.com/walkermatt/2871026

    :param interval: interval time in seconds
    """

    def decorator(func: Callable):
        def debounced(*args, **kwargs):
            def call_it():
                func(*args, **kwargs)
                logger.debug(f"Called debounced function: {func.__qualname__}()")

            try:
                debounced.t.cancel()
                logger.debug(
                    f"Cancelled calling debounced function: {func.__qualname__}()"
                )
            except AttributeError:
                pass
            debounced.t = Timer(interval, call_it)
            debounced.t.start()

        return debounced

    return decorator


class _Wrapper:
    def __init__(self, initial_value=None) -> None:
        self._value = initial_value

    def get(self):
        return self._value

    def set(self, v):
        self._value = v


def async_debounce(interval: float):
    """
    Async debounce decorator.

    Python 中的防抖与节流 https://www.bilibili.com/read/cv13257868/
    Python 中的防抖与节流 https://www.moyu.moe/articles/25/

    :param interval: interval time in seconds
    """

    # 用于存储 asyncio.Task 实例，这里是闭包
    task_wrapper = _Wrapper()

    def decorator(fn):
        # Task 协程函数
        async def f(*args, **kwargs):
            # 进行休眠
            logger.debug("Set debounced function delay in {} seconds", interval)
            await asyncio.sleep(interval)

            # 调用函数
            f1 = fn(*args, **kwargs)
            logger.debug("Called debounced function, {}", fn)

            # 支持回调函数是异步函数的情况
            if asyncio.iscoroutine(f1):
                await f1

            # 清除 task_wrapper
            task_wrapper.set(None)

        def wrapper(*args, **kwargs):
            # 如果 task_wrapper 存在，说明在 delay 秒内调用过一次函数，此次调用应当重置计时器，因此取消先前的 Task
            if task_wrapper.get() is not None:
                task_wrapper.get().cancel()
                logger.debug("Task cancelled, {}", task_wrapper.get())

            # 创建 Task 并赋值变量 task_wrapper
            task_wrapper.set(asyncio.create_task(f(*args, **kwargs)))
            logger.debug(f"Created task: {task_wrapper.get()}")

        return wrapper

    return decorator


def throttle(interval: float):
    """
    Throttle decorator.
    Python 中的防抖与节流 https://www.bilibili.com/read/cv13257868/
    Python 中的防抖与节流 https://www.moyu.moe/articles/25/

    :param interval: interval time in seconds
    """

    # 下一次许可调用的时间，初始化为 0
    next_t = _Wrapper(0)

    def decorator(fn):
        def throttled(*args, **kwargs):
            # 当前时间
            now = time()
            # 若未到下一次许可调用的时间，直接返回
            if next_t.get() > now:
                return
            # 更新下一次许可调用的时间
            next_t.set(now + interval)
            # 调用函数并返回
            return fn(*args, **kwargs)

        return throttled

    return decorator


@async_debounce(1)
def debounced_example_1():
    logger.info(f"debounced_example_1 function: {datetime.now()}")
