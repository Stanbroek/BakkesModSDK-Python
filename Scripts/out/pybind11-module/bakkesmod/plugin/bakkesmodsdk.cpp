void bind_bakkesmodsdk(pybind11::module& m)
{
	m.attr("PLUGINTYPE_FREEPLAY") = pybind11::int_(static_cast<unsigned long>(PLUGINTYPE_FREEPLAY));
	m.attr("PLUGINTYPE_CUSTOM_TRAINING") = pybind11::int_(static_cast<unsigned long>(PLUGINTYPE_CUSTOM_TRAINING));
	m.attr("PLUGINTYPE_SPECTATOR") = pybind11::int_(static_cast<unsigned long>(PLUGINTYPE_SPECTATOR));
	m.attr("PLUGINTYPE_BOTAI") = pybind11::int_(static_cast<unsigned long>(PLUGINTYPE_BOTAI));
	m.attr("PLUGINTYPE_REPLAY") = pybind11::int_(static_cast<unsigned long>(PLUGINTYPE_REPLAY));
	m.attr("PLUGINTYPE_THREADED") = pybind11::int_(static_cast<unsigned long>(PLUGINTYPE_THREADED));
	m.attr("PLUGINTYPE_THREADEDUNLOAD") = pybind11::int_(static_cast<unsigned long>(PLUGINTYPE_THREADEDUNLOAD));
	m.attr("PERMISSION_ALL") = pybind11::int_(static_cast<unsigned long>(PERMISSION_ALL));
	m.attr("PERMISSION_MENU") = pybind11::int_(static_cast<unsigned long>(PERMISSION_MENU));
	m.attr("PERMISSION_SOCCAR") = pybind11::int_(static_cast<unsigned long>(PERMISSION_SOCCAR));
	m.attr("PERMISSION_FREEPLAY") = pybind11::int_(static_cast<unsigned long>(PERMISSION_FREEPLAY));
	m.attr("PERMISSION_CUSTOM_TRAINING") = pybind11::int_(static_cast<unsigned long>(PERMISSION_CUSTOM_TRAINING));
	m.attr("PERMISSION_ONLINE") = pybind11::int_(static_cast<unsigned long>(PERMISSION_ONLINE));
	m.attr("PERMISSION_PAUSEMENU_CLOSED") = pybind11::int_(static_cast<unsigned long>(PERMISSION_PAUSEMENU_CLOSED));
	m.attr("PERMISSION_REPLAY") = pybind11::int_(static_cast<unsigned long>(PERMISSION_REPLAY));
	m.attr("PERMISSION_OFFLINE") = pybind11::int_(static_cast<unsigned long>(PERMISSION_OFFLINE));
}
