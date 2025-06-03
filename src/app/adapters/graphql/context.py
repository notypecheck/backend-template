import dataclasses
import functools
from typing import TypeVar

import aioinject
from aioinject.ext.strawberry import inject as original_inject
from fastapi.requests import Request
from fastapi.responses import Response
from fastapi.websockets import WebSocket
from strawberry.types import Info as StrawberryInfo

from .dataloaders import Dataloaders

T = TypeVar("T")


@dataclasses.dataclass(slots=True, kw_only=True)
class Context:
    request: Request | WebSocket
    response: Response | WebSocket
    loaders: Dataloaders
    context: aioinject.Context | aioinject.SyncContext | None = None


Info = StrawberryInfo[Context, None]


def context_setter(
    ctx: Context, aioinject_context: aioinject.Context | aioinject.SyncContext
) -> None:
    ctx.context = aioinject_context


def context_getter(ctx: Context) -> aioinject.Context | aioinject.SyncContext:
    return ctx.context  # type: ignore[return-value]


inject = functools.partial(original_inject, context_getter=context_getter)
