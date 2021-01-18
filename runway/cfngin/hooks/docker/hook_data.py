"""Docker hook_data object."""
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, overload

from docker import DockerClient

from ....util import MutableMap, cached_property

if TYPE_CHECKING:
    from ...context import Context
    from .data_models import DockerImage


class DockerHookData(MutableMap):
    """Docker hook_data object."""

    image: Optional["DockerImage"] = None

    @cached_property
    def client(self) -> DockerClient:  # pylint: disable=no-self-use
        """Docker client."""
        return DockerClient.from_env()

    @overload
    def update_context(self, context: Context = ...) -> DockerHookData:  # noqa
        ...

    @overload
    def update_context(self, context: None = ...) -> None:  # noqa
        ...

    def update_context(
        self, context: Optional[Context] = None
    ) -> Optional[DockerHookData]:
        """Update context object with new the current DockerHookData."""
        if not context:
            return None
        context.hook_data["docker"] = self
        return self

    @classmethod
    def from_cfngin_context(cls, context: Optional[Context] = None) -> DockerHookData:
        """Get existing object or create a new one."""
        if context and "docker" in context.hook_data:
            found = context.hook_data["docker"]
            if isinstance(found, cls):
                return found
        new_obj = cls()
        context.hook_data["docker"] = new_obj
        return new_obj
