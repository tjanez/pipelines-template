"""Central place for package metadata."""

# NOTE: We use __title__ instead of simply __name__ since the latter would
#       interfere with a global variable __name__ denoting object's name.
__title__ = 'pipelines-template'
__summary__ = 'Pipelines for the Resolwe platform'
__url__ = 'https://github.com/genialis/pipelines-template'

# Semantic versioning is used. For more information see:
# https://packaging.python.org/en/latest/distributing/#semantic-versioning-preferred
__version__ = '1.0.0'

__author__ = 'Genialis d.o.o.'
__email__ = 'dev-team@genialis.com'

__license__ = ''
__copyright__ = '2017, ' + __author__

__all__ = (
    "__title__", "__summary__", "__url__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__",
)
