from main import load_config


def test_load_valid_config(tmp_path):
    config_file = tmp_path / "config.json"

    config_file.write_text(
        '{"minimum_size_kb": 10, "categories": {".pdf": "Documents"}}',
        encoding="utf-8"
    )

    result = load_config(config_file)

    assert result["minimum_size_kb"] == 10
    assert result["categories"][".pdf"] == "Documents"


def test_missing_config_returns_none(tmp_path):
    config_file = tmp_path / "missing.json"

    result = load_config(config_file)

    assert result is None


def test_invalid_json_returns_none(tmp_path):
    config_file = tmp_path / "invalid.json"

    config_file.write_text(
        '{"minimum_size_kb": 10, invalid}',
        encoding="utf-8"
    )

    result = load_config(config_file)

    assert result is None