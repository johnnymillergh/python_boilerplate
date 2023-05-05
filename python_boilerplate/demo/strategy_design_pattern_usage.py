from loguru import logger


class BaseStrategy:
    _strategies: list["BaseStrategy"] = []

    @classmethod
    def init(cls) -> None:
        if len(cls._strategies) > 0:
            return
        strategy_classes = BaseStrategy.__subclasses__()
        cls._strategies = [
            strategy_class.__new__(strategy_class)
            for strategy_class in strategy_classes
        ]

    def strategy_name(self) -> str:
        return self.__class__.__name__

    def matches(self, data_input: str) -> bool:
        raise NotImplementedError(
            f"Function `{self.matches.__qualname__}` is not implemented"
        )

    def execute(self, data_input: str) -> None:
        raise NotImplementedError(
            f"Function `{self.execute.__qualname__}` is not implemented"
        )

    @classmethod
    def iter_execute(cls, data_input: str) -> None:
        strategies = list(filter(lambda x: x.matches(data_input), cls._strategies))
        if len(strategies) != 1:
            raise ValueError("No supported strategies found")
        strategies[0].execute(data_input)


class StrategyOne(BaseStrategy):
    def matches(self, data_input: str) -> bool:
        return "one" in data_input

    def execute(self, data_input: str) -> None:
        logger.info(f"Executing {self.strategy_name()} with: {data_input}")


class StrategyTwo(BaseStrategy):
    def matches(self, data_input: str) -> bool:
        return "two" in data_input

    def execute(self, data_input: str) -> None:
        logger.info(f"Executing {self.strategy_name()} with: {data_input}")
