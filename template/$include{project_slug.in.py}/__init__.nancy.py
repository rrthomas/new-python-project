# © $include{author.in.py} <$include{email.in.py}> $include{year.in.py}
# Released under the GPL version 3, or (at your option) any later version.

import argparse
import importlib.metadata
import sys
import warnings

from .warnings_util import simple_warning


VERSION = importlib.metadata.version("$include{project_slug.in.py}")


def main(argv: list[str] = sys.argv[1:]) -> None:
    # Command-line arguments
    parser = argparse.ArgumentParser(
        description="$include{description.in.py}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"""%(prog)s {VERSION}
© $include{year.in.py} $include{author.in.py} <$include{email.in.py}>
https://github.com/rrthomas/$include{project_slug.in.py}
Distributed under the GNU General Public License version 3, or (at
your option) any later version. There is no warranty.""",
    )
    warnings.showwarning = simple_warning(parser.prog)

    args = parser.parse_args(argv)

    print("Hello from $include{project_slug.in.py}!")