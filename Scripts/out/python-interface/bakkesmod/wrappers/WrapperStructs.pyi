from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

# ToastType [enumeration]
class ToastType(Enum):
    ToastType_Info = 0
    ToastType_OK = 1
    ToastType_Warning = 2
    ToastType_Error = 3

# FVector [class declaration]

# FRotator [class declaration]

class Vector():
    # Public:
    # Vector::X [variable]
    @property
    def X(self) -> float: ...

    # Vector::Y [variable]
    @property
    def Y(self) -> float: ...

    # Vector::Z [variable]
    @property
    def Z(self) -> float: ...

    # Vector::Vector(FVector v) [constructor]
    def __init__(self, v: FVector) -> None: ...

    # Vector::Vector(float x, float y, float z) [constructor]
    def __init__(self, x: float, y: float, z: float) -> None: ...

    # Vector::Vector(float def) [constructor]
    def __init__(self, def: float) -> None: ...

    # Vector::Vector() [constructor]
    def __init__(self) -> None: ...

    # FVector Vector::operator ::FVector() [casting operator]

    # Vector Vector::operator+=(Vector const v2) [member operator]
    def __iadd__(self, other: Vector) -> Vector: ...

    # Vector Vector::operator-=(Vector const v2) [member operator]
    def __isub__(self, other: Vector) -> Vector: ...

    # Vector Vector::operator*=(Vector const v2) [member operator]
    def __imul__(self, other: Vector) -> Vector: ...

    # Vector Vector::operator/=(Vector const v2) [member operator]
    def __itruediv__(self, other: Vector) -> Vector: ...

    # Vector Vector::operator+=(float const f) [member operator]
    def __iadd__(self, other: float) -> Vector: ...

    # Vector Vector::operator-=(float const f) [member operator]
    def __isub__(self, other: float) -> Vector: ...

    # Vector Vector::operator*=(float const f) [member operator]
    def __imul__(self, other: float) -> Vector: ...

    # Vector Vector::operator/=(float const f) [member operator]
    def __itruediv__(self, other: float) -> Vector: ...

    # float Vector::magnitude() const [member function]
    def magnitude(self) -> float: ...

    # void Vector::normalize() [member function]
    def normalize(self) -> None: ...

    # Vector Vector::getNormalized() [member function]
    def getNormalized(self) -> Vector: ...

    # Vector Vector::clone() const [member function]
    def clone(self) -> Vector: ...

    # static float Vector::dot(Vector const v1, Vector const v2) [member function]
    def dot(self, v1: Vector, v2: Vector) -> float: ...

    # static Vector Vector::cross(Vector const v1, Vector const v2) [member function]
    def cross(self, v1: Vector, v2: Vector) -> Vector: ...

    # static Vector Vector::lerp(Vector const v1, Vector const v2, float const t) [member function]
    def lerp(self, v1: Vector, v2: Vector, t: float) -> Vector: ...

    # static Vector Vector::slerp(Vector const v1, Vector const v2, float const t) [member function]
    def slerp(self, v1: Vector, v2: Vector, t: float) -> Vector: ...

    # Vector::Vector(Vector const & arg0) [constructor]

    # Vector::~Vector() [destructor]
    def __del__(self) -> None: ...

    # Vector & Vector::operator=(Vector const & arg0) [member operator]


# Vector operator+(Vector const v1, Vector const v2) [free operator]

# Vector operator-(Vector const v1, Vector const v2) [free operator]

# Vector operator*(Vector const v1, Vector const v2) [free operator]

# Vector operator/(Vector const v1, Vector const v2) [free operator]

# Vector operator+(Vector const v1, float const f) [free operator]

# Vector operator-(Vector const v1, float const f) [free operator]

# Vector operator*(Vector const v1, float const f) [free operator]

# Vector operator/(Vector const v1, float const f) [free operator]

