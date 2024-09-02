"""atlas-ftag-tools - Common tools for ATLAS flavour tagging software."""

from __future__ import annotations

__version__ = "v0.2.2"


from ftag import hdf5
from ftag.cuts import Cuts
from ftag.flavour import Flavour, Flavours
from ftag.mock import get_mock_file
from ftag.sample import Sample
from ftag.transform import Transform
from ftag.wps.discriminant import get_discriminant
from ftag.wps.working_points import get_working_points

__all__ = [
    "Cuts",
    "Flavour",
    "Flavours",
    "Sample",
    "Transform",
    "__version__",
    "get_discriminant",
    "get_mock_file",
    "get_working_points",
    "hdf5",
]
