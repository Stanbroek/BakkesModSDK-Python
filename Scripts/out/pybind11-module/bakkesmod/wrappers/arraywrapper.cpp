void bind_arraywrapper(pybind11::module& m)
{

	pybind11::class_<ArrayWrapper<ActorWrapper>, std::shared_ptr<ArrayWrapper<ActorWrapper>>> cl_ArrayWrapper_ActorWrapper(m, "ArrayWrapper<ActorWrapper>");
	cl_ArrayWrapper_ActorWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_ActorWrapper.def(pybind11::init<ArrayWrapper<ActorWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_ActorWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_ActorWrapper.def("Count", [](ArrayWrapper<ActorWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_ActorWrapper.def("Get", [](ArrayWrapper<ActorWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_ActorWrapper.def("IsNull", [](ArrayWrapper<ActorWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<CarComponentWrapper>, std::shared_ptr<ArrayWrapper<CarComponentWrapper>>> cl_ArrayWrapper_CarComponentWrapper(m, "ArrayWrapper<CarComponentWrapper>");
	cl_ArrayWrapper_CarComponentWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_CarComponentWrapper.def(pybind11::init<ArrayWrapper<CarComponentWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_CarComponentWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_CarComponentWrapper.def("Count", [](ArrayWrapper<CarComponentWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_CarComponentWrapper.def("Get", [](ArrayWrapper<CarComponentWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_CarComponentWrapper.def("IsNull", [](ArrayWrapper<CarComponentWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<PriWrapper>, std::shared_ptr<ArrayWrapper<PriWrapper>>> cl_ArrayWrapper_PriWrapper(m, "ArrayWrapper<PriWrapper>");
	cl_ArrayWrapper_PriWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_PriWrapper.def(pybind11::init<ArrayWrapper<PriWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_PriWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_PriWrapper.def("Count", [](ArrayWrapper<PriWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_PriWrapper.def("Get", [](ArrayWrapper<PriWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_PriWrapper.def("IsNull", [](ArrayWrapper<PriWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<TeamWrapper>, std::shared_ptr<ArrayWrapper<TeamWrapper>>> cl_ArrayWrapper_TeamWrapper(m, "ArrayWrapper<TeamWrapper>");
	cl_ArrayWrapper_TeamWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_TeamWrapper.def(pybind11::init<ArrayWrapper<TeamWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_TeamWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_TeamWrapper.def("Count", [](ArrayWrapper<TeamWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_TeamWrapper.def("Get", [](ArrayWrapper<TeamWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_TeamWrapper.def("IsNull", [](ArrayWrapper<TeamWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<CarWrapper>, std::shared_ptr<ArrayWrapper<CarWrapper>>> cl_ArrayWrapper_CarWrapper(m, "ArrayWrapper<CarWrapper>");
	cl_ArrayWrapper_CarWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_CarWrapper.def(pybind11::init<ArrayWrapper<CarWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_CarWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_CarWrapper.def("Count", [](ArrayWrapper<CarWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_CarWrapper.def("Get", [](ArrayWrapper<CarWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_CarWrapper.def("IsNull", [](ArrayWrapper<CarWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<BallWrapper>, std::shared_ptr<ArrayWrapper<BallWrapper>>> cl_ArrayWrapper_BallWrapper(m, "ArrayWrapper<BallWrapper>");
	cl_ArrayWrapper_BallWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_BallWrapper.def(pybind11::init<ArrayWrapper<BallWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_BallWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_BallWrapper.def("Count", [](ArrayWrapper<BallWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_BallWrapper.def("Get", [](ArrayWrapper<BallWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_BallWrapper.def("IsNull", [](ArrayWrapper<BallWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<WheelWrapper>, std::shared_ptr<ArrayWrapper<WheelWrapper>>> cl_ArrayWrapper_WheelWrapper(m, "ArrayWrapper<WheelWrapper>");
	cl_ArrayWrapper_WheelWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_WheelWrapper.def(pybind11::init<ArrayWrapper<WheelWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_WheelWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_WheelWrapper.def("Count", [](ArrayWrapper<WheelWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_WheelWrapper.def("Get", [](ArrayWrapper<WheelWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_WheelWrapper.def("IsNull", [](ArrayWrapper<WheelWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<RBActorWrapper>, std::shared_ptr<ArrayWrapper<RBActorWrapper>>> cl_ArrayWrapper_RBActorWrapper(m, "ArrayWrapper<RBActorWrapper>");
	cl_ArrayWrapper_RBActorWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_RBActorWrapper.def(pybind11::init<ArrayWrapper<RBActorWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_RBActorWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_RBActorWrapper.def("Count", [](ArrayWrapper<RBActorWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_RBActorWrapper.def("Get", [](ArrayWrapper<RBActorWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_RBActorWrapper.def("IsNull", [](ArrayWrapper<RBActorWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<GoalWrapper>, std::shared_ptr<ArrayWrapper<GoalWrapper>>> cl_ArrayWrapper_GoalWrapper(m, "ArrayWrapper<GoalWrapper>");
	cl_ArrayWrapper_GoalWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_GoalWrapper.def(pybind11::init<ArrayWrapper<GoalWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_GoalWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_GoalWrapper.def("Count", [](ArrayWrapper<GoalWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_GoalWrapper.def("Get", [](ArrayWrapper<GoalWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_GoalWrapper.def("IsNull", [](ArrayWrapper<GoalWrapper>& cls_) { return cls_.IsNull(); });

	//pybind11::class_<ArrayWrapper<BoostPickupWrapper>, std::shared_ptr<ArrayWrapper<BoostPickupWrapper>>> cl_ArrayWrapper_BoostPickupWrapper(m, "ArrayWrapper<BoostPickupWrapper>");
	//cl_ArrayWrapper_BoostPickupWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	//cl_ArrayWrapper_BoostPickupWrapper.def(pybind11::init<ArrayWrapper<BoostPickupWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_BoostPickupWrapper.def(pybind11::del<>());
	//cl_ArrayWrapper_BoostPickupWrapper.def("Count", [](ArrayWrapper<BoostPickupWrapper>& cls_) { return cls_.Count(); });
	//cl_ArrayWrapper_BoostPickupWrapper.def("Get", [](ArrayWrapper<BoostPickupWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	//cl_ArrayWrapper_BoostPickupWrapper.def("IsNull", [](ArrayWrapper<BoostPickupWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<SampleHistoryWrapper>, std::shared_ptr<ArrayWrapper<SampleHistoryWrapper>>> cl_ArrayWrapper_SampleHistoryWrapper(m, "ArrayWrapper<SampleHistoryWrapper>");
	cl_ArrayWrapper_SampleHistoryWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_SampleHistoryWrapper.def(pybind11::init<ArrayWrapper<SampleHistoryWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_SampleHistoryWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_SampleHistoryWrapper.def("Count", [](ArrayWrapper<SampleHistoryWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_SampleHistoryWrapper.def("Get", [](ArrayWrapper<SampleHistoryWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_SampleHistoryWrapper.def("IsNull", [](ArrayWrapper<SampleHistoryWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<StatGraphWrapper>, std::shared_ptr<ArrayWrapper<StatGraphWrapper>>> cl_ArrayWrapper_StatGraphWrapper(m, "ArrayWrapper<StatGraphWrapper>");
	cl_ArrayWrapper_StatGraphWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_StatGraphWrapper.def(pybind11::init<ArrayWrapper<StatGraphWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_StatGraphWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_StatGraphWrapper.def("Count", [](ArrayWrapper<StatGraphWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_StatGraphWrapper.def("Get", [](ArrayWrapper<StatGraphWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_StatGraphWrapper.def("IsNull", [](ArrayWrapper<StatGraphWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<ControllerWrapper>, std::shared_ptr<ArrayWrapper<ControllerWrapper>>> cl_ArrayWrapper_ControllerWrapper(m, "ArrayWrapper<ControllerWrapper>");
	cl_ArrayWrapper_ControllerWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_ControllerWrapper.def(pybind11::init<ArrayWrapper<ControllerWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_ControllerWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_ControllerWrapper.def("Count", [](ArrayWrapper<ControllerWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_ControllerWrapper.def("Get", [](ArrayWrapper<ControllerWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_ControllerWrapper.def("IsNull", [](ArrayWrapper<ControllerWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<PlayerControllerWrapper>, std::shared_ptr<ArrayWrapper<PlayerControllerWrapper>>> cl_ArrayWrapper_PlayerControllerWrapper(m, "ArrayWrapper<PlayerControllerWrapper>");
	cl_ArrayWrapper_PlayerControllerWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_PlayerControllerWrapper.def(pybind11::init<ArrayWrapper<PlayerControllerWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_PlayerControllerWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_PlayerControllerWrapper.def("Count", [](ArrayWrapper<PlayerControllerWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_PlayerControllerWrapper.def("Get", [](ArrayWrapper<PlayerControllerWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_PlayerControllerWrapper.def("IsNull", [](ArrayWrapper<PlayerControllerWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<wchar_t>, std::shared_ptr<ArrayWrapper<wchar_t>>> cl_ArrayWrapper_wchar_t(m, "ArrayWrapper<wchar_t>");
	cl_ArrayWrapper_wchar_t.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_wchar_t.def(pybind11::init<ArrayWrapper<wchar_t> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_wchar_t.def(pybind11::del<>());
	cl_ArrayWrapper_wchar_t.def("Count", [](ArrayWrapper<wchar_t>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_wchar_t.def("Get", [](ArrayWrapper<wchar_t>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_wchar_t.def("IsNull", [](ArrayWrapper<wchar_t>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<SequenceWrapper>, std::shared_ptr<ArrayWrapper<SequenceWrapper>>> cl_ArrayWrapper_SequenceWrapper(m, "ArrayWrapper<SequenceWrapper>");
	cl_ArrayWrapper_SequenceWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_SequenceWrapper.def(pybind11::init<ArrayWrapper<SequenceWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_SequenceWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_SequenceWrapper.def("Count", [](ArrayWrapper<SequenceWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_SequenceWrapper.def("Get", [](ArrayWrapper<SequenceWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_SequenceWrapper.def("IsNull", [](ArrayWrapper<SequenceWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<SequenceObjectWrapper>, std::shared_ptr<ArrayWrapper<SequenceObjectWrapper>>> cl_ArrayWrapper_SequenceObjectWrapper(m, "ArrayWrapper<SequenceObjectWrapper>");
	cl_ArrayWrapper_SequenceObjectWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_SequenceObjectWrapper.def(pybind11::init<ArrayWrapper<SequenceObjectWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_SequenceObjectWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_SequenceObjectWrapper.def("Count", [](ArrayWrapper<SequenceObjectWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_SequenceObjectWrapper.def("Get", [](ArrayWrapper<SequenceObjectWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_SequenceObjectWrapper.def("IsNull", [](ArrayWrapper<SequenceObjectWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<SequenceVariableWrapper>, std::shared_ptr<ArrayWrapper<SequenceVariableWrapper>>> cl_ArrayWrapper_SequenceVariableWrapper(m, "ArrayWrapper<SequenceVariableWrapper>");
	cl_ArrayWrapper_SequenceVariableWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_SequenceVariableWrapper.def(pybind11::init<ArrayWrapper<SequenceVariableWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_SequenceVariableWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_SequenceVariableWrapper.def("Count", [](ArrayWrapper<SequenceVariableWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_SequenceVariableWrapper.def("Get", [](ArrayWrapper<SequenceVariableWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_SequenceVariableWrapper.def("IsNull", [](ArrayWrapper<SequenceVariableWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<ProductWrapper>, std::shared_ptr<ArrayWrapper<ProductWrapper>>> cl_ArrayWrapper_ProductWrapper(m, "ArrayWrapper<ProductWrapper>");
	cl_ArrayWrapper_ProductWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_ProductWrapper.def(pybind11::init<ArrayWrapper<ProductWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_ProductWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_ProductWrapper.def("Count", [](ArrayWrapper<ProductWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_ProductWrapper.def("Get", [](ArrayWrapper<ProductWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_ProductWrapper.def("IsNull", [](ArrayWrapper<ProductWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<OnlineProductWrapper>, std::shared_ptr<ArrayWrapper<OnlineProductWrapper>>> cl_ArrayWrapper_OnlineProductWrapper(m, "ArrayWrapper<OnlineProductWrapper>");
	cl_ArrayWrapper_OnlineProductWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_OnlineProductWrapper.def(pybind11::init<ArrayWrapper<OnlineProductWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_OnlineProductWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_OnlineProductWrapper.def("Count", [](ArrayWrapper<OnlineProductWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_OnlineProductWrapper.def("Get", [](ArrayWrapper<OnlineProductWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_OnlineProductWrapper.def("IsNull", [](ArrayWrapper<OnlineProductWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<ProductAttributeWrapper>, std::shared_ptr<ArrayWrapper<ProductAttributeWrapper>>> cl_ArrayWrapper_ProductAttributeWrapper(m, "ArrayWrapper<ProductAttributeWrapper>");
	cl_ArrayWrapper_ProductAttributeWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_ProductAttributeWrapper.def(pybind11::init<ArrayWrapper<ProductAttributeWrapper> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_ProductAttributeWrapper.def(pybind11::del<>());
	cl_ArrayWrapper_ProductAttributeWrapper.def("Count", [](ArrayWrapper<ProductAttributeWrapper>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_ProductAttributeWrapper.def("Get", [](ArrayWrapper<ProductAttributeWrapper>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_ProductAttributeWrapper.def("IsNull", [](ArrayWrapper<ProductAttributeWrapper>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<int>, std::shared_ptr<ArrayWrapper<int>>> cl_ArrayWrapper_int(m, "ArrayWrapper<int>");
	cl_ArrayWrapper_int.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_int.def(pybind11::init<ArrayWrapper<int> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_int.def(pybind11::del<>());
	cl_ArrayWrapper_int.def("Count", [](ArrayWrapper<int>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_int.def("Get", [](ArrayWrapper<int>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_int.def("IsNull", [](ArrayWrapper<int>& cls_) { return cls_.IsNull(); });

	pybind11::class_<ArrayWrapper<unsigned long long>, std::shared_ptr<ArrayWrapper<unsigned long long>>> cl_ArrayWrapper_unsigned_long_long(m, "ArrayWrapper<unsigned long long>");
	cl_ArrayWrapper_unsigned_long_long.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ArrayWrapper_unsigned_long_long.def(pybind11::init<ArrayWrapper<unsigned long long> const &>(), pybind11::arg("other"));
	// cl_ArrayWrapper_unsigned_long_long.def(pybind11::del<>());
	cl_ArrayWrapper_unsigned_long_long.def("Count", [](ArrayWrapper<unsigned long long>& cls_) { return cls_.Count(); });
	cl_ArrayWrapper_unsigned_long_long.def("Get", [](ArrayWrapper<unsigned long long>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
	cl_ArrayWrapper_unsigned_long_long.def("IsNull", [](ArrayWrapper<unsigned long long>& cls_) { return cls_.IsNull(); });
}