class Rotator():
    # Public:
    # Rotator::Pitch [variable]
    @property
    def Pitch(self) -> int: ...

    # Rotator::Yaw [variable]
    @property
    def Yaw(self) -> int: ...

    # Rotator::Roll [variable]
    @property
    def Roll(self) -> int: ...

    # Rotator::Rotator(FRotator r) [constructor]
    def __init__(self, r: FRotator) -> None: ...

    # Rotator::Rotator(int pitch, int yaw, int roll) [constructor]
    def __init__(self, pitch: int, yaw: int, roll: int) -> None: ...

    # Rotator::Rotator(int def) [constructor]
    def __init__(self, def: int) -> None: ...

    # Rotator::Rotator() [constructor]
    def __init__(self) -> None: ...

    # FRotator Rotator::operator ::FRotator() [casting operator]

    # Rotator Rotator::operator+=(Rotator const r2) [member operator]
    def __iadd__(self, other: Rotator) -> Rotator: ...

    # Rotator Rotator::operator-=(Rotator const r2) [member operator]
    def __isub__(self, other: Rotator) -> Rotator: ...

    # Rotator Rotator::operator*=(Rotator const r2) [member operator]
    def __imul__(self, other: Rotator) -> Rotator: ...

    # Rotator Rotator::operator/=(Rotator const r2) [member operator]
    def __itruediv__(self, other: Rotator) -> Rotator: ...

    # Rotator::Rotator(Rotator const & arg0) [constructor]

    # Rotator::~Rotator() [destructor]
    def __del__(self) -> None: ...

    # Rotator & Rotator::operator=(Rotator const & arg0) [member operator]


# Rotator operator+(Rotator const r1, Rotator const r2) [free operator]

# Rotator operator-(Rotator const r1, Rotator const r2) [free operator]

# Rotator operator*(Rotator const r1, Rotator const r2) [free operator]

# Rotator operator/(Rotator const r1, Rotator const r2) [free operator]

# int fixRotator(int newRotation) [free function]
def fixRotator(self, newRotation: int) -> int: ...

# int fixPitch(int newRotation) [free function]
def fixPitch(self, newRotation: int) -> int: ...

# Rotator VectorToRotator(Vector const vVector) [free function]
def VectorToRotator(self, vVector: Vector) -> Rotator: ...

# Vector RotatorToVector(Rotator const R) [free function]
def RotatorToVector(self, R: Rotator) -> Vector: ...

class Quat():
    # Public:
    # Quat::X [variable]
    @property
    def X(self) -> float: ...

    # Quat::Y [variable]
    @property
    def Y(self) -> float: ...

    # Quat::Z [variable]
    @property
    def Z(self) -> float: ...

    # Quat::W [variable]
    @property
    def W(self) -> float: ...

    # Quat::Quat(float w, float x, float y, float z) [constructor]
    def __init__(self, w: float, x: float, y: float, z: float) -> None: ...

    # Quat::Quat() [constructor]
    def __init__(self) -> None: ...

    # Quat Quat::conjugate() const [member function]
    def conjugate(self) -> Quat: ...

    # Quat Quat::normalize() [member function]
    def normalize(self) -> Quat: ...

    # Quat Quat::operator*=(Quat const q2) [member operator]
    def __imul__(self, other: Quat) -> Quat: ...

    # Quat::Quat(Quat const & arg0) [constructor]

    # Quat::~Quat() [destructor]
    def __del__(self) -> None: ...

    # Quat & Quat::operator=(Quat const & arg0) [member operator]


# Quat operator*(Quat const q1, Quat const q2) [free operator]

# Quat QuatSlerp(Quat const q1, Quat const q2, float percent) [free function]
def QuatSlerp(self, q1: Quat, q2: Quat, percent: float) -> Quat: ...

# Vector RotateVectorWithQuat(Vector const v, Quat const q) [free function]
def RotateVectorWithQuat(self, v: Vector, q: Quat) -> Vector: ...

# Quat RotatorToQuat(Rotator const rot) [free function]
def RotatorToQuat(self, rot: Rotator) -> Quat: ...

# Rotator QuatToRotator(Quat const q) [free function]
def QuatToRotator(self, q: Quat) -> Rotator: ...

class Vector2():
    # Public:
    # Vector2::X [variable]
    @property
    def X(self) -> int: ...

    # Vector2::Y [variable]
    @property
    def Y(self) -> int: ...

    # Vector2 Vector2::minus(Vector2 const other) const [member function]
    def minus(self, other: Vector2) -> Vector2: ...

    # Vector2 Vector2::operator+=(Vector2 const v2) [member operator]
    def __iadd__(self, other: Vector2) -> Vector2: ...

    # Vector2 Vector2::operator-=(Vector2 const v2) [member operator]
    def __isub__(self, other: Vector2) -> Vector2: ...

    # Vector2 Vector2::operator*=(Vector2 const v2) [member operator]
    def __imul__(self, other: Vector2) -> Vector2: ...

    # Vector2 Vector2::operator/=(Vector2 const v2) [member operator]
    def __itruediv__(self, other: Vector2) -> Vector2: ...

    # Vector2 Vector2::operator+=(int const i) [member operator]
    def __iadd__(self, other: int) -> Vector2: ...

    # Vector2 Vector2::operator-=(int const i) [member operator]
    def __isub__(self, other: int) -> Vector2: ...

    # Vector2 Vector2::operator*=(int const i) [member operator]
    def __imul__(self, other: int) -> Vector2: ...

    # Vector2 Vector2::operator/=(int const i) [member operator]
    def __itruediv__(self, other: int) -> Vector2: ...

    # Vector2::Vector2() [constructor]
    def __init__(self) -> None: ...

    # Vector2::Vector2(Vector2 const & arg0) [constructor]

    # Vector2::~Vector2() [destructor]
    def __del__(self) -> None: ...

    # Vector2 & Vector2::operator=(Vector2 const & arg0) [member operator]


# Vector2 operator+(Vector2 const v1, Vector2 const v2) [free operator]

# Vector2 operator-(Vector2 const v1, Vector2 const v2) [free operator]

# Vector2 operator*(Vector2 const v1, Vector2 const v2) [free operator]

# Vector2 operator/(Vector2 const v1, Vector2 const v2) [free operator]

# Vector2 operator+(Vector2 const v1, int const i) [free operator]

# Vector2 operator-(Vector2 const v1, int const i) [free operator]

# Vector2 operator*(Vector2 const v1, int const i) [free operator]

# Vector2 operator/(Vector2 const v1, int const i) [free operator]

class Vector2F():
    # Public:
    # Vector2F::X [variable]
    @property
    def X(self) -> float: ...

    # Vector2F::Y [variable]
    @property
    def Y(self) -> float: ...

    # Vector2F Vector2F::minus(Vector2 const other) const [member function]
    def minus(self, other: Vector2) -> Vector2F: ...

    # Vector2F Vector2F::minus(Vector2F const other) const [member function]
    def minus(self, other: Vector2F) -> Vector2F: ...

    # Vector2F Vector2F::operator+=(Vector2 const v2) [member operator]
    def __iadd__(self, other: Vector2) -> Vector2F: ...

    # Vector2F Vector2F::operator-=(Vector2 const v2) [member operator]
    def __isub__(self, other: Vector2) -> Vector2F: ...

    # Vector2F Vector2F::operator*=(Vector2 const v2) [member operator]
    def __imul__(self, other: Vector2) -> Vector2F: ...

    # Vector2F Vector2F::operator/=(Vector2 const v2) [member operator]
    def __itruediv__(self, other: Vector2) -> Vector2F: ...

    # Vector2F Vector2F::operator+=(Vector2F const v2) [member operator]
    def __iadd__(self, other: Vector2F) -> Vector2F: ...

    # Vector2F Vector2F::operator-=(Vector2F const v2) [member operator]
    def __isub__(self, other: Vector2F) -> Vector2F: ...

    # Vector2F Vector2F::operator*=(Vector2F const v2) [member operator]
    def __imul__(self, other: Vector2F) -> Vector2F: ...

    # Vector2F Vector2F::operator/=(Vector2F const v2) [member operator]
    def __itruediv__(self, other: Vector2F) -> Vector2F: ...

    # Vector2F Vector2F::operator+=(float const f) [member operator]
    def __iadd__(self, other: float) -> Vector2F: ...

    # Vector2F Vector2F::operator-=(float const f) [member operator]
    def __isub__(self, other: float) -> Vector2F: ...

    # Vector2F Vector2F::operator*=(float const f) [member operator]
    def __imul__(self, other: float) -> Vector2F: ...

    # Vector2F Vector2F::operator/=(float const f) [member operator]
    def __itruediv__(self, other: float) -> Vector2F: ...

    # Vector2F::Vector2F() [constructor]
    def __init__(self) -> None: ...

    # Vector2F::Vector2F(Vector2F const & arg0) [constructor]

    # Vector2F::~Vector2F() [destructor]
    def __del__(self) -> None: ...

    # Vector2F & Vector2F::operator=(Vector2F const & arg0) [member operator]


# Vector2F operator+(Vector2F const v1, Vector2 const v2) [free operator]

# Vector2F operator-(Vector2F const v1, Vector2 const v2) [free operator]

# Vector2F operator*(Vector2F const v1, Vector2 const v2) [free operator]

