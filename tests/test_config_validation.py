
import pytest
from main import validate_config


def test_valid_config():
    config = {
        "categories": {
            ".pdf": "Documents",
            ".py": "Python"
        },
        "minimum_size_kb": 10
    }

    assert validate_config(config) is True


def test_missing_categories():
    config = {
        "minimum_size_kb": 10
    }

    with pytest.raises(ValueError):
        validate_config(config)


def test_categories_must_be_dictionary():
    config = {
        "categories": "Documents",
        "minimum_size_kb": 10
    }

    with pytest.raises(ValueError):
        validate_config(config)


def test_invalid_extension():
    config = {
        "categories": {
            "pdf": "Documents"
        },
        "minimum_size_kb": 10
    }

    with pytest.raises(ValueError):
        validate_config(config)


def test_empty_category_name():
    config = {
        "categories": {
            ".pdf": ""
        },
        "minimum_size_kb": 10
    }

    with pytest.raises(ValueError):
        validate_config(config)


def test_missing_minimum_size():
    config = {
        "categories": {
            ".pdf": "Documents"
        }
    }

    with pytest.raises(ValueError):
        validate_config(config)


def test_negative_minimum_size():
    config = {
        "categories": {
            ".pdf": "Documents"
        },
        "minimum_size_kb": -10
    }

    with pytest.raises(ValueError):
        validate_config(config)


def test_boolean_minimum_size():
    config = {
        "categories": {
            ".pdf": "Documents"
        },
        "minimum_size_kb": True
    }

    with pytest.raises(ValueError):
        validate_config(config)
