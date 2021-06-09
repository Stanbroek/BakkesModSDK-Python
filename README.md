[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Stanbroek/BakkesModSDK-Python.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Stanbroek/BakkesModSDK-Python/context:python)

# BakkesModSDK - Python
This plugin adds python bindings to the bakkesmod sdk through [pybind11](https://github.com/pybind/pybind11).  
Inspired by [BakkesPython](https://github.com/Martinii89/BakkesPython) made by [@Martinii89](https://github.com/Martinii89).

## Generate bindings (*optional*):
- Make sure the `BAKKESMODSDK_DIR` value in [generate_sdk.py](/Scripts/generate_sdk.py) is set to the correct folder.
- Generate the bindings with for example `generate_sdk.py bakkesmodplugin.cpp -o out -pybind11-module`
- Fix all the errors, most of them should be detailed in [bindings.cpp](\PythonPlugin\bindings.cpp).

## Compile plugin:
- Make sure you have the python libs installed from [https://www.python.org/downloads/](https://www.python.org/downloads/).
- Compile the PythonPlugin with `PythonPlugin.sln`.

## Usage:
- Change the plugin directory by changing `pp_plugin_dir`, default is `${BakkesModFolder}/py`.
- Load plugins with `pplugin load ${plugin_name}`.

## Examples:
- see [Examples](/Examples)