# Vector2F operator/(Vector2F const v1, Vector2 const v2) [free operator]

# Vector2F operator+(Vector2F const v1, Vector2F const v2) [free operator]

# Vector2F operator-(Vector2F const v1, Vector2F const v2) [free operator]

# Vector2F operator*(Vector2F const v1, Vector2F const v2) [free operator]

# Vector2F operator/(Vector2F const v1, Vector2F const v2) [free operator]

# Vector2F operator+(Vector2F const v1, float const f) [free operator]

# Vector2F operator-(Vector2F const v1, float const f) [free operator]

# Vector2F operator*(Vector2F const v1, float const f) [free operator]

# Vector2F operator/(Vector2F const v1, float const f) [free operator]

class LinearColor():
    # Public:
    # LinearColor::R [variable]
    @property
    def R(self) -> float: ...

    # LinearColor::G [variable]
    @property
    def G(self) -> float: ...

    # LinearColor::B [variable]
    @property
    def B(self) -> float: ...

    # LinearColor::A [variable]
    @property
    def A(self) -> float: ...

    # LinearColor LinearColor::operator*=(float const f) [member operator]
    def __imul__(self, other: float) -> LinearColor: ...

    # LinearColor LinearColor::operator/=(float const f) [member operator]
    def __itruediv__(self, other: float) -> LinearColor: ...

    # LinearColor::LinearColor() [constructor]
    def __init__(self) -> None: ...

    # LinearColor::LinearColor(LinearColor const & arg0) [constructor]

    # LinearColor::~LinearColor() [destructor]
    def __del__(self) -> None: ...

    # LinearColor & LinearColor::operator=(LinearColor const & arg0) [member operator]


# LinearColor operator*(LinearColor const c1, float const f) [free operator]

# LinearColor operator/(LinearColor const c1, float const f) [free operator]

# bool operator==(LinearColor const c1, LinearColor const c2) [free operator]

# bool operator!=(LinearColor const c1, LinearColor const c2) [free operator]

class PredictionInfo():
    # Public:
    # PredictionInfo::Time [variable]
    @property
    def Time(self) -> float: ...

    # PredictionInfo::ArchTopTime [variable]
    @property
    def ArchTopTime(self) -> float: ...

    # PredictionInfo::Location [variable]
    @property
    def Location(self) -> Vector: ...

    # PredictionInfo::Velocity [variable]
    @property
    def Velocity(self) -> Vector: ...

    # PredictionInfo::ArchTop [variable]
    @property
    def ArchTop(self) -> Vector: ...

    # PredictionInfo::ArchTopVelocity [variable]
    @property
    def ArchTopVelocity(self) -> Vector: ...

    # PredictionInfo::bHitWall [variable]
    @property
    def bHitWall(self) -> bool: ...

    # PredictionInfo::bHitGround [variable]
    @property
    def bHitGround(self) -> bool: ...

    # PredictionInfo::PredictionInfo() [constructor]
    def __init__(self) -> None: ...

    # PredictionInfo::PredictionInfo(PredictionInfo const & arg0) [constructor]

    # PredictionInfo & PredictionInfo::operator=(PredictionInfo const & arg0) [member operator]

    # PredictionInfo::~PredictionInfo() [destructor]
    def __del__(self) -> None: ...


class SteamID():
    # Public:
    # SteamID::ID [variable]
    @property
    def ID(self) -> int: ...

    # SteamID::SteamID() [constructor]
    def __init__(self) -> None: ...

    # SteamID::SteamID(SteamID const & arg0) [constructor]

    # SteamID & SteamID::operator=(SteamID const & arg0) [member operator]

    # SteamID::~SteamID() [destructor]
    def __del__(self) -> None: ...


class SkillRating():
    # Public:
    # SkillRating::Mu [variable]
    @property
    def Mu(self) -> float: ...

    # SkillRating::Sigma [variable]
    @property
    def Sigma(self) -> float: ...

    # SkillRating::SkillRating() [constructor]
    def __init__(self) -> None: ...

    # SkillRating::SkillRating(SkillRating const & arg0) [constructor]

    # SkillRating & SkillRating::operator=(SkillRating const & arg0) [member operator]

    # SkillRating::~SkillRating() [destructor]
    def __del__(self) -> None: ...


