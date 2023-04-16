"""Configuration of pytest."""

from __future__ import annotations

from pathlib import Path
import shutil
from textwrap import dedent, indent
from typing import Generator

from click.testing import CliRunner
import pytest

collect_ignore = ["setup.py"]


@pytest.fixture()
def configured_cli_runner(tmp_path: Path, resource_path_root: Path) -> Generator[CliRunner, None, None]:
    """Prepares CLI runner with configuration files in temporary directory."""
    config_yaml_dist = Path(__file__).parent.parent / "config.yml.dist"
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path) as temp_dir:
        temp_path_dir = Path(temp_dir)
        config_file_test = Path("config.yml")
        config_file_for_test = temp_path_dir / config_file_test
        shutil.copy(config_yaml_dist, config_file_for_test)
        definition_exclude = indent(
            dedent(
                """\
            athena/workgroup:
            - prim*
            """,
            ),
            "  ",
        )
        with config_file_for_test.open("a") as file:
            file.write(definition_exclude)
        awsets_json_file_test = Path("awsets.json")
        input_directory = temp_path_dir / "input"
        input_directory.mkdir()
        shutil.copy(resource_path_root / awsets_json_file_test, input_directory / awsets_json_file_test)
        intermediate_directory = temp_path_dir / "intermediate"
        intermediate_directory.mkdir()
        output_directory = temp_path_dir / "output"
        output_directory.mkdir()
        yield runner
