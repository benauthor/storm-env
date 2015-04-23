import os as _os
import sys as _sys
from types import ModuleType as _ModuleType

import avro.schema as _schema

_SCHEMA_ROOT = "schemas/"

_this_module = _sys.modules[__name__]


def _load_schema(path):
    return _schema.parse(open(path).read())


def _generate_submodules(parent_module, root):
    submodule_names = []
    for path, modules, files in _os.walk(root):
        if modules:
            for mod_name in modules:
                setattr(parent_module, mod_name, _ModuleType(mod_name))

        elif files:
            mod_name = path.split("/")[-1]
            submodule = getattr(parent_module, mod_name)
            submodule_names.append(mod_name)
            for filename in files:
                schema_name = filename.split(".")[0]
                schema = _load_schema("/".join((path, filename)))
                setattr(submodule, schema_name, schema)

__all__ = _generate_submodules(_this_module, _SCHEMA_ROOT)
