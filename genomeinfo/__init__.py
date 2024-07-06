from . import core
from .interface import GenomeInfo

for module in [core]:
    for name, func in module.__dict__.items():
        if callable(func) and not name.startswith("_"):
            setattr(GenomeInfo, name, func)

__all__ = ["GenomeInfo"]
