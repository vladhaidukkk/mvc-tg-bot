from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def build(*args: any, **kwargs: any) -> any:
        pass
