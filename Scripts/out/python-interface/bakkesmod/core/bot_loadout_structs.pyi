from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class BotLoadoutData():
    # Public:
    class Attribute():
        # Public:
        # BotLoadoutData::Attribute::Type [enumeration]
        class Type(Enum):
            PAINT = 0
            ESPORTWHEEL = 1
            SPECIALEDITION = 2

        # BotLoadoutData::Attribute::type [variable]
        @property
        def type(self) -> Type: ...

        # BotLoadoutData::Attribute::value [variable]
        @property
        def value(self) -> int: ...

        # BotLoadoutData::Attribute::Attribute() [constructor]
        def __init__(self) -> None: ...

        # BotLoadoutData::Attribute::Attribute(BotLoadoutData::Attribute const & arg0) [constructor]

        # BotLoadoutData::Attribute & BotLoadoutData::Attribute::operator=(BotLoadoutData::Attribute const & arg0) [member operator]

        # BotLoadoutData::Attribute::~Attribute() [destructor]
        def __del__(self) -> None: ...


    # BotLoadoutData::products [variable]
    @property
    def products(self) -> Dict[int, int]: ...

    # BotLoadoutData::product_attributes [variable]
    @property
    def product_attributes(self) -> Dict[int, Attribute]: ...

    # BotLoadoutData::team [variable]
    @property
    def team(self) -> int: ...

    # BotLoadoutData::team_finish_id [variable]
    @property
    def team_finish_id(self) -> int: ...

    # BotLoadoutData::custom_finish_id [variable]
    @property
    def custom_finish_id(self) -> int: ...

    # BotLoadoutData::team_color_id [variable]
    @property
    def team_color_id(self) -> int: ...

    # BotLoadoutData::custom_color_id [variable]
    @property
    def custom_color_id(self) -> int: ...

    # BotLoadoutData::BotLoadoutData(BotLoadoutData const & arg0) [constructor]

    # BotLoadoutData::~BotLoadoutData() [destructor]
    def __del__(self) -> None: ...

    # BotLoadoutData::BotLoadoutData() [constructor]
    def __init__(self) -> None: ...

    # BotLoadoutData & BotLoadoutData::operator=(BotLoadoutData const & arg0) [member operator]


