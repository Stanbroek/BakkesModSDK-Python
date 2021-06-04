from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ArrayWrapper_ActorWrapper():
    # Public:
    # ArrayWrapper<ActorWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<ActorWrapper>::ArrayWrapper(ArrayWrapper<ActorWrapper> const & other) [constructor]

    # ArrayWrapper<ActorWrapper> & ArrayWrapper<ActorWrapper>::operator=(ArrayWrapper<ActorWrapper> rhs) [member operator]

    # ArrayWrapper<ActorWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<ActorWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # ActorWrapper ArrayWrapper<ActorWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> ActorWrapper: ...

    # bool ArrayWrapper<ActorWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<ActorWrapper>::Impl [class declaration]

    # ArrayWrapper<ActorWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_CarComponentWrapper():
    # Public:
    # ArrayWrapper<CarComponentWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<CarComponentWrapper>::ArrayWrapper(ArrayWrapper<CarComponentWrapper> const & other) [constructor]

    # ArrayWrapper<CarComponentWrapper> & ArrayWrapper<CarComponentWrapper>::operator=(ArrayWrapper<CarComponentWrapper> rhs) [member operator]

    # ArrayWrapper<CarComponentWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<CarComponentWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # CarComponentWrapper ArrayWrapper<CarComponentWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> CarComponentWrapper: ...

    # bool ArrayWrapper<CarComponentWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<CarComponentWrapper>::Impl [class declaration]

    # ArrayWrapper<CarComponentWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_PriWrapper():
    # Public:
    # ArrayWrapper<PriWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<PriWrapper>::ArrayWrapper(ArrayWrapper<PriWrapper> const & other) [constructor]

    # ArrayWrapper<PriWrapper> & ArrayWrapper<PriWrapper>::operator=(ArrayWrapper<PriWrapper> rhs) [member operator]

    # ArrayWrapper<PriWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<PriWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # PriWrapper ArrayWrapper<PriWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> PriWrapper: ...

    # bool ArrayWrapper<PriWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<PriWrapper>::Impl [class declaration]

    # ArrayWrapper<PriWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_TeamWrapper():
    # Public:
    # ArrayWrapper<TeamWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<TeamWrapper>::ArrayWrapper(ArrayWrapper<TeamWrapper> const & other) [constructor]

    # ArrayWrapper<TeamWrapper> & ArrayWrapper<TeamWrapper>::operator=(ArrayWrapper<TeamWrapper> rhs) [member operator]

    # ArrayWrapper<TeamWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<TeamWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # TeamWrapper ArrayWrapper<TeamWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> TeamWrapper: ...

    # bool ArrayWrapper<TeamWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<TeamWrapper>::Impl [class declaration]

    # ArrayWrapper<TeamWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_CarWrapper():
    # Public:
    # ArrayWrapper<CarWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<CarWrapper>::ArrayWrapper(ArrayWrapper<CarWrapper> const & other) [constructor]

    # ArrayWrapper<CarWrapper> & ArrayWrapper<CarWrapper>::operator=(ArrayWrapper<CarWrapper> rhs) [member operator]

    # ArrayWrapper<CarWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<CarWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # CarWrapper ArrayWrapper<CarWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> CarWrapper: ...

    # bool ArrayWrapper<CarWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<CarWrapper>::Impl [class declaration]

    # ArrayWrapper<CarWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_BallWrapper():
    # Public:
    # ArrayWrapper<BallWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<BallWrapper>::ArrayWrapper(ArrayWrapper<BallWrapper> const & other) [constructor]

    # ArrayWrapper<BallWrapper> & ArrayWrapper<BallWrapper>::operator=(ArrayWrapper<BallWrapper> rhs) [member operator]

    # ArrayWrapper<BallWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<BallWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # BallWrapper ArrayWrapper<BallWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> BallWrapper: ...

    # bool ArrayWrapper<BallWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<BallWrapper>::Impl [class declaration]

    # ArrayWrapper<BallWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_WheelWrapper():
    # Public:
    # ArrayWrapper<WheelWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<WheelWrapper>::ArrayWrapper(ArrayWrapper<WheelWrapper> const & other) [constructor]

    # ArrayWrapper<WheelWrapper> & ArrayWrapper<WheelWrapper>::operator=(ArrayWrapper<WheelWrapper> rhs) [member operator]

    # ArrayWrapper<WheelWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<WheelWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # WheelWrapper ArrayWrapper<WheelWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> WheelWrapper: ...

    # bool ArrayWrapper<WheelWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<WheelWrapper>::Impl [class declaration]

    # ArrayWrapper<WheelWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_RBActorWrapper():
    # Public:
    # ArrayWrapper<RBActorWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<RBActorWrapper>::ArrayWrapper(ArrayWrapper<RBActorWrapper> const & other) [constructor]

    # ArrayWrapper<RBActorWrapper> & ArrayWrapper<RBActorWrapper>::operator=(ArrayWrapper<RBActorWrapper> rhs) [member operator]

    # ArrayWrapper<RBActorWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<RBActorWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # RBActorWrapper ArrayWrapper<RBActorWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> RBActorWrapper: ...

    # bool ArrayWrapper<RBActorWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<RBActorWrapper>::Impl [class declaration]

    # ArrayWrapper<RBActorWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_GoalWrapper():
    # Public:
    # ArrayWrapper<GoalWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<GoalWrapper>::ArrayWrapper(ArrayWrapper<GoalWrapper> const & other) [constructor]

    # ArrayWrapper<GoalWrapper> & ArrayWrapper<GoalWrapper>::operator=(ArrayWrapper<GoalWrapper> rhs) [member operator]

    # ArrayWrapper<GoalWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<GoalWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # GoalWrapper ArrayWrapper<GoalWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> GoalWrapper: ...

    # bool ArrayWrapper<GoalWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<GoalWrapper>::Impl [class declaration]

    # ArrayWrapper<GoalWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_BoostPickupWrapper():
    # Public:
    # ArrayWrapper<BoostPickupWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<BoostPickupWrapper>::ArrayWrapper(ArrayWrapper<BoostPickupWrapper> const & other) [constructor]

    # ArrayWrapper<BoostPickupWrapper> & ArrayWrapper<BoostPickupWrapper>::operator=(ArrayWrapper<BoostPickupWrapper> rhs) [member operator]

    # ArrayWrapper<BoostPickupWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<BoostPickupWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # BoostPickupWrapper ArrayWrapper<BoostPickupWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> BoostPickupWrapper: ...

    # bool ArrayWrapper<BoostPickupWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<BoostPickupWrapper>::Impl [class declaration]

    # ArrayWrapper<BoostPickupWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_SampleHistoryWrapper():
    # Public:
    # ArrayWrapper<SampleHistoryWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<SampleHistoryWrapper>::ArrayWrapper(ArrayWrapper<SampleHistoryWrapper> const & other) [constructor]

    # ArrayWrapper<SampleHistoryWrapper> & ArrayWrapper<SampleHistoryWrapper>::operator=(ArrayWrapper<SampleHistoryWrapper> rhs) [member operator]

    # ArrayWrapper<SampleHistoryWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<SampleHistoryWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # SampleHistoryWrapper ArrayWrapper<SampleHistoryWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> SampleHistoryWrapper: ...

    # bool ArrayWrapper<SampleHistoryWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<SampleHistoryWrapper>::Impl [class declaration]

    # ArrayWrapper<SampleHistoryWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_StatGraphWrapper():
    # Public:
    # ArrayWrapper<StatGraphWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<StatGraphWrapper>::ArrayWrapper(ArrayWrapper<StatGraphWrapper> const & other) [constructor]

    # ArrayWrapper<StatGraphWrapper> & ArrayWrapper<StatGraphWrapper>::operator=(ArrayWrapper<StatGraphWrapper> rhs) [member operator]

    # ArrayWrapper<StatGraphWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<StatGraphWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # StatGraphWrapper ArrayWrapper<StatGraphWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> StatGraphWrapper: ...

    # bool ArrayWrapper<StatGraphWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<StatGraphWrapper>::Impl [class declaration]

    # ArrayWrapper<StatGraphWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_ControllerWrapper():
    # Public:
    # ArrayWrapper<ControllerWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<ControllerWrapper>::ArrayWrapper(ArrayWrapper<ControllerWrapper> const & other) [constructor]

    # ArrayWrapper<ControllerWrapper> & ArrayWrapper<ControllerWrapper>::operator=(ArrayWrapper<ControllerWrapper> rhs) [member operator]

    # ArrayWrapper<ControllerWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<ControllerWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # ControllerWrapper ArrayWrapper<ControllerWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> ControllerWrapper: ...

    # bool ArrayWrapper<ControllerWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<ControllerWrapper>::Impl [class declaration]

    # ArrayWrapper<ControllerWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_PlayerControllerWrapper():
    # Public:
    # ArrayWrapper<PlayerControllerWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<PlayerControllerWrapper>::ArrayWrapper(ArrayWrapper<PlayerControllerWrapper> const & other) [constructor]

    # ArrayWrapper<PlayerControllerWrapper> & ArrayWrapper<PlayerControllerWrapper>::operator=(ArrayWrapper<PlayerControllerWrapper> rhs) [member operator]

    # ArrayWrapper<PlayerControllerWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<PlayerControllerWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # PlayerControllerWrapper ArrayWrapper<PlayerControllerWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> PlayerControllerWrapper: ...

    # bool ArrayWrapper<PlayerControllerWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<PlayerControllerWrapper>::Impl [class declaration]

    # ArrayWrapper<PlayerControllerWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_wchar_t():
    # Public:
    # ArrayWrapper<wchar_t>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<wchar_t>::ArrayWrapper(ArrayWrapper<wchar_t> const & other) [constructor]

    # ArrayWrapper<wchar_t> & ArrayWrapper<wchar_t>::operator=(ArrayWrapper<wchar_t> rhs) [member operator]

    # ArrayWrapper<wchar_t>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<wchar_t>::Count() [member function]
    def Count(self) -> int: ...

    # wchar_t ArrayWrapper<wchar_t>::Get(int index) [member function]
    def Get(self, index: int) -> str: ...

    # bool ArrayWrapper<wchar_t>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<wchar_t>::Impl [class declaration]

    # ArrayWrapper<wchar_t>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_SequenceWrapper():
    # Public:
    # ArrayWrapper<SequenceWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<SequenceWrapper>::ArrayWrapper(ArrayWrapper<SequenceWrapper> const & other) [constructor]

    # ArrayWrapper<SequenceWrapper> & ArrayWrapper<SequenceWrapper>::operator=(ArrayWrapper<SequenceWrapper> rhs) [member operator]

    # ArrayWrapper<SequenceWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<SequenceWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # SequenceWrapper ArrayWrapper<SequenceWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> SequenceWrapper: ...

    # bool ArrayWrapper<SequenceWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<SequenceWrapper>::Impl [class declaration]

    # ArrayWrapper<SequenceWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_SequenceObjectWrapper():
    # Public:
    # ArrayWrapper<SequenceObjectWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<SequenceObjectWrapper>::ArrayWrapper(ArrayWrapper<SequenceObjectWrapper> const & other) [constructor]

    # ArrayWrapper<SequenceObjectWrapper> & ArrayWrapper<SequenceObjectWrapper>::operator=(ArrayWrapper<SequenceObjectWrapper> rhs) [member operator]

    # ArrayWrapper<SequenceObjectWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<SequenceObjectWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # SequenceObjectWrapper ArrayWrapper<SequenceObjectWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> SequenceObjectWrapper: ...

    # bool ArrayWrapper<SequenceObjectWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<SequenceObjectWrapper>::Impl [class declaration]

    # ArrayWrapper<SequenceObjectWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_SequenceVariableWrapper():
    # Public:
    # ArrayWrapper<SequenceVariableWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<SequenceVariableWrapper>::ArrayWrapper(ArrayWrapper<SequenceVariableWrapper> const & other) [constructor]

    # ArrayWrapper<SequenceVariableWrapper> & ArrayWrapper<SequenceVariableWrapper>::operator=(ArrayWrapper<SequenceVariableWrapper> rhs) [member operator]

    # ArrayWrapper<SequenceVariableWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<SequenceVariableWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # SequenceVariableWrapper ArrayWrapper<SequenceVariableWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> SequenceVariableWrapper: ...

    # bool ArrayWrapper<SequenceVariableWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<SequenceVariableWrapper>::Impl [class declaration]

    # ArrayWrapper<SequenceVariableWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_ProductWrapper():
    # Public:
    # ArrayWrapper<ProductWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<ProductWrapper>::ArrayWrapper(ArrayWrapper<ProductWrapper> const & other) [constructor]

    # ArrayWrapper<ProductWrapper> & ArrayWrapper<ProductWrapper>::operator=(ArrayWrapper<ProductWrapper> rhs) [member operator]

    # ArrayWrapper<ProductWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<ProductWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # ProductWrapper ArrayWrapper<ProductWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> ProductWrapper: ...

    # bool ArrayWrapper<ProductWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<ProductWrapper>::Impl [class declaration]

    # ArrayWrapper<ProductWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_OnlineProductWrapper():
    # Public:
    # ArrayWrapper<OnlineProductWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<OnlineProductWrapper>::ArrayWrapper(ArrayWrapper<OnlineProductWrapper> const & other) [constructor]

    # ArrayWrapper<OnlineProductWrapper> & ArrayWrapper<OnlineProductWrapper>::operator=(ArrayWrapper<OnlineProductWrapper> rhs) [member operator]

    # ArrayWrapper<OnlineProductWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<OnlineProductWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # OnlineProductWrapper ArrayWrapper<OnlineProductWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> OnlineProductWrapper: ...

    # bool ArrayWrapper<OnlineProductWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<OnlineProductWrapper>::Impl [class declaration]

    # ArrayWrapper<OnlineProductWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_ProductAttributeWrapper():
    # Public:
    # ArrayWrapper<ProductAttributeWrapper>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<ProductAttributeWrapper>::ArrayWrapper(ArrayWrapper<ProductAttributeWrapper> const & other) [constructor]

    # ArrayWrapper<ProductAttributeWrapper> & ArrayWrapper<ProductAttributeWrapper>::operator=(ArrayWrapper<ProductAttributeWrapper> rhs) [member operator]

    # ArrayWrapper<ProductAttributeWrapper>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<ProductAttributeWrapper>::Count() [member function]
    def Count(self) -> int: ...

    # ProductAttributeWrapper ArrayWrapper<ProductAttributeWrapper>::Get(int index) [member function]
    def Get(self, index: int) -> ProductAttributeWrapper: ...

    # bool ArrayWrapper<ProductAttributeWrapper>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<ProductAttributeWrapper>::Impl [class declaration]

    # ArrayWrapper<ProductAttributeWrapper>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_int():
    # Public:
    # ArrayWrapper<int>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<int>::ArrayWrapper(ArrayWrapper<int> const & other) [constructor]

    # ArrayWrapper<int> & ArrayWrapper<int>::operator=(ArrayWrapper<int> rhs) [member operator]

    # ArrayWrapper<int>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<int>::Count() [member function]
    def Count(self) -> int: ...

    # int ArrayWrapper<int>::Get(int index) [member function]
    def Get(self, index: int) -> int: ...

    # bool ArrayWrapper<int>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<int>::Impl [class declaration]

    # ArrayWrapper<int>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ArrayWrapper_unsigned_long_long():
    # Public:
    # ArrayWrapper<unsigned long long>::ArrayWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ArrayWrapper<unsigned long long>::ArrayWrapper(ArrayWrapper<unsigned long long> const & other) [constructor]

    # ArrayWrapper<unsigned long long> & ArrayWrapper<unsigned long long>::operator=(ArrayWrapper<unsigned long long> rhs) [member operator]

    # ArrayWrapper<unsigned long long>::~ArrayWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ArrayWrapper<unsigned long long>::Count() [member function]
    def Count(self) -> int: ...

    # long long unsigned int ArrayWrapper<unsigned long long>::Get(int index) [member function]
    def Get(self, index: int) -> int: ...

    # bool ArrayWrapper<unsigned long long>::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # Protected:
    # ArrayWrapper<unsigned long long>::Impl [class declaration]

    # ArrayWrapper<unsigned long long>::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


