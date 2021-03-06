from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

# GuiManagerWrapper [class declaration]

# BindingsWrapper [class declaration]

class GameWrapper():
    # Public:
    # GameWrapper::GameWrapper(uintptr_t mem, long int pluginType, std::type_index idx) [constructor]
    def __init__(self, mem: int, pluginType: int, idx: type_index) -> None: ...

    # GameWrapper::GameWrapper(GameWrapper const & other) [constructor]

    # GameWrapper & GameWrapper::operator=(GameWrapper rhs) [member operator]

    # GameWrapper::~GameWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool GameWrapper::IsInGame() [member function]
    def IsInGame(self) -> bool: ...

    # bool GameWrapper::IsInOnlineGame() [member function]
    def IsInOnlineGame(self) -> bool: ...

    # bool GameWrapper::IsInFreeplay() [member function]
    def IsInFreeplay(self) -> bool: ...

    # bool GameWrapper::IsInReplay() [member function]
    def IsInReplay(self) -> bool: ...

    # bool GameWrapper::IsInCustomTraining() [member function]
    def IsInCustomTraining(self) -> bool: ...

    # bool GameWrapper::IsSpectatingInOnlineGame() [member function]
    def IsSpectatingInOnlineGame(self) -> bool: ...

    # bool GameWrapper::IsPaused() [member function]
    def IsPaused(self) -> bool: ...

    # bool GameWrapper::IsUsingEpicVersion() [member function]
    def IsUsingEpicVersion(self) -> bool: ...

    # bool GameWrapper::IsUsingSteamVersion() [member function]
    def IsUsingSteamVersion(self) -> bool: ...

    # int GameWrapper::GetSteamVersion() [member function]
    def GetSteamVersion(self) -> int: ...

    # std::string GameWrapper::GetPsyBuildID() [member function]
    def GetPsyBuildID(self) -> str: ...

    # ServerWrapper GameWrapper::GetCurrentGameState() [member function]
    def GetCurrentGameState(self) -> ServerWrapper: ...

    # ServerWrapper GameWrapper::GetOnlineGame() [member function]
    def GetOnlineGame(self) -> ServerWrapper: ...

    # ServerWrapper GameWrapper::GetGameEventAsServer() [member function]
    def GetGameEventAsServer(self) -> ServerWrapper: ...

    # ReplayServerWrapper GameWrapper::GetGameEventAsReplay() [member function]
    def GetGameEventAsReplay(self) -> ReplayServerWrapper: ...

    # MMRWrapper GameWrapper::GetMMRWrapper() [member function]
    def GetMMRWrapper(self) -> MMRWrapper: ...

    # CarWrapper GameWrapper::GetLocalCar() [member function]
    def GetLocalCar(self) -> CarWrapper: ...

    # CameraWrapper GameWrapper::GetCamera() [member function]
    def GetCamera(self) -> CameraWrapper: ...

    # EngineTAWrapper GameWrapper::GetEngine() [member function]
    def GetEngine(self) -> EngineTAWrapper: ...

    # PluginManagerWrapper GameWrapper::GetPluginManager() [member function]
    def GetPluginManager(self) -> PluginManagerWrapper: ...

    # GuiManagerWrapper GameWrapper::GetGUIManager() [member function]
    def GetGUIManager(self) -> GuiManagerWrapper: ...

    # PlayerControllerWrapper GameWrapper::GetPlayerController() [member function]
    def GetPlayerController(self) -> PlayerControllerWrapper: ...

    # ItemsWrapper GameWrapper::GetItemsWrapper() [member function]
    def GetItemsWrapper(self) -> ItemsWrapper: ...

    # MatchmakingWrapper GameWrapper::GetMatchmakingWrapper() [member function]
    def GetMatchmakingWrapper(self) -> MatchmakingWrapper: ...

    # SettingsWrapper GameWrapper::GetSettings() [member function]
    def GetSettings(self) -> SettingsWrapper: ...

    # ModalWrapper GameWrapper::CreateModal(std::string const & title) [member function]
    def CreateModal(self, title: str) -> ModalWrapper: ...

    # TextInputModalWrapper GameWrapper::CreateTextInputModal(std::string const & title) [member function]
    def CreateTextInputModal(self, title: str) -> TextInputModalWrapper: ...

    # void GameWrapper::OverrideParams(void * src, size_t memsize) [member function]
    def OverrideParams(self, src: Any, memsize: int) -> None: ...

    # void GameWrapper::SetTimeout(std::function<void (GameWrapper *)> theLambda, float time) [member function]
    def SetTimeout(self, theLambda: Callable[[GameWrapper], None], time: float) -> None: ...

    # void GameWrapper::Execute(std::function<void (GameWrapper *)> theLambda) [member function]
    def Execute(self, theLambda: Callable[[GameWrapper], None]) -> None: ...

    # void GameWrapper::RegisterDrawable(std::function<void (CanvasWrapper)> callback) [member function]
    def RegisterDrawable(self, callback: Callable[[CanvasWrapper], None]) -> None: ...

    # void GameWrapper::UnregisterDrawables() [member function]
    def UnregisterDrawables(self) -> None: ...

    # std::string GameWrapper::GetFNameByIndex(int index) [member function]
    def GetFNameByIndex(self, index: int) -> str: ...

    # int GameWrapper::GetFNameIndexByString(std::string name) [member function]
    def GetFNameIndexByString(self, name: str) -> int: ...

    # void GameWrapper::HookEvent(std::string eventName, std::function<void (std::basic_string<char>)> callback) [member function]
    def HookEvent(self, eventName: str, callback: Callable[[str], None]) -> None: ...

    # void GameWrapper::UnhookEvent(std::string eventName) [member function]
    def UnhookEvent(self, eventName: str) -> None: ...

    # void GameWrapper::HookEventPost(std::string eventName, std::function<void (std::basic_string<char>)> callback) [member function]
    def HookEventPost(self, eventName: str, callback: Callable[[str], None]) -> None: ...

    # void GameWrapper::UnhookEventPost(std::string eventName) [member function]
    def UnhookEventPost(self, eventName: str) -> None: ...

    # void GameWrapper::LogToChatbox(std::string text, std::string sender="BAKKESMOD") [member function]
    def LogToChatbox(self, text: str, sender: str = "BAKKESMOD") -> None: ...

    # void GameWrapper::LoadToastTexture(std::string name, std::string path) [member function]
    def LoadToastTexture(self, name: str, path: str) -> None: ...

    # void GameWrapper::LoadToastTexture(std::string name, std::wstring path) [member function]
    def LoadToastTexture(self, name: str, path: str) -> None: ...

    # void GameWrapper::Toast(std::string title, std::string text, std::string texture="default", float timeout=3.5F, uint8_t toastType=0, float width=290.F, float height=60.F) [member function]
    def Toast(self, title: str, text: str, texture: str = "default", timeout: float = 3.5, toastType: uint8_t = 0, width: float = 290., height: float = 60.) -> None: ...

    # bool GameWrapper::IsKeyPressed(int keyName) [member function]
    def IsKeyPressed(self, keyName: int) -> bool: ...

    # int GameWrapper::IsCursorVisible() [member function]
    def IsCursorVisible(self) -> int: ...

    # void GameWrapper::ExecuteUnrealCommand(std::string command) [member function]
    def ExecuteUnrealCommand(self, command: str) -> None: ...

    # std::string GameWrapper::GetRandomMap() [member function]
    def GetRandomMap(self) -> str: ...

    # std::string GameWrapper::GetCurrentMap() [member function]
    def GetCurrentMap(self) -> str: ...

    # long long unsigned int GameWrapper::GetSteamID() [member function]
    def GetSteamID(self) -> int: ...

    # std::string GameWrapper::GetEpicID() [member function]
    def GetEpicID(self) -> str: ...

    # UniqueIDWrapper GameWrapper::GetUniqueID() [member function]
    def GetUniqueID(self) -> UniqueIDWrapper: ...

    # UnrealStringWrapper GameWrapper::GetPlayerName() [member function]
    def GetPlayerName(self) -> UnrealStringWrapper: ...

    # ClubDetailsWrapper GameWrapper::GetLocalClub() [member function]
    def GetLocalClub(self) -> ClubDetailsWrapper: ...

    # SequenceWrapper GameWrapper::GetMainSequence() [member function]
    def GetMainSequence(self) -> SequenceWrapper: ...

    # void GameWrapper::SetBotLoadout(PriWrapper & bot_pri, BotLoadoutData const & loadout_data) [member function]
    def SetBotLoadout(self, bot_pri: PriWrapper, loadout_data: BotLoadoutData) -> None: ...

    # Vector2 GameWrapper::GetScreenSize() [member function]
    def GetScreenSize(self) -> Vector2: ...

    # float GameWrapper::GetSafeZoneRatio() [member function]
    def GetSafeZoneRatio(self) -> float: ...

    # float GameWrapper::GetUIScale() [member function]
    def GetUIScale(self) -> float: ...

    # unsigned int GameWrapper::GetbMetric() [member function]
    def GetbMetric(self) -> int: ...

    # UnrealStringWrapper GameWrapper::GetUILanguage() [member function]
    def GetUILanguage(self) -> UnrealStringWrapper: ...

    # bool GameWrapper::GetbColorBlind() [member function]
    def GetbColorBlind(self) -> bool: ...

    # std::wstring GameWrapper::GetBakkesModPathW() [member function]
    def GetBakkesModPathW(self) -> str: ...

    # std::wstring GameWrapper::GetDataFolderW() [member function]
    def GetDataFolderW(self) -> str: ...

    # int GameWrapper::GetBakkesModVersion() [member function]
    def GetBakkesModVersion(self) -> int: ...

    # void GameWrapper::PlayReplay(std::wstring const & path) [member function]
    def PlayReplay(self, path: str) -> None: ...

    # void GameWrapper::HookEventWithCaller(std::string eventName, std::function<void (ServerWrapper, void *, std::basic_string<char>)> callback) [member function]
    def HookEventWithCaller(self, eventName: str, callback: Callable[[ServerWrapper, Any, str], None]) -> None: ...

    # void GameWrapper::HookEventWithCaller(std::string eventName, std::function<void (ActorWrapper, void *, std::basic_string<char>)> callback) [member function]
    def HookEventWithCaller(self, eventName: str, callback: Callable[[ActorWrapper, Any, str], None]) -> None: ...

    # void GameWrapper::HookEventWithCaller(std::string eventName, std::function<void (CarWrapper, void *, std::basic_string<char>)> callback) [member function]
    def HookEventWithCaller(self, eventName: str, callback: Callable[[CarWrapper, Any, str], None]) -> None: ...

    # void GameWrapper::HookEventWithCaller(std::string eventName, std::function<void (CarComponentWrapper, void *, std::basic_string<char>)> callback) [member function]
    def HookEventWithCaller(self, eventName: str, callback: Callable[[CarComponentWrapper, Any, str], None]) -> None: ...

    # void GameWrapper::HookEventWithCaller(std::string eventName, std::function<void (PlayerControllerWrapper, void *, std::basic_string<char>)> callback) [member function]
    def HookEventWithCaller(self, eventName: str, callback: Callable[[PlayerControllerWrapper, Any, str], None]) -> None: ...

    # void GameWrapper::HookEventWithCaller(std::string eventName, std::function<void (BallWrapper, void *, std::basic_string<char>)> callback) [member function]
    def HookEventWithCaller(self, eventName: str, callback: Callable[[BallWrapper, Any, str], None]) -> None: ...

    # void GameWrapper::HookEventWithCallerPost(std::string eventName, std::function<void (ActorWrapper, void *, std::basic_string<char>)> callback) [member function]
    def HookEventWithCallerPost(self, eventName: str, callback: Callable[[ActorWrapper, Any, str], None]) -> None: ...

    # void GameWrapper::HookEventWithCallerPost(std::string eventName, std::function<void (ServerWrapper, void *, std::basic_string<char>)> callback) [member function]
    def HookEventWithCallerPost(self, eventName: str, callback: Callable[[ServerWrapper, Any, str], None]) -> None: ...

    # void GameWrapper::HookEventWithCallerPost(std::string eventName, std::function<void (CarWrapper, void *, std::basic_string<char>)> callback) [member function]
    def HookEventWithCallerPost(self, eventName: str, callback: Callable[[CarWrapper, Any, str], None]) -> None: ...

    # void GameWrapper::HookEventWithCallerPost(std::string eventName, std::function<void (CarComponentWrapper, void *, std::basic_string<char>)> callback) [member function]
    def HookEventWithCallerPost(self, eventName: str, callback: Callable[[CarComponentWrapper, Any, str], None]) -> None: ...

    # void GameWrapper::HookEventWithCallerPost(std::string eventName, std::function<void (PlayerControllerWrapper, void *, std::basic_string<char>)> callback) [member function]
    def HookEventWithCallerPost(self, eventName: str, callback: Callable[[PlayerControllerWrapper, Any, str], None]) -> None: ...

    # void GameWrapper::HookEventWithCallerPost(std::string eventName, std::function<void (BallWrapper, void *, std::basic_string<char>)> callback) [member function]
    def HookEventWithCallerPost(self, eventName: str, callback: Callable[[BallWrapper, Any, str], None]) -> None: ...

    # GameWrapper::Impl [class declaration]

    # GameWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