class SkillRank():
    # Public:
    # SkillRank::Tier [variable]
    @property
    def Tier(self) -> int: ...

    # SkillRank::Division [variable]
    @property
    def Division(self) -> int: ...

    # SkillRank::MatchesPlayed [variable]
    @property
    def MatchesPlayed(self) -> int: ...

    # SkillRank::SkillRank() [constructor]
    def __init__(self) -> None: ...

    # SkillRank::SkillRank(SkillRank const & arg0) [constructor]

    # SkillRank & SkillRank::operator=(SkillRank const & arg0) [member operator]

    # SkillRank::~SkillRank() [destructor]
    def __del__(self) -> None: ...


class UnrealColor():
    # Public:
    # UnrealColor::B [variable]
    @property
    def B(self) -> int: ...

    # UnrealColor::G [variable]
    @property
    def G(self) -> int: ...

    # UnrealColor::R [variable]
    @property
    def R(self) -> int: ...

    # UnrealColor::A [variable]
    @property
    def A(self) -> int: ...

    # UnrealColor::UnrealColor() [constructor]
    def __init__(self) -> None: ...

    # UnrealColor::UnrealColor(UnrealColor const & arg0) [constructor]

    # UnrealColor & UnrealColor::operator=(UnrealColor const & arg0) [member operator]

    # UnrealColor::~UnrealColor() [destructor]
    def __del__(self) -> None: ...


class ControllerInput():
    # Public:
    # ControllerInput::Throttle [variable]
    @property
    def Throttle(self) -> float: ...

    # ControllerInput::Steer [variable]
    @property
    def Steer(self) -> float: ...

    # ControllerInput::Pitch [variable]
    @property
    def Pitch(self) -> float: ...

    # ControllerInput::Yaw [variable]
    @property
    def Yaw(self) -> float: ...

    # ControllerInput::Roll [variable]
    @property
    def Roll(self) -> float: ...

    # ControllerInput::DodgeForward [variable]
    @property
    def DodgeForward(self) -> float: ...

    # ControllerInput::DodgeStrafe [variable]
    @property
    def DodgeStrafe(self) -> float: ...

    # ControllerInput::Handbrake [variable]
    @property
    def Handbrake(self) -> bool: ...

    # ControllerInput::Jump [variable]
    @property
    def Jump(self) -> bool: ...

    # ControllerInput::ActivateBoost [variable]
    @property
    def ActivateBoost(self) -> bool: ...

    # ControllerInput::HoldingBoost [variable]
    @property
    def HoldingBoost(self) -> bool: ...

    # ControllerInput::Jumped [variable]
    @property
    def Jumped(self) -> bool: ...

    # ControllerInput::ControllerInput() [constructor]
    def __init__(self) -> None: ...

    # ControllerInput::ControllerInput(ControllerInput const & arg0) [constructor]

    # ControllerInput & ControllerInput::operator=(ControllerInput const & arg0) [member operator]

    # ControllerInput::~ControllerInput() [destructor]
    def __del__(self) -> None: ...


class RecordedSample():
    # Public:
    # RecordedSample::Low [variable]
    @property
    def Low(self) -> float: ...

    # RecordedSample::High [variable]
    @property
    def High(self) -> float: ...

    # RecordedSample::RecordedSample() [constructor]
    def __init__(self) -> None: ...

    # RecordedSample::RecordedSample(RecordedSample const & arg0) [constructor]

    # RecordedSample & RecordedSample::operator=(RecordedSample const & arg0) [member operator]

    # RecordedSample::~RecordedSample() [destructor]
    def __del__(self) -> None: ...


class POV():
    # Public:
    # POV::location [variable]
    @property
    def location(self) -> Vector: ...

    # POV::rotation [variable]
    @property
    def rotation(self) -> Rotator: ...

    # POV::FOV [variable]
    @property
    def FOV(self) -> float: ...

    # POV::POV() [constructor]
    def __init__(self) -> None: ...

    # POV::POV(POV const & arg0) [constructor]

    # POV & POV::operator=(POV const & arg0) [member operator]

    # POV::~POV() [destructor]
    def __del__(self) -> None: ...


class ViewTarget():
    # Public:
    # ViewTarget::Target [variable]
    @property
    def Target(self) -> Any: ...

    # ViewTarget::Controller [variable]
    @property
    def Controller(self) -> Any: ...

    # ViewTarget::POV [variable]
    @property
    def POV(self) -> POV: ...

    # ViewTarget::AspectRatio [variable]
    @property
    def AspectRatio(self) -> float: ...

    # ViewTarget::PRI [variable]
    @property
    def PRI(self) -> Any: ...

    # ViewTarget::ViewTarget() [constructor]
    def __init__(self) -> None: ...

    # ViewTarget::ViewTarget(ViewTarget const & arg0) [constructor]

    # ViewTarget & ViewTarget::operator=(ViewTarget const & arg0) [member operator]

    # ViewTarget::~ViewTarget() [destructor]
    def __del__(self) -> None: ...


