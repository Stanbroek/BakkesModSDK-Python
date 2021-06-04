void bind_HttpWrapper(pybind11::module& m)
{

	pybind11::class_<HttpWrapper, std::shared_ptr<HttpWrapper>> cl_HttpWrapper(m, "HttpWrapper");
	cl_HttpWrapper.def_static("SendCurlRequest", [](CurlRequest request_data, CurlRequestDoneStringReturn on_complete) { return HttpWrapper::SendCurlRequest(request_data, on_complete); }, pybind11::arg("request_data"), pybind11::arg("on_complete"));
	cl_HttpWrapper.def_static("SendCurlRequest", [](CurlRequest request_data, CurlRequestDoneBinaryReturn on_complete) { return HttpWrapper::SendCurlRequest(request_data, on_complete); }, pybind11::arg("request_data"), pybind11::arg("on_complete"));
	cl_HttpWrapper.def_static("SendCurlRequest", [](CurlRequest request_data, std::wstring const & file_output, CurlRequestDoneFileReturn on_complete) { return HttpWrapper::SendCurlRequest(request_data, file_output, on_complete); }, pybind11::arg("request_data"), pybind11::arg("file_output"), pybind11::arg("on_complete"));
	cl_HttpWrapper.def_static("SendCurlJsonRequest", [](CurlRequest request_data, CurlRequestDoneStringReturn on_complete) { return HttpWrapper::SendCurlJsonRequest(request_data, on_complete); }, pybind11::arg("request_data"), pybind11::arg("on_complete"));
	cl_HttpWrapper.def(pybind11::init<>());
	cl_HttpWrapper.def(pybind11::init<HttpWrapper const &>(), pybind11::arg("arg0"));
	// cl_HttpWrapper.def(pybind11::del<>());
}
