import hashlib
from pathlib import Path
from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from hashlib import _Hash
else:
    _Hash = Any

__all__ = ["get_sha256_hash", "get_md5_hash"]


def _get_hash(file_path: Union[Path, str], hash_fn: _Hash) -> str:
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_fn.update(chunk)
    return hash_fn.hexdigest()


def get_sha256_hash(file_path: Union[Path, str]) -> str:
    """Reads in data from disk and returns md5 hash"""
    return _get_hash(file_path, hashlib.sha256())


def get_md5_hash(file_path: Union[Path, str]) -> str:
    """Reads in data from disk and returns md5 hash"""
    return _get_hash(file_path, hashlib.md5())