class CameraSave():
    # Public:
    # CameraSave::InvertSwivelPitch [variable]
    @property
    def InvertSwivelPitch(self) -> bool: ...

    # CameraSave::CameraShake [variable]
    @property
    def CameraShake(self) -> bool: ...

    # CameraSave::CameraSave() [constructor]
    def __init__(self) -> None: ...

    # CameraSave::CameraSave(CameraSave const & arg0) [constructor]

    # CameraSave & CameraSave::operator=(CameraSave const & arg0) [member operator]

    # CameraSave::~CameraSave() [destructor]
    def __del__(self) -> None: ...


class ProfileCameraSettings():
    # Public:
    # ProfileCameraSettings::FOV [variable]
    @property
    def FOV(self) -> float: ...

    # ProfileCameraSettings::Height [variable]
    @property
    def Height(self) -> float: ...

    # ProfileCameraSettings::Pitch [variable]
    @property
    def Pitch(self) -> float: ...

    # ProfileCameraSettings::Distance [variable]
    @property
    def Distance(self) -> float: ...

    # ProfileCameraSettings::Stiffness [variable]
    @property
    def Stiffness(self) -> float: ...

    # ProfileCameraSettings::SwivelSpeed [variable]
    @property
    def SwivelSpeed(self) -> float: ...

    # ProfileCameraSettings::TransitionSpeed [variable]
    @property
    def TransitionSpeed(self) -> float: ...

    # ProfileCameraSettings::ProfileCameraSettings() [constructor]
    def __init__(self) -> None: ...

    # ProfileCameraSettings::ProfileCameraSettings(ProfileCameraSettings const & arg0) [constructor]

    # ProfileCameraSettings & ProfileCameraSettings::operator=(ProfileCameraSettings const & arg0) [member operator]

    # ProfileCameraSettings::~ProfileCameraSettings() [destructor]
    def __del__(self) -> None: ...


class GamepadSettings():
    # Public:
    # GamepadSettings::ControllerDeadzone [variable]
    @property
    def ControllerDeadzone(self) -> float: ...

    # GamepadSettings::DodgeInputThreshold [variable]
    @property
    def DodgeInputThreshold(self) -> float: ...

    # GamepadSettings::SteeringSensitivity [variable]
    @property
    def SteeringSensitivity(self) -> float: ...

    # GamepadSettings::AirControlSensitivity [variable]
    @property
    def AirControlSensitivity(self) -> float: ...

    # GamepadSettings::GamepadSettings() [constructor]
    def __init__(self) -> None: ...

    # GamepadSettings::GamepadSettings(GamepadSettings const & arg0) [constructor]

    # GamepadSettings & GamepadSettings::operator=(GamepadSettings const & arg0) [member operator]

    # GamepadSettings::~GamepadSettings() [destructor]
    def __del__(self) -> None: ...


class RBState():
    # Public:
    # RBState::Quaternion [variable]
    @property
    def Quaternion(self) -> Quat: ...

    # RBState::Location [variable]
    @property
    def Location(self) -> Vector: ...

    # RBState::LinearVelocity [variable]
    @property
    def LinearVelocity(self) -> Vector: ...

    # RBState::AngularVelocity [variable]
    @property
    def AngularVelocity(self) -> Vector: ...

    # RBState::Time [variable]
    @property
    def Time(self) -> float: ...

    # RBState::bSleeping [variable]
    @property
    def bSleeping(self) -> bool: ...

    # RBState::bNewData [variable]
    @property
    def bNewData(self) -> bool: ...

    # RBState::RBState() [constructor]
    def __init__(self) -> None: ...

    # RBState::RBState(RBState const & arg0) [constructor]

    # RBState & RBState::operator=(RBState const & arg0) [member operator]

    # RBState::~RBState() [destructor]
    def __del__(self) -> None: ...


