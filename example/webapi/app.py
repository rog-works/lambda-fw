from logging import Logger
from typing import Optional

from lf2.apps.webapp import WebApp
from lf2.i18n.i18n import I18n
from lf2.lang.cache import Cache
from lf2.lang.di import DI


class MyApp(WebApp):
    __instance: Optional['MyApp'] = None

    @classmethod
    def get(cls) -> 'MyApp':
        if cls.__instance is None:
            raise AssertionError()

        return cls.__instance

    def __init__(self, di: DI) -> None:
        super(MyApp, self).__init__(di)
        MyApp.__instance = self

    @property
    def i18n(self) -> I18n:
        return self._di.resolve(I18n)

    @property
    def logger(self) -> Logger:
        return self._di.resolve(Logger)

    @property
    def cache(self) -> Cache:
        return self._di.resolve(Cache)
