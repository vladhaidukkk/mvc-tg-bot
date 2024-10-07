from abc import ABC, abstractmethod


class BaseBuilder(ABC):
    @abstractmethod
    def build(*args: any, **kwargs: any) -> any:
        pass