class WorldContactData():
    # Public:
    # WorldContactData::bHasContact [variable]
    @property
    def bHasContact(self) -> bool: ...

    # WorldContactData::Location [variable]
    @property
    def Location(self) -> Vector: ...

    # WorldContactData::Velocity [variable]
    @property
    def Velocity(self) -> Vector: ...

    # WorldContactData::Normal [variable]
    @property
    def Normal(self) -> Vector: ...

    # WorldContactData::WorldContactData() [constructor]
    def __init__(self) -> None: ...

    # WorldContactData::WorldContactData(WorldContactData const & arg0) [constructor]

    # WorldContactData & WorldContactData::operator=(WorldContactData const & arg0) [member operator]

    # WorldContactData::~WorldContactData() [destructor]
    def __del__(self) -> None: ...


class StickyForceData():
    # Public:
    # StickyForceData::Ground [variable]
    @property
    def Ground(self) -> float: ...

    # StickyForceData::Wall [variable]
    @property
    def Wall(self) -> float: ...

    # StickyForceData::StickyForceData() [constructor]
    def __init__(self) -> None: ...

    # StickyForceData::StickyForceData(StickyForceData const & arg0) [constructor]

    # StickyForceData & StickyForceData::operator=(StickyForceData const & arg0) [member operator]

    # StickyForceData::~StickyForceData() [destructor]
    def __del__(self) -> None: ...


class WheelContactData():
    # Public:
    # WheelContactData::bHasContact [variable]
    @property
    def bHasContact(self) -> bool: ...

    # WheelContactData::bHasContactWithWorldGeometry [variable]
    @property
    def bHasContactWithWorldGeometry(self) -> bool: ...

    # WheelContactData::HasContactChangeTime [variable]
    @property
    def HasContactChangeTime(self) -> float: ...

    # WheelContactData::Actor [variable]
    @property
    def Actor(self) -> Any: ...

    # WheelContactData::Component [variable]
    @property
    def Component(self) -> Any: ...

    # WheelContactData::Location [variable]
    @property
    def Location(self) -> Vector: ...

    # WheelContactData::Normal [variable]
    @property
    def Normal(self) -> Vector: ...

    # WheelContactData::LatDirection [variable]
    @property
    def LatDirection(self) -> Vector: ...

    # WheelContactData::LongDirection [variable]
    @property
    def LongDirection(self) -> Vector: ...

    # WheelContactData::PhysMatProp [variable]
    @property
    def PhysMatProp(self) -> Any: ...

    # WheelContactData::WheelContactData() [constructor]
    def __init__(self) -> None: ...

    # WheelContactData::WheelContactData(WheelContactData const & arg0) [constructor]

    # WheelContactData & WheelContactData::operator=(WheelContactData const & arg0) [member operator]

    # WheelContactData::~WheelContactData() [destructor]
    def __del__(self) -> None: ...


class ReplayScoreData():
    # Public:
    # ReplayScoreData::ScoredBy [variable]
    @property
    def ScoredBy(self) -> int: ...

    # ReplayScoreData::AssistedBy [variable]
    @property
    def AssistedBy(self) -> int: ...

    # ReplayScoreData::Speed [variable]
    @property
    def Speed(self) -> float: ...

    # ReplayScoreData::Time [variable]
    @property
    def Time(self) -> float: ...

    # ReplayScoreData::ScoreTeam [variable]
    @property
    def ScoreTeam(self) -> int: ...

    # ReplayScoreData::ReplayScoreData() [constructor]
    def __init__(self) -> None: ...

    # ReplayScoreData::ReplayScoreData(ReplayScoreData const & arg0) [constructor]

    # ReplayScoreData & ReplayScoreData::operator=(ReplayScoreData const & arg0) [member operator]

    # ReplayScoreData::~ReplayScoreData() [destructor]
    def __del__(self) -> None: ...


