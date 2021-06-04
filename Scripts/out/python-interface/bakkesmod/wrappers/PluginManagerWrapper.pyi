from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class PluginManagerWrapper():
    # Public:
    # PluginManagerWrapper::PluginManagerWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # PluginManagerWrapper::PluginManagerWrapper(PluginManagerWrapper const & other) [constructor]

    # PluginManagerWrapper & PluginManagerWrapper::operator=(PluginManagerWrapper rhs) [member operator]

    # PluginManagerWrapper::~PluginManagerWrapper() [destructor]
    def __del__(self) -> None: ...

    # std::vector<std::shared_ptr<BakkesMod::Plugin::LoadedPlugin>, std::allocator<std::shared_ptr<BakkesMod::Plugin::LoadedPlugin> > > * PluginManagerWrapper::GetLoadedPlugins() [member function]
    def GetLoadedPlugins(self) -> List[LoadedPlugin]: ...

    # Private:
    # PluginManagerWrapper::Impl [class declaration]

    # PluginManagerWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


