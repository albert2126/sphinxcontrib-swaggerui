"""
    sphinxcontrib.swaggerui
    ~~~~~~~~~~~~~~~~~~~~~~~

    Provides the swaggerui directive for reST files to build an interactive HTML page with your OpenAPI specification document.

    :copyright: Copyright 2017 by Albert Bagdasaryan <albert.bagd@gmail.com>
    :license: BSD, see LICENSE for details.
"""

import pbr.version

if False:
    # For type annotations
    from typing import Any, Dict  # noqa
    from sphinx.application import Sphinx  # noqa

__version__ = pbr.version.VersionInfo(
    'swaggerui').version_string()


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    return {'version': __version__, 'parallel_read_safe': True}
