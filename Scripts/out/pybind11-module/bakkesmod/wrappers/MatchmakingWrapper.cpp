void bind_MatchmakingWrapper(pybind11::module& m)
{

	pybind11::class_<MatchmakingWrapper, std::shared_ptr<MatchmakingWrapper>, ObjectWrapper> cl_MatchmakingWrapper(m, "MatchmakingWrapper");
	cl_MatchmakingWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_MatchmakingWrapper.def(pybind11::init<MatchmakingWrapper const &>(), pybind11::arg("other"));
	// cl_MatchmakingWrapper.def(pybind11::del<>());
	cl_MatchmakingWrapper.def("IsNull", [](MatchmakingWrapper& cls_) { return cls_.IsNull(); });
	cl_MatchmakingWrapper.def("IsSearching", [](MatchmakingWrapper& cls_) { return cls_.IsSearching(); });
	cl_MatchmakingWrapper.def("GetActiveViewTab", [](MatchmakingWrapper& cls_) { return cls_.GetActiveViewTab(); });
	cl_MatchmakingWrapper.def("SetRegionSelection", [](MatchmakingWrapper& cls_, Region region, bool bSelected) { return cls_.SetRegionSelection(region, bSelected); }, pybind11::arg("region"), pybind11::arg("bSelected"));
	cl_MatchmakingWrapper.def("SetPlaylistSelection", [](MatchmakingWrapper& cls_, Playlist playlist, bool bSelected) { return cls_.SetPlaylistSelection(playlist, bSelected); }, pybind11::arg("playlist"), pybind11::arg("bSelected"));
	cl_MatchmakingWrapper.def("StartMatchmaking", [](MatchmakingWrapper& cls_, PlaylistCategory playlist_category) { return cls_.StartMatchmaking(playlist_category); }, pybind11::arg("playlist_category"));
	cl_MatchmakingWrapper.def("CancelMatchmaking", [](MatchmakingWrapper& cls_) { return cls_.CancelMatchmaking(); });
	cl_MatchmakingWrapper.def("CreatePrivateMatch", [](MatchmakingWrapper& cls_, Region region, CustomMatchSettings const & match_settings) { return cls_.CreatePrivateMatch(region, match_settings); }, pybind11::arg("region"), pybind11::arg("match_settings"));
	cl_MatchmakingWrapper.def("JoinPrivateMatch", [](MatchmakingWrapper& cls_, std::string const & server_name, std::string const & server_password="") { return cls_.JoinPrivateMatch(server_name, server_password); }, pybind11::arg("server_name"), pybind11::arg("server_password"));
	cl_MatchmakingWrapper.def("SeasonEndDays", [](MatchmakingWrapper& cls_) { return cls_.SeasonEndDays(); });
	cl_MatchmakingWrapper.def("SeasonEndHours", [](MatchmakingWrapper& cls_) { return cls_.SeasonEndHours(); });
	cl_MatchmakingWrapper.def("SeasonEndMinutes", [](MatchmakingWrapper& cls_) { return cls_.SeasonEndMinutes(); });
	cl_MatchmakingWrapper.def("GetSeasonTimeRemaining", [](MatchmakingWrapper& cls_) { return cls_.GetSeasonTimeRemaining(); });
	cl_MatchmakingWrapper.def("GetSeasonEndTimeSeconds", [](MatchmakingWrapper& cls_) { return cls_.GetSeasonEndTimeSeconds(); });
	cl_MatchmakingWrapper.def("HasSeasonEnded", [](MatchmakingWrapper& cls_) { return cls_.HasSeasonEnded(); });
	cl_MatchmakingWrapper.def("GetTotalPopulation", [](MatchmakingWrapper& cls_) { return cls_.GetTotalPopulation(); });
	cl_MatchmakingWrapper.def_static("GetRegionID", [](Region region) { return MatchmakingWrapper::GetRegionID(region); }, pybind11::arg("region"));
	cl_MatchmakingWrapper.def_static("GetRegionLabel", [](Region region) { return MatchmakingWrapper::GetRegionLabel(region); }, pybind11::arg("region"));

	pybind11::enum_<Region> cl_Region(m, "Region");
	cl_Region.value("USE", Region::USE);
	cl_Region.value("EU", Region::EU);
	cl_Region.value("USW", Region::USW);
	cl_Region.value("ASC", Region::ASC);
	cl_Region.value("ASM", Region::ASM);
	cl_Region.value("JPN", Region::JPN);
	cl_Region.value("ME", Region::ME);
	cl_Region.value("OCE", Region::OCE);
	cl_Region.value("SAF", Region::SAF);
	cl_Region.value("SAM", Region::SAM);
	// cl_Region.export_values();

	pybind11::enum_<Playlist> cl_Playlist(m, "Playlist");
	cl_Playlist.value("CASUAL_STANDARD", Playlist::CASUAL_STANDARD);
	cl_Playlist.value("CASUAL_DOUBLES", Playlist::CASUAL_DOUBLES);
	cl_Playlist.value("CASUAL_DUELS", Playlist::CASUAL_DUELS);
	cl_Playlist.value("CASUAL_CHAOS", Playlist::CASUAL_CHAOS);
	cl_Playlist.value("RANKED_STANDARD", Playlist::RANKED_STANDARD);
	cl_Playlist.value("RANKED_DOUBLES", Playlist::RANKED_DOUBLES);
	cl_Playlist.value("RANKED_DUELS", Playlist::RANKED_DUELS);
	cl_Playlist.value("EXTRAS_RUMBLE", Playlist::EXTRAS_RUMBLE);
	cl_Playlist.value("EXTRAS_DROPSHOT", Playlist::EXTRAS_DROPSHOT);
	cl_Playlist.value("EXTRAS_HOOPS", Playlist::EXTRAS_HOOPS);
	cl_Playlist.value("EXTRAS_SNOWDAY", Playlist::EXTRAS_SNOWDAY);
	// cl_Playlist.export_values();

	pybind11::enum_<PlaylistCategory> cl_PlaylistCategory(m, "PlaylistCategory");
	cl_PlaylistCategory.value("CASUAL", PlaylistCategory::CASUAL);
	cl_PlaylistCategory.value("RANKED", PlaylistCategory::RANKED);
	cl_PlaylistCategory.value("EXTRAS", PlaylistCategory::EXTRAS);
	// cl_PlaylistCategory.export_values();

	pybind11::class_<ClubColorSet, std::shared_ptr<ClubColorSet>> cl_ClubColorSet(m, "ClubColorSet");
	cl_ClubColorSet.def_property("TeamColorID", [](const ClubColorSet& cls_) { return cls_.TeamColorID; }, [](ClubColorSet& cls_, unsigned char const& prop_) { cls_.TeamColorID = prop_; });
	cl_ClubColorSet.def_property("CustomColorID", [](const ClubColorSet& cls_) { return cls_.CustomColorID; }, [](ClubColorSet& cls_, unsigned char const& prop_) { cls_.CustomColorID = prop_; });
	cl_ClubColorSet.def_property("bTeamColorSet", [](const ClubColorSet& cls_) { return cls_.bTeamColorSet; }, [](ClubColorSet& cls_, bool const& prop_) { cls_.bTeamColorSet = prop_; });
	cl_ClubColorSet.def_property("bCustomColorSet", [](const ClubColorSet& cls_) { return cls_.bCustomColorSet; }, [](ClubColorSet& cls_, bool const& prop_) { cls_.bCustomColorSet = prop_; });
	cl_ClubColorSet.def(pybind11::init<ClubColorSet const &>(), pybind11::arg("arg0"));
	// cl_ClubColorSet.def(pybind11::del<>());
	cl_ClubColorSet.def(pybind11::init<>());

	pybind11::class_<CustomMatchTeamSettings, std::shared_ptr<CustomMatchTeamSettings>> cl_CustomMatchTeamSettings(m, "CustomMatchTeamSettings");
	cl_CustomMatchTeamSettings.def_property("Name", [](const CustomMatchTeamSettings& cls_) { return cls_.Name; }, [](CustomMatchTeamSettings& cls_, std::string const& prop_) { cls_.Name = prop_; });
	cl_CustomMatchTeamSettings.def_property("Colors", [](const CustomMatchTeamSettings& cls_) { return cls_.Colors; }, [](CustomMatchTeamSettings& cls_, ClubColorSet const& prop_) { cls_.Colors = prop_; });
	cl_CustomMatchTeamSettings.def_property("GameScore", [](const CustomMatchTeamSettings& cls_) { return cls_.GameScore; }, [](CustomMatchTeamSettings& cls_, int const& prop_) { cls_.GameScore = prop_; });
	cl_CustomMatchTeamSettings.def(pybind11::init<CustomMatchTeamSettings const &>(), pybind11::arg("arg0"));
	// cl_CustomMatchTeamSettings.def(pybind11::del<>());
	cl_CustomMatchTeamSettings.def(pybind11::init<>());

	pybind11::class_<CustomMatchSettings, std::shared_ptr<CustomMatchSettings>> cl_CustomMatchSettings(m, "CustomMatchSettings");
	cl_CustomMatchSettings.def_property("GameTags", [](const CustomMatchSettings& cls_) { return cls_.GameTags; }, [](CustomMatchSettings& cls_, std::string const& prop_) { cls_.GameTags = prop_; });
	cl_CustomMatchSettings.def_property("MapName", [](const CustomMatchSettings& cls_) { return cls_.MapName; }, [](CustomMatchSettings& cls_, std::string const& prop_) { cls_.MapName = prop_; });
	cl_CustomMatchSettings.def_property("ServerName", [](const CustomMatchSettings& cls_) { return cls_.ServerName; }, [](CustomMatchSettings& cls_, std::string const& prop_) { cls_.ServerName = prop_; });
	cl_CustomMatchSettings.def_property("Password", [](const CustomMatchSettings& cls_) { return cls_.Password; }, [](CustomMatchSettings& cls_, std::string const& prop_) { cls_.Password = prop_; });
	cl_CustomMatchSettings.def_property("BlueTeamSettings", [](const CustomMatchSettings& cls_) { return cls_.BlueTeamSettings; }, [](CustomMatchSettings& cls_, CustomMatchTeamSettings const& prop_) { cls_.BlueTeamSettings = prop_; });
	cl_CustomMatchSettings.def_property("OrangeTeamSettings", [](const CustomMatchSettings& cls_) { return cls_.OrangeTeamSettings; }, [](CustomMatchSettings& cls_, CustomMatchTeamSettings const& prop_) { cls_.OrangeTeamSettings = prop_; });
	cl_CustomMatchSettings.def_property("GameMode", [](const CustomMatchSettings& cls_) { return cls_.GameMode; }, [](CustomMatchSettings& cls_, int const& prop_) { cls_.GameMode = prop_; });
	cl_CustomMatchSettings.def_property("MaxPlayerCount", [](const CustomMatchSettings& cls_) { return cls_.MaxPlayerCount; }, [](CustomMatchSettings& cls_, int const& prop_) { cls_.MaxPlayerCount = prop_; });
	cl_CustomMatchSettings.def_property("bPartyMembersOnly", [](const CustomMatchSettings& cls_) { return cls_.bPartyMembersOnly; }, [](CustomMatchSettings& cls_, bool const& prop_) { cls_.bPartyMembersOnly = prop_; });
	cl_CustomMatchSettings.def_property("bClubServer", [](const CustomMatchSettings& cls_) { return cls_.bClubServer; }, [](CustomMatchSettings& cls_, bool const& prop_) { cls_.bClubServer = prop_; });
	cl_CustomMatchSettings.def(pybind11::init<CustomMatchSettings const &>(), pybind11::arg("arg0"));
	// cl_CustomMatchSettings.def(pybind11::del<>());
	cl_CustomMatchSettings.def(pybind11::init<>());
}
