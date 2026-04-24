"""$run(project_name.in.py) tests.

© $run(author.in.py) <$run(email.in.py)> $run(year.in.py)

Released under the GPL version 3, or (at your option) any later version.
"""

import sys
from pathlib import Path

import pytest
from pytest import CaptureFixture, LogCaptureFixture
from testutils import failing_cli_test, passing_cli_test

from $run(project_module.in.py) import main


from contextlib import chdir  # pyright: ignore


tests_dir = Path(__file__).parent.resolve() / "test-files"


# CLI tests
def test_help_option_should_produce_output(capsys: CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as e:
        main(["--help"])
    assert e.type is SystemExit
    assert e.value.code == 0
    assert capsys.readouterr().out.find("$run(description.in.py)") != -1


def test_greeting(
    capsys: CaptureFixture[str],
) -> None:
    with chdir(tests_dir):
        passing_cli_test(
            capsys,
            ["--greeting=Goodbye"],
            "greeting-goodbye-expected.txt",
        )


def test_invalid_command_line_argument_causes_an_error(
    capsys: CaptureFixture[str],
    caplog: LogCaptureFixture,
) -> None:
    if sys.version_info < (3, 12, 8):
        subcommand_list = "'demo'"
    else:
        subcommand_list = "demo"
    failing_cli_test(capsys, caplog, ["--foo", "a"], f"argument SUBCOMMAND: invalid choice: 'a' (choose from {subcommand_list})")