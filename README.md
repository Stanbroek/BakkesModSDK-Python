# BakkesModSDK - Python
This plugin adds python bindings to the bakkesmod sdk through [pybind11](https://github.com/pybind/pybind11).  
Inspired by [BakkesPython](https://github.com/Martinii89/BakkesPython) made by [@Martinii89](https://github.com/Martinii89).

## Compile instructions:
- Clone the project with its submodues.
- Install the python libs from [https://www.python.org/downloads/](https://www.python.org/downloads/).
- Generate the bindings with `Scripts/generate_sdk.py`.
- Compile the PythonPlugin with `PythonPlugin.sln`.

## Usage:
- Change the plugin directory by changing `pp_plugin_dir`, default is `${BakkesModFolder}/py`.
- Load plugins with `pplugin load ${plugin_name}`.

## Examples:
- see [Examples](/Examples)
