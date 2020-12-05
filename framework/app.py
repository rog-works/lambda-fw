from logging import Logger
from typing import Callable, Optional, Type, TypeVar

from framework.api.api import Api
from framework.data.config import Config
from framework.i18n.i18n import I18n
from framework.lang.di import DI

_T = TypeVar('_T')


class App:
    __instance: Optional['App'] = None

    @classmethod
    def get(cls) -> 'App':
        if cls.__instance is None:
            raise AssertionError()

        return cls.__instance

    @classmethod
    def create(cls, di: DI) -> 'App':
        cls.__instance = cls(di)
        return cls.__instance

    def __init__(self, di: DI) -> None:
        self._di = di

    @property
    def config(self) -> Config:
        return self._di.resolve(Config)

    @property
    def i18n(self) -> I18n:
        return self._di.resolve(I18n)

    @property
    def logger(self) -> Logger:
        return self._di.resolve(Logger)

    @property
    def api(self) -> Api:
        return self._di.resolve(Api)

    def perform(self, runner: Type[Callable[..., _T]], *args, **kwargs) -> _T:
        return (self._di.resolve(runner))(*args, **kwargs)
