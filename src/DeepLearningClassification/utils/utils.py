import pickle
import sys
from pathlib import Path

import numpy as np
import yaml

from ..exception.exceptions import CustomeException
from ..logging.logger import logger


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as exc:
        raise CustomeException(exc, sys) from exc


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        path = Path(file_path)
        serialized = yaml.safe_dump(content)
        path.parent.mkdir(parents=True, exist_ok=True)
        mode = "w" if replace else "x"
        with path.open(mode, encoding="utf-8") as yaml_file:
            yaml_file.write(serialized)
    except Exception as exc:
        raise CustomeException(exc, sys) from exc


def save_numpy_array(file_path: str, array: np.ndarray) -> None:
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("wb") as file_obj:
            np.save(file_obj, array)
    except Exception as exc:
        raise CustomeException(exc, sys) from exc


def load_numpy_array(file_path: str) -> np.ndarray:
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as exc:
        raise CustomeException(exc, sys) from exc


def save_object(file_path: str, obj: object) -> None:
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as exc:
        raise CustomeException(exc, sys) from exc


def load_object(file_path: str) -> object:
    """Load a pickle file from a trusted source."""
    try:
        with open(file_path, "rb") as file_obj:
            logger.info("Loading object from %s", file_path)
            return pickle.load(file_obj)
    except Exception as exc:
        raise CustomeException(exc, sys) from exc
