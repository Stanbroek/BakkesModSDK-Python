from os import path
from typing import Type, TypeVar
from pygccxml import declarations

T = TypeVar('T', bound='ParserHelper')


class ParserHelper():
    """Helper functions for pygccxml parsers"""
    sdk_dir = None

    def is_bm_declaration(self: Type[T], decl: declarations.declaration_t) -> bool:
        """Checks if declaration is a BM declaration."""
        if not decl.location:
            return False

        return path.abspath(decl.location.file_name).startswith(path.abspath(self.sdk_dir))

    @staticmethod
    def is_class(decl: declarations.declaration_t) -> bool:
        """Matches classes and structs."""
        return isinstance(decl, declarations.class_declaration.class_t)

    @staticmethod
    def is_constructor(decl: declarations.declaration_t) -> bool:
        """Matches any constructors."""
        return isinstance(decl, declarations.calldef_members.constructor_t)

    @staticmethod
    def is_destructor(decl: declarations.declaration_t) -> bool:
        """Matches any destructors."""
        return isinstance(decl, declarations.calldef_members.destructor_t)

    @staticmethod
    def is_operator(decl: declarations.declaration_t) -> bool:
        """Matches any operators."""
        return isinstance(decl, declarations.operator_t)

    @staticmethod
    def is_free_operator(decl: declarations.declaration_t) -> bool:
        """Matches any free operators."""
        return isinstance(decl, declarations.free_calldef.free_operator_t)

    @staticmethod
    def is_member_operator(decl: declarations.declaration_t) -> bool:
        """Matches any member operators."""
        return isinstance(decl, declarations.calldef_members.member_operator_t)

    @staticmethod
    def is_casting_operator(decl: declarations.declaration_t) -> bool:
        """Matches any casting operators."""
        return isinstance(decl, declarations.calldef_members.casting_operator_t)

    @staticmethod
    def is_function(decl: declarations.declaration_t) -> bool:
        """Matches any functions."""
        return isinstance(decl, declarations.calldef.calldef_t)

    @staticmethod
    def is_free_function(decl: declarations.declaration_t) -> bool:
        """Matches any free functions."""
        declarations.free_calldef.free_operator_t
        return isinstance(decl, declarations.free_calldef.free_function_t)

    @staticmethod
    def is_member_function(decl: declarations.declaration_t) -> bool:
        """Matches any members functions."""
        return isinstance(decl, declarations.calldef_members.member_function_t)

    @staticmethod
    def is_variable(decl: declarations.declaration_t) -> bool:
        """Matches any variables."""
        return isinstance(decl, declarations.variable.variable_t)

    @staticmethod
    def is_enumeration(decl: declarations.declaration_t) -> bool:
        """Matches any enumerators."""
        return isinstance(decl, declarations.enumeration_t)

    @staticmethod
    def is_class_declaration(decl: declarations.declaration_t) -> bool:
        """Matches any classes."""
        return isinstance(decl, declarations.class_declaration.class_declaration_t)

    @staticmethod
    def is_typedef(decl: declarations.declaration_t) -> bool:
        """Matches any typedefs."""
        return isinstance(decl, declarations.typedef.typedef_t)

    @staticmethod
    def is_namespace(decl: declarations.declaration_t) -> bool:
        """Matches any namespaces."""
        return isinstance(decl, declarations.namespace.namespace_t)

    @staticmethod
    def is_templated(decl_str: str) -> bool:
        """Matches any templated declarations."""
        return declarations.templates.is_instantiation(decl_str)

    @staticmethod
    def is_deprecated(decl: declarations.declaration_t) -> bool:
        """Matches any declarations with deprecated attribute."""
        return decl.attributes and 'deprecated' in decl.attributes