class VideoSettings():
    # Public:
    # VideoSettings::bVsync [variable]
    @property
    def bVsync(self) -> bool: ...

    # VideoSettings::bShowWeatherFX [variable]
    @property
    def bShowWeatherFX(self) -> bool: ...

    # VideoSettings::bShowLightShafts [variable]
    @property
    def bShowLightShafts(self) -> bool: ...

    # VideoSettings::bTranslucentArenaShaders [variable]
    @property
    def bTranslucentArenaShaders(self) -> bool: ...

    # VideoSettings::bShowLensFlares [variable]
    @property
    def bShowLensFlares(self) -> bool: ...

    # VideoSettings::bEnableHDRSideBySideVisualizer [variable]
    @property
    def bEnableHDRSideBySideVisualizer(self) -> bool: ...

    # VideoSettings::bUncappedFramerate [variable]
    @property
    def bUncappedFramerate(self) -> bool: ...

    # VideoSettings::HDRBrightnessScale [variable]
    @property
    def HDRBrightnessScale(self) -> float: ...

    # VideoSettings::HDRPaperWhiteScale [variable]
    @property
    def HDRPaperWhiteScale(self) -> float: ...

    # VideoSettings::HDRGammaScale [variable]
    @property
    def HDRGammaScale(self) -> float: ...

    # VideoSettings::WindowMode [variable]
    @property
    def WindowMode(self) -> int: ...

    # VideoSettings::Resolution [variable]
    @property
    def Resolution(self) -> str: ...

    # VideoSettings::MaxFPS [variable]
    @property
    def MaxFPS(self) -> int: ...

    # VideoSettings::VideoOptions [variable]
    @property
    def VideoOptions(self) -> Dict[str, str]: ...

    # VideoSettings::VideoSettings(VideoSettings const & arg0) [constructor]

    # VideoSettings::~VideoSettings() [destructor]
    def __del__(self) -> None: ...

    # VideoSettings::VideoSettings() [constructor]
    def __init__(self) -> None: ...

    # VideoSettings & VideoSettings::operator=(VideoSettings const & arg0) [member operator]


# TRADEHOLD [enumeration]
class TRADEHOLD(Enum):
    TRADEHOLD_P2P = -2
    TRADEHOLD_ALL = -1
    TRADEHOLD_NONE = 0

# PRODUCTQUALITY [enumeration]
class PRODUCTQUALITY(Enum):
    Common = 0
    Uncommon = 1
    Rare = 2
    VeryRare = 3
    Import = 4
    Exotic = 5
    BlackMarket = 6
    Premium = 7
    Limited = 8
    MAX = 9

# UNLOCKMETHOD [enumeration]
class UNLOCKMETHOD(Enum):
    Default = 0
    Drop = 1
    Special = 2
    Reward = 3
    DLC = 4
    Never = 5
    MAX_ = 6

# CARBODY [enumeration]
class CARBODY(Enum):
    CAR_BACKFIRE = 21
    CAR_BREAKOUT = 22
    CAR_BREAKOUTTYPES = 1416
    CAR_OCTANE = 23
    CAR_OCTANEZSR = 1568
    CAR_PALADIN = 24
    CAR_ROADHOG = 25
    CAR_ROADHOGXL = 1300
    CAR_GIZMO = 26
    CAR_SWEETTOOTH = 27
    CAR_XDEVIL = 28
    CAR_XDEVILMK2 = 1159
    CAR_HOTSHOT = 29
    CAR_MERC = 30
    CAR_VENOM = 31
    CAR_TAKUMI = 402
    CAR_TAKUMIRXT = 1295
    CAR_DOMINUS = 403
    CAR_DOMINUSGT = 1018
    CAR_SCARAB = 404
    CAR_ZIPPY = 523
    CAR_DELOREAN = 597
    CAR_RIPPER = 600
    CAR_GROG = 607
    CAR_ARMADILLO = 625
    CAR_WARTHOG = 723
    CAR_BATMOBILE = 803
    CAR_MASAMUNE = 1171
    CAR_MARAUDER = 1172
    CAR_AFTERSHOCK = 1286
    CAR_ESPER = 1317
    CAR_PROTEUS = 1475
    CAR_TRITON = 1478
    CAR_VULCAN = 1533
    CAR_TWINMILL = 1603
    CAR_BONESHAKER = 1623
    CAR_ENDO = 1624
    CAR_ICECHARGER = 1675
    CAR_MANTIS = 1691
    CAR_JOGER619RS = 1856
    CAR_CENTIO = 1919
    CAR_ANIMUSGP = 1932

# OnlinePlatform [enumeration]
class OnlinePlatform(Enum):
    OnlinePlatform_Unknown = 0
    OnlinePlatform_Steam = 1
    OnlinePlatform_PS4 = 2
    OnlinePlatform_PS3 = 3
    OnlinePlatform_Dingo = 4
    OnlinePlatform_QQ = 5
    OnlinePlatform_OldNNX = 6
    OnlinePlatform_NNX = 7
    OnlinePlatform_PsyNet = 8
    OnlinePlatform_Deleted = 9
    OnlinePlatform_WeGame = 10
    OnlinePlatform_Epic = 11
    OnlinePlatform_MAX = 12

