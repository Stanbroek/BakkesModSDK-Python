from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class SettingsWrapper():
    # Public:
    # SettingsWrapper::SettingsWrapper() [constructor]
    def __init__(self) -> None: ...

    # SettingsWrapper::~SettingsWrapper() [destructor]
    def __del__(self) -> None: ...

    # ProfileCameraSettings SettingsWrapper::GetCameraSettings() [member function]
    def GetCameraSettings(self) -> ProfileCameraSettings: ...

    # CameraSave SettingsWrapper::GetCameraSaveSettings() [member function]
    def GetCameraSaveSettings(self) -> CameraSave: ...

    # std::map<std::basic_string<char>, std::basic_string<char>, std::less<std::basic_string<char> >, std::allocator<std::pair<const std::basic_string<char>, std::basic_string<char> > > > SettingsWrapper::GetPCBindings() [member function]
    def GetPCBindings(self) -> Dict[str, str]: ...

    # std::map<std::basic_string<char>, std::basic_string<char>, std::less<std::basic_string<char> >, std::allocator<std::pair<const std::basic_string<char>, std::basic_string<char> > > > SettingsWrapper::GetGamepadBindings() [member function]
    def GetGamepadBindings(self) -> Dict[str, str]: ...

    # std::vector<std::pair<std::basic_string<char>, std::basic_string<char> >, std::allocator<std::pair<std::basic_string<char>, std::basic_string<char> > > > SettingsWrapper::GetAllPCBindings() [member function]
    def GetAllPCBindings(self) -> List[Tuple[str, str]]: ...

    # std::vector<std::pair<std::basic_string<char>, std::basic_string<char> >, std::allocator<std::pair<std::basic_string<char>, std::basic_string<char> > > > SettingsWrapper::GetAllGamepadBindings() [member function]
    def GetAllGamepadBindings(self) -> List[Tuple[str, str]]: ...

    # GamepadSettings SettingsWrapper::GetGamepadSettings() [member function]
    def GetGamepadSettings(self) -> GamepadSettings: ...

    # VideoSettings SettingsWrapper::GetVideoSettings() [member function]
    def GetVideoSettings(self) -> VideoSettings: ...

    # SettingsWrapper::SettingsWrapper(SettingsWrapper const & arg0) [constructor]

    # SettingsWrapper & SettingsWrapper::operator=(SettingsWrapper const & arg0) [member operator]


