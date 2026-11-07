<!-- source: https://raw.githubusercontent.com/danielgatis/rembg/main/rembg/__init__.py, fetched 2026-11-07, http 200, rendered with Playwright -->
try:
    from importlib.metadata import PackageNotFoundError, version

    try:
        \_\_version\_\_ = version("rembg")
    except PackageNotFoundError:
        \_\_version\_\_ = "0.0.0"  # Fallback for development
except ImportError:
    \_\_version\_\_ = "0.0.0"  # Fallback for older Python versions

from .bg import remove
from .session\_factory import new\_session
