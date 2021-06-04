from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductAttribute_AnimatedSkinLabelWrapper():
    # Public:
    # ProductAttribute_AnimatedSkinLabelWrapper::ProductAttribute_AnimatedSkinLabelWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductAttribute_AnimatedSkinLabelWrapper::ProductAttribute_AnimatedSkinLabelWrapper(ProductAttribute_AnimatedSkinLabelWrapper const & other) [constructor]

    # ProductAttribute_AnimatedSkinLabelWrapper & ProductAttribute_AnimatedSkinLabelWrapper::operator=(ProductAttribute_AnimatedSkinLabelWrapper rhs) [member operator]

    # ProductAttribute_AnimatedSkinLabelWrapper::~ProductAttribute_AnimatedSkinLabelWrapper() [destructor]
    def __del__(self) -> None: ...

    # UnrealStringWrapper ProductAttribute_AnimatedSkinLabelWrapper::GetAnimatedLabel() [member function]
    def GetAnimatedLabel(self) -> UnrealStringWrapper: ...

    # Private:
    # ProductAttribute_AnimatedSkinLabelWrapper::Impl [class declaration]

    # ProductAttribute_AnimatedSkinLabelWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


