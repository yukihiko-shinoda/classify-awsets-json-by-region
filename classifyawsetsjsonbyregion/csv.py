# SPDX-FileCopyrightText: Copyright (c) 2023 Yukihiko Shinoda
# SPDX-License-Identifier: MIT
"""Json to CSV."""

import csv
from contextlib import contextmanager
from contextlib import suppress
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import sys
    from collections.abc import Generator

    # typeshed names the type of csv.writer() objects Writer since Python 3.10, and _writer before that.
    if sys.version_info >= (3, 10):
        from _csv import Writer as StandardCsvWriter
    else:
        from _csv import _writer

        StandardCsvWriter = _writer


class OutputCsv:
    """To output AWSets data into CSV."""

    def __init__(self, path_csv: Path) -> None:
        self.path_csv = path_csv
        with suppress(FileNotFoundError):
            self.path_csv.unlink()

    @contextmanager
    def writer(self) -> "Generator[StandardCsvWriter, None, None]":
        with self.path_csv.open("w", newline="") as csv_file_pointer:
            yield csv.writer(csv_file_pointer, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
