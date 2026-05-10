import pytest
from pathlib import Path
from build.parser import parse_config


def test_parses_key_value_pairs(tmp_path):
    (tmp_path / "client.env").write_text("BUSINESS_NAME=Priority Plumbing\nPHONE=+1-239-555-0100\n")
    result = parse_config(tmp_path)
    assert result["BUSINESS_NAME"] == "Priority Plumbing"
    assert result["PHONE"] == "+1-239-555-0100"


def test_blank_values_return_empty_string(tmp_path):
    (tmp_path / "client.env").write_text("FACEBOOK=\n")
    result = parse_config(tmp_path)
    assert result["FACEBOOK"] == ""


def test_comments_and_blank_lines_ignored(tmp_path):
    (tmp_path / "client.env").write_text("# This is a comment\n\nBUSINESS_NAME=Acme\n")
    result = parse_config(tmp_path)
    assert "# This is a comment" not in result
    assert result["BUSINESS_NAME"] == "Acme"


def test_values_with_equals_sign(tmp_path):
    (tmp_path / "client.env").write_text("HOME_META=Fast plumber = reliable service\n")
    result = parse_config(tmp_path)
    assert result["HOME_META"] == "Fast plumber = reliable service"


def test_missing_config_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        parse_config(tmp_path)
