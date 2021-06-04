// BakkesMod SDK
#include "bakkesmod/plugin/bakkesmodplugin.h"
// Include all the wrappers
#include "bakkesmod/wrappers/includes.h"

// and more
#include "bakkesmod/wrappers/Engine/WorldInfoWrapper.h"
#include "bakkesmod/wrappers/GameObject/RumbleComponent/BasketballPickup.h"
#include "bakkesmod/wrappers/GameObject/PerformanceStats/StartGraphSystemWrapper.h"
#include "bakkesmod/wrappers/GameObject/Stats/StatEventWrapper.h"
#include "bakkesmod/wrappers/kismet/SequenceVariableWrapper.h"
#include "bakkesmod/wrappers/kismet/SequenceWrapper.h"
//#include "bakkesmod/wrappers/GuiManagerWrapper.h"  // ImGui is not available in python bindings.
#include "bakkesmod/wrappers/PluginManagerWrapper.h"
//#include "bakkesmod/wrappers/replaywrapper.h"  // Redefinition of ReplayWrapper in 'bakkesmod/wrappers/GameEvent/ReplayWrapper.h'.
