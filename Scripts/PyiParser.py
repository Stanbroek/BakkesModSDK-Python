import os
import re
import shutil
import warnings
from pygccxml import declarations
from typing import Dict, IO, List, Set, Type, TypeVar

from ParserHelper import ParserHelper

T = TypeVar('T', bound='SdkParser')


class PyiParser(ParserHelper):
    """
    Parses pygccxml declarations into a python interface.

    TODO's:
        - Oder dependencies.
        - Add __init__.py in `bakkesmod` folders.
        - Fix ClubMember::paddingForReasons in `ClubDetailsWrapper.py`.
        - Edit reserved keywords in `WrapperStructs.py`.
    """
    type_tranlation_table: Dict[str, str] = {
        'bool': 'bool',
        'char': 'int',
        'char unsigned': 'int',
        'unsigned char': 'int',
        'short': 'int',
        'short unsigned': 'int',
        'unsigned short': 'int',
        'int': 'int',
        'int unsigned': 'int',
        'unsigned int': 'int',
        'long': 'int',
        'long unsigned': 'int',
        'unsigned long': 'int',
        'long long': 'int',
        'long long unsigned': 'int',
        'unsigned long long': 'int',
        'long int': 'int',
        'long unsigned int': 'bool',  # Looks like its bit fields.
        'long long unsigned int': 'int',
        'size_t': 'int',
        'float': 'float',
        'double': 'float',
        'void': 'None',
        'char *': 'str',
        'unsigned char *': 'str',
        'string': 'str',
        'std::string': 'str',
        'wchar_t': 'str',
        'wchar_t *': 'str',
        'wstring': 'str',
        'std::wstring': 'str',
        'uintptr_t': 'int',
        'void *': 'Any'
    }

    value_tranlation_table: Dict[str, str] = {
        'true': 'True',
        'false': 'False',
        'nullptr': 'None'
    }

    custom_types: List[str] = [
        'Impl'
    ]

    def __init__(self: Type[T], sdk_dir: str) -> None:
        """Initialises member variables."""
        warnings.warn("Does not generate usable Python interface, use pybind11_stubgen instead.")

        self.sdk_dir = sdk_dir
        self.typedefs = dict()
        self.definitions: Dict[str, Set[str]] = dict()
        self.dependencies: Dict[str, Set[str]] = dict()
        self.unimplemented_declarations: Set[str] = set()

        self.current_location = ''

    def get_python_function_type_name(self: Type[T], decl_str: str) -> str:
        """
        Gets python typing type for function.

        Args:
            decl_str: String representation of the cpp function, expected to look like `std::function<foo(bar, bar)>`.

        Returns:
            Python typing type for function.
        """
        ret = decl_str[decl_str.find('<') + 1:decl_str.find('(')].strip()
        # BUG, recursive stuff breaks.
        params = decl_str[decl_str.find('(') + 1: decl_str.rfind(')')].split(',')
        return f"Callable[[{', '.join([self.get_python_type_name(param.strip()) for param in params])}], {self.get_python_type_name(ret)}]"

    def get_python_templated_type_name(self: Type[T], decl_str: str) -> str:
        """
        Gets python typing type for templated type.

        Args:
            decl_str: String representation of a templated type, expected to look like `foo<bar, bar>`.

        Returns:
            Python typing type for templated type.
        """
        # HACK, recursive stuff breaks atm.
        if decl_str == "std::vector<std::pair<std::basic_string<char>, std::basic_string<char> >, std::allocator<std::pair<std::basic_string<char>, std::basic_string<char> > > >":
            return "List[Tuple[str, str]]"
        if decl_str == "std::function<void (std::vector<std::basic_string<char>, std::allocator<std::basic_string<char> > >)>":
            return "Callable[[List[str]], None]"
        if decl_str == "void (*)( ::std::vector<std::basic_string<char>, std::allocator<std::basic_string<char> > > )":
            return "Callable[[List[str]], None]"
        template = decl_str[:decl_str.find('<')].strip()
        # BUG, recursive stuff breaks.
        types = decl_str[decl_str.find('<') + 1: decl_str.rfind('>')].split(',')
        if template == "std::function":
            return self.get_python_function_type_name(decl_str)
        elif template == "std::unique_ptr":
            return self.get_python_type_name(types[0].strip())
        elif template == "std::shared_ptr":
            return self.get_python_type_name(types[0].strip())
        elif template == "std::vector":
            return f"List[{self.get_python_type_name(types[0].strip())}]"
        elif template == "std::pair":
            return f"Tuple[{self.get_python_type_name(types[0].strip())}, {self.get_python_type_name(types[1].strip())}]"
        elif template == "std::map":
            return f"Dict[{self.get_python_type_name(types[0].strip())}, {self.get_python_type_name(types[1].strip())}]"
        elif template == "std::basic_string":
            return "str"
        elif template == "ArrayWrapper":
            return decl_str.replace('<', '_').replace('>', '').replace(' ', '_')
        elif template == "StructArrayWrapper":
            return decl_str.replace('<', '_').replace('>', '').replace(' ', '_')
        else:
            raise RuntimeError(f"Could not parse {repr(decl_str)}")

    def get_python_type_name(self: Type[T], decl: declarations.cpptypes.type_t) -> str:
        """
        Gets python name of cpp type.

        Args:
            decl: pygccxml cpp type.

        Returns:
            Python name of cpp type.
        """
        decl_str = str(decl)
        # Trim whitespaces and stuff.
        decl_str = re.sub(r"(\s\s+|\s?\&|\s?const)", "", decl_str)

        if self.is_templated(decl_str):
            return self.get_python_templated_type_name(decl_str)
        if decl_str in self.typedefs:
            return self.get_python_type_name(self.typedefs[decl_str])
        if decl_str in self.type_tranlation_table:
            return self.type_tranlation_table[decl_str]

        decl_str = re.sub(r"(\s?\*)", "", decl_str)

        # Remove namespace.
        namespace_idx = decl_str.rfind('::')
        if namespace_idx != -1:
            decl_str = decl_str[namespace_idx + 2:]

        # Set custom structs to Any.
        if decl_str in self.custom_types:
            return "Any"

        if self.current_location not in self.dependencies:
            self.dependencies[self.current_location] = set()
        self.dependencies[self.current_location].add(decl_str)

        return decl_str

    def get_python_default_value(self: Type[T], default_value: str) -> str:
        """
        Gets python name of default cpp value.

        Args:
            decl: Default cpp value.

        Returns:
            Python name of default cpp value.
        """
        if default_value in self.value_tranlation_table:
            return self.value_tranlation_table[default_value]

        # Convert floats.
        if default_value.lower().endswith('f'):
            default_value = default_value[:-1]

        return default_value

    def get_python_argument_name(self: Type[T], decl: declarations.calldef.argument_t) -> str:
        """
        Gets python name of cpp arguments.

        Args:
            decl: pygccxml arguments.

        Returns:
            Python name of cpp arguments.
        """
        return f"{decl.name}: {self.get_python_type_name(decl.decl_type)}" + (f" = {self.get_python_default_value(decl.default_value)}" if decl.default_value else "")

    def parse_dummy(self: Type[T], decl: declarations.declaration_t, output_file: IO, indent: int = 0) -> None:
        """
        Parses declaration.

        Args:
            decl: pygccxml declaration.
            output_file: file to write to.
            indent: Optional; indentation to use.
        """
        output_file.write("    " * indent + f"# {decl}\n\n")

    def parse_function(self: Type[T], decl: declarations.calldef.calldef_t, output_file: IO, indent: int = 0) -> None:
        """
        Parses function declaration.

        Args:
            decl: pygccxml calldef.
            output_file: file to write to.
            indent: Optional; indentation to use.
        """
        output_file.write("    " * indent + f"# {decl}\n")
        output_file.write("    " * indent + f"def {decl.name}(self{''.join([', ' + self.get_python_argument_name(a) for a in decl.arguments])}) -> {self.get_python_type_name(decl.return_type)}: ...\n\n")

    def parse_variable(self: Type[T], decl: declarations.variable.variable_t, output_file: IO, indent: int = 0) -> None:
        """
        Parses variable declaration.

        Args:
            decl: pygccxml variable.
            output_file: file to write to.
            indent: Optional; indentation to use.
        """
        output_file.write("    " * indent + f"# {decl}\n")
        output_file.write("    " * indent + "@property\n")
        output_file.write("    " * indent + f"def {decl.name}(self) -> {self.get_python_type_name(decl.decl_type)}: ...\n\n")

    def parse_class(self: Type[T], decl: declarations.class_declaration.class_t, output_file: IO, indent: int = 0) -> None:
        """
        Parses class declaration.

        Args:
            decl: pygccxml class.
            output_file: file to write to.
            indent: Optional; indentation to use.
        """
        if not decl.public_members and not decl.private_members and not decl.protected_members:
            return
        class_name = decl.name
        if self.is_templated(class_name):
            class_name = class_name.replace('<', '_').replace('>', '').replace(' ', '_')
        # Don't add member classes.
        if indent == 0:
            if self.current_location not in self.definitions:
                self.definitions[self.current_location] = set()
            self.definitions[self.current_location].add(class_name)
        output_file.write("    " * indent + f"class {class_name}():\n")
        if decl.public_members:
            output_file.write("    " * (indent + 1) + "# Public:\n")
            for public_member in decl.public_members:
                self.parse_declaration(public_member, output_file, indent + 1)
        if decl.private_members:
            output_file.write("    " * (indent + 1) + "# Private:\n")
            for private_member in decl.private_members:
                self.parse_declaration(private_member, output_file, indent + 1)
        if decl.protected_members:
            output_file.write("    " * (indent + 1) + "# Protected:\n")
            for protected_member in decl.protected_members:
                self.parse_declaration(protected_member, output_file, indent + 1)
        output_file.write("\n")

    def parse_enumeration(self: Type[T], decl: declarations.enumeration.enumeration_t, output_file: IO, indent: int = 0) -> None:
        """
        Parses enumeration declaration.

        Args:
            decl: pygccxml enumeration.
            output_file: file to write to.
            indent: Optional; indentation to use.
        """
        if not decl.values:
            return
        if self.current_location not in self.definitions:
            self.definitions[self.current_location] = set()
        if decl.name:
            # Don't add member classes.
            if indent == 0:
                self.definitions[self.current_location].add(decl.name)
            output_file.write("    " * indent + f"# {decl}\n")
            output_file.write("    " * indent + f"class {decl.name}(Enum):\n")
            indent += 1
        for value in decl.values:
            output_file.write("    " * indent + f"{value[0]} = {value[1]}\n")
            # Don't add member classes.
            if not decl.name and indent == 0:
                self.definitions[self.current_location].add(value[0])
        output_file.write("\n")

    def parse_constructor(self: Type[T], decl: declarations.calldef_members.constructor_t, output_file: IO, indent: int = 0) -> None:
        """
        Parses constructor declaration.

        Args:
            decl: pygccxml constructor.
            output_file: file to write to.
            indent: Optional; indentation to use.
        """
        output_file.write("    " * indent + f"# {decl}\n")
        # Disable move constructor.
        if decl.arguments and self.get_python_type_name(decl.parent.name) == self.get_python_type_name(decl.arguments[0].decl_type):
            output_file.write("\n")
        else:
            output_file.write("    " * indent + f"def __init__(self{''.join([', ' + self.get_python_argument_name(a) for a in decl.arguments])}) -> None: ...\n\n")

    def parse_destructor(self: Type[T], decl: declarations.calldef_members.destructor_t, output_file: IO, indent: int = 0) -> None:
        """
        Parses destructor declaration.

        Args:
            decl: pygccxml destructor.
            output_file: file to write to.
            indent: Optional; indentation to use.
        """
        output_file.write("    " * indent + f"# {decl}\n")
        output_file.write("    " * indent + "def __del__(self) -> None: ...\n\n")

    def parse_member_operator(self: Type[T], decl: declarations.calldef_members.operator_t, output_file: IO, indent: int = 0) -> None:
        """
        Parses members operator declaration.

        Args:
            decl: pygccxml members operator.
            output_file: file to write to.
            indent: Optional; indentation to use.
        """
        symbol = decl.symbol
        # TODO, check if argument or return type is same as class
        argument = self.get_python_type_name(decl.arguments[0].decl_type) if decl.arguments else ""
        return_type = self.get_python_type_name(decl.return_type) if decl.return_type else "None"

        output_file.write("    " * indent + f"# {decl}\n")

        if symbol == "+":
            output_file.write("    " * indent + f"def __add__(self, other: {argument}) -> {return_type}: ...\n\n")
        elif symbol == "-":
            output_file.write("    " * indent + f"def __sub__(self, other: {argument}) -> {return_type}: ...\n\n")
        elif symbol == "*":
            output_file.write("    " * indent + f"def __mul__(self, other: {argument}) -> {return_type}: ...\n\n")
        elif symbol == "/":
            output_file.write("    " * indent + f"def __truediv__(self, other: {argument}) -> {return_type}: ...\n\n")

        elif symbol == "+=":
            output_file.write("    " * indent + f"def __iadd__(self, other: {argument}) -> {return_type}: ...\n\n")
        elif symbol == "-=":
            output_file.write("    " * indent + f"def __isub__(self, other: {argument}) -> {return_type}: ...\n\n")
        elif symbol == "*=":
            output_file.write("    " * indent + f"def __imul__(self, other: {argument}) -> {return_type}: ...\n\n")
        elif symbol == "/=":
            output_file.write("    " * indent + f"def __itruediv__(self, other: {argument}) -> {return_type}: ...\n\n")

        elif symbol == "<":
            output_file.write("    " * indent + f"def __lt__(self, other: {argument}) -> bool: ...\n\n")
        elif symbol == "<=":
            output_file.write("    " * indent + f"def __le__(self, other: {argument}) -> bool: ...\n\n")
        elif symbol == "==":
            output_file.write("    " * indent + f"def __eq__(self, other: {argument}) -> bool: ...\n\n")
        elif symbol == "!=":
            output_file.write("    " * indent + f"def __ne__(self, other: {argument}) -> bool: ...\n\n")
        elif symbol == ">":
            output_file.write("    " * indent + f"def __gt__(self, other: {argument}) -> bool: ...\n\n")
        elif symbol == ">=":
            output_file.write("    " * indent + f"def __ge__(self, other: {argument}) -> bool: ...\n\n")

        elif symbol == "bool":
            output_file.write("    " * indent + "def __bool__(self) -> bool: ...\n\n")

        else:
            # pygccxml.declarations.calldef_members.member_operator_t
            # pygccxml.declarations.calldef_members.casting_operator_t
            self.unimplemented_declarations.add(type(decl))
            output_file.write("\n")

    def parse_declaration(self: Type[T], decl: declarations.declaration_t, output_file: IO, indent: int = 0) -> None:
        """
        Parses declaration.

        Args:
            decl: pygccxml declaration
            output_file: file to write to.
            indent: Optional; indentation to use.
        """
        if self.is_class(decl):
            self.parse_class(decl, output_file, indent)
        elif self.is_enumeration(decl):
            self.parse_enumeration(decl, output_file, indent)
        elif self.is_free_function(decl):
            self.parse_function(decl, output_file, indent)
        elif self.is_member_function(decl):
            self.parse_function(decl, output_file, indent)
        elif self.is_constructor(decl):
            self.parse_constructor(decl, output_file, indent)
        elif self.is_destructor(decl):
            self.parse_destructor(decl, output_file, indent)
        elif self.is_member_operator(decl):
            self.parse_member_operator(decl, output_file, indent)
        elif self.is_variable(decl):
            self.parse_variable(decl, output_file, indent)
        elif self.is_typedef(decl):
            self.typedefs[decl.name] = decl._decl_type
        else:
            # declarations.free_calldef.free_operator_t
            # declarations.class_declaration.class_declaration_t
            self.unimplemented_declarations.add(type(decl))
            self.parse_dummy(decl, output_file, indent)

    def get_dependencies(self: Type[T]) -> Set[str]:
        """
        Gets dependencies for current location.

        Returns:
            Set of dependencies for current location.
        """
        deps = self.dependencies[self.current_location] if self.current_location in self.dependencies else set()
        defs = self.definitions[self.current_location] if self.current_location in self.definitions else set()

        return deps - defs

    def parse_imports(self: Type[T], filename: str) -> None:
        """
        Parses python imports.

        Args:
            filename: File name to add python imports to.
        """
        file_contents = []
        if os.path.exists(filename):
            with open(filename, "r") as file:
                file_contents = file.readlines()
        if file_contents:
            with open(filename, "w") as file:
                # Check if the default dependencies where already added.
                typing_imports = "from typing import Callable, List, Tuple, Dict, Any\n"
                if file_contents[0] != typing_imports:
                    file.write(typing_imports)
                    file.write("from enum import Enum\n")
                    file.write("\n")
                file.writelines(file_contents)

    def parse_exports(self: Type[T]) -> None:
        """
        Parses python exports.
        """
        for location in self.definitions:
            dirname = os.path.dirname(location)
            filename = os.path.splitext(os.path.basename(location))[0]
            init_file = dirname + "/__init__.py"
            if not os.path.exists(init_file):
                dir_names = [name for name in os.listdir(dirname) if os.path.isdir(dirname + '/' + name)]
                if dir_names:
                    with open(init_file, "w") as file:
                        for dir_name in dir_names:
                            file.write(f"from .{dir_name} import *\n")
                        file.write("\n")
            with open(init_file, "a") as file:
                for definition in self.definitions[location]:
                    file.write(f"from .{filename} import {definition}\n")

    def parse_declarations(self: Type[T], decls: declarations.scopedef_t, output: str) -> None:
        """
        Parses scope declarations.

        Args:
            decl: pygccxml scope declaration
            output: file to write to.
        """
        # Removes any excisting files.
        if os.path.exists(os.path.dirname(output)):
            shutil.rmtree(output)
        os.makedirs(output)

        for decl in decls.declarations:
            if self.is_bm_declaration(decl):
                dirname = os.path.abspath(os.path.dirname(decl.location.file_name))[len(os.path.abspath(self.sdk_dir)) + 1:]
                if not os.path.exists(output + dirname):
                    os.makedirs(output + dirname)
                filename = output + dirname + "/" + os.path.splitext(os.path.basename(decl.location.file_name))[0] + ".pyi"
                self.current_location = filename
                # Write declarations to file.
                with open(filename, "a") as output_file:
                    self.parse_declaration(decl, output_file)
                self.parse_imports(filename)

        self.parse_exports()

        if self.unimplemented_declarations:
            print(f"Warning {self.unimplemented_declarations=}")
