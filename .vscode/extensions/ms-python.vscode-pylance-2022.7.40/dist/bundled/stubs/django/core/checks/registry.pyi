import sys
from typing import Any, Callable, List, Optional, Sequence, Set, TypeVar, Union

from django.apps.config import AppConfig
from django.core.checks.messages import CheckMessage

if sys.version_info < (3, 8):
    from typing_extensions import Protocol
else:
    from typing import Protocol

class Tags:
    admin: str = ...
    caches: str = ...
    compatibility: str = ...
    database: str = ...
    models: str = ...
    security: str = ...
    signals: str = ...
    sites: str = ...
    staticfiles: str = ...
    templates: str = ...
    translation: str = ...
    urls: str = ...

_CheckCallable = Callable[..., Sequence[CheckMessage]]
_C = TypeVar("_C", bound=_CheckCallable)

class _ProcessedCheckCallable(Protocol[_C]):
    tags: Sequence[str]
    __call__: _C

class CheckRegistry:
    registered_checks: Set[_ProcessedCheckCallable] = ...
    deployment_checks: Set[_ProcessedCheckCallable] = ...
    def __init__(self) -> None: ...
    def register(
        self, check: Optional[Union[_CheckCallable, str]] = ..., *tags: str, **kwargs: Any
    ) -> Union[Callable[[_CheckCallable], _ProcessedCheckCallable], _ProcessedCheckCallable]: ...
    def run_checks(
        self,
        app_configs: Optional[Sequence[AppConfig]] = ...,
        tags: Optional[Sequence[str]] = ...,
        include_deployment_checks: bool = ...,
        databases: Optional[Any] = ...,
    ) -> List[CheckMessage]: ...
    def tag_exists(self, tag: str, include_deployment_checks: bool = ...) -> bool: ...
    def tags_available(self, deployment_checks: bool = ...) -> Set[str]: ...
    def get_checks(self, include_deployment_checks: bool = ...) -> List[_ProcessedCheckCallable]: ...

registry: CheckRegistry = ...
register: Any = ...
run_checks: Any = ...
tag_exists: Any = ...