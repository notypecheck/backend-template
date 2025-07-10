import functools
from typing import TYPE_CHECKING

import dotenv
from pydantic_settings import BaseSettings


@functools.cache
def _load_dotenv_once() -> None:
    dotenv.load_dotenv()


def get_settings[TSettings: BaseSettings](cls: type[TSettings]) -> TSettings:
    _load_dotenv_once()
    return cls()


if not TYPE_CHECKING:  # pragma: no cover
    get_settings = functools.lru_cache(get_settings)
