# SPDX-FileCopyrightText: Copyright (c) 2023 Yukihiko Shinoda
# SPDX-License-Identifier: MIT
"""Configurations."""

from dataclasses import dataclass
from typing import Dict
from typing import List

from yamldataclassconfig import YamlDataClassConfig


@dataclass
class Config(YamlDataClassConfig):
    """Configuration loaded from config.yml."""

    # Reason: `from __future__ import annotations` turns field.type into a string,
    # and dataclasses_json builds the marshmallow schema from field.type,
    # so these fields fall back to an untyped field ("Unknown type" warning) and lose type validation:
    # - PEP 563 - Postponed Evaluation of Annotations
    #   https://peps.python.org/pep-0563/
    # - dataclasses-json/dataclasses_json/mm.py at v0.6.7 · lidatong/dataclasses-json
    #   https://github.com/lidatong/dataclasses-json/blob/v0.6.7/dataclasses_json/mm.py#L306
    region_exclude: List[str] = None  # type: ignore[assignment]  # noqa: FA100
    ignore_pattern: Dict[str, List[str]] = None  # type: ignore[assignment]  # noqa: FA100
