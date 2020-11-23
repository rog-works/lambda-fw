from framework.i18n.datetime import DateTime
from framework.i18n.tzinfo import TZInfo
from framework.i18n.translator import Translator


class Locale:
    def __init__(self, locale: str, trans_config: dict) -> None:
        self._datetime = DateTime(TZInfo(locale))
        self._translator = Translator(trans_config)

    def datetime(self) -> DateTime:
        return self._datetime

    def trans(self, path: str) -> str:
        return self._translator.trans(path)