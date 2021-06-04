import os
import shutil
from pygccxml import declarations
from typing import IO, Type, TypeVar

from ParserHelper import ParserHelper

T = TypeVar('T', bound='DebugParser')


class DebugParser(ParserHelper):
    """Parses pygccxml declarations into output files."""

    def __init__(self: Type[T], sdk_dir: str):
        """Initialises member variables."""
        self.sdk_dir = sdk_dir

    def parse_comments(self: Type[T], decl: declarations.comment.comment_t, output_file: IO, indent: int = 0) -> None:
        """
        Parses comment declarations.

        Args:
            decl: pygccxml comment.
            output_file: file to write to.
            indent: Optional; indentation to use.
        """
        if decl.text:
            output_file.write("    " * indent + f"[comment] {decl.text}\n")

    def parse_members(self: Type[T], decl: declarations.class_declaration.class_t, output_file: IO, indent: int = 0) -> None:
        """
        Parses class member declarations.

        Args:
            decl: pygccxml class.
            output_file: file to write to.
            indent: Optional; indentation to use.
        """
        self.parse_comments(decl.comment, output_file, indent)
        output_file.write("    " * indent + f"{decl}\n")
        if decl.public_members:
            output_file.write("    " * indent + "public:\n")
            for public_member in decl.public_members:
                self.parse_declaration(public_member, output_file, indent + 1)
        if decl.private_members:
            output_file.write("    " * indent + "private:\n")
            for private_member in decl.private_members:
                self.parse_declaration(private_member, output_file, indent + 1)
        if decl.protected_members:
            output_file.write("    " * indent + "protected:\n")
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
        self.parse_comments(decl.comment, output_file, indent)
        output_file.write("    " * indent + f"{decl}\n")
        indent += 1
        for value in decl.values:
            output_file.write("    " * indent + f"{value}\n")
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
            self.parse_members(decl, output_file, indent)
        elif self.is_enumeration(decl):
            self.parse_enumeration(decl, output_file, indent)
        else:
            self.parse_comments(decl.comment, output_file, indent)
            output_file.write("    " * indent + f"{decl}{f' [{decl.attributes}]' if decl.attributes else ''}\n")

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

        with open(output + "declarations.txt", "w") as log_file:
            for i, decl in enumerate(decls.declarations):
                dirname = "none"
                if decl.location:
                    dirname = os.path.abspath(decl.location.file_name)
                log_file.write(f"{i}: {decl} - {dirname}\n")
                if self.is_bm_declaration(decl):
                    filename = os.path.splitext(os.path.basename(decl.location.file_name))[0] + ".txt"
                    dirname = os.path.abspath(os.path.dirname(decl.location.file_name))[len(os.path.abspath(self.sdk_dir)) + 1:]
                    if not os.path.exists(output + dirname):
                        os.makedirs(output + dirname)
                    # Write declarations to file.
                    with open(output + dirname + "/" + filename, "a") as output_file:
                        self.parse_declaration(decl, output_file)
