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
    """Reads in data from disk and returns md5 hash
    
    Examples
    --------
    >>> from cog_data._utils import get_sha256_hash
    >>> get_sha256_hash("./CogWeb/website_src/Language/Exercises/dat/stopwords.txt")
    '9aa3e6f003d6c0e07a2d6e049e43a5669d554622dbd38fef91b37d4a852e15a5'
    """
    return _get_hash(file_path, hashlib.sha256())


def get_md5_hash(file_path: Union[Path, str]) -> str:
    """Reads in data from disk and returns sha256 hash
    
    Examples
    --------
    >>> from cog_data._utils import get_md5_hash
    >>> get_md5_hash("./CogWeb/website_src/Language/Exercises/dat/stopwords.txt")
    'a25f9890bfa50457244792b4b5c15566'
    """
    return _get_hash(file_path, hashlib.md5())
