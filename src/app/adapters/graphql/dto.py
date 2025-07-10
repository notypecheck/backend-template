import abc
from collections.abc import Iterable
from typing import Protocol, Self


class DTOMixinProtocol[Model, DTO](Protocol):
    @classmethod
    def from_orm_list(cls, models: Iterable[Model]) -> list[DTO]: ...


class DTOMixin[Model]:
    @classmethod
    @abc.abstractmethod
    def from_dto(cls, model: Model) -> Self:
        raise NotImplementedError

    @classmethod
    def from_dto_optional(
        cls,
        model: Model | None,
    ) -> Self | None:
        if model is None:
            return None
        return cls.from_dto(model)

    @classmethod
    def from_dto_list(cls, models: Iterable[Model]) -> list[Self]:
        return [cls.from_dto(model) for model in models]  # pragma: no cover
