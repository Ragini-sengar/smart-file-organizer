from organizer.classifier import FileClassifier
from organizer.duplicate_detector import DuplicateDetector
from organizer.file_mover import FileMover
from organizer.organizer import Organizer
import pytest


def create_organizer():
    categories = {
        ".txt": "Documents",
        ".py": "Python"
    }

    classifier = FileClassifier(categories)
    duplicate_detector = DuplicateDetector()
    file_mover = FileMover()

    return Organizer(classifier, duplicate_detector, file_mover)


def test_organizer_scans_and_classifies_files(tmp_path):
    source = tmp_path / "source"
    destination = tmp_path / "organized"

    source.mkdir()

    (source / "notes.txt").write_text("Study notes")
    (source / "script.py").write_text("print('Hello')")

    organizer = create_organizer()

    result = organizer.organize_folder(
        source,
        destination,
        dry_run=True
    )

    assert result["total_files"] == 2
    assert result["category_counts"] == {
        "Documents": 1,
        "Python": 1
    }


def test_organizer_detects_duplicates(tmp_path):
    source = tmp_path / "source"
    destination = tmp_path / "organized"

    source.mkdir()

    (source / "first.txt").write_text("Same content")
    (source / "second.txt").write_text("Same content")

    organizer = create_organizer()

    result = organizer.organize_folder(
        source,
        destination,
        dry_run=True
    )

    assert result["total_files"] == 2
    assert result["duplicate_count"] == 1


def test_organizer_moves_files_in_move_mode(tmp_path):
    source = tmp_path / "source"
    destination = tmp_path / "organized"

    source.mkdir()

    file = source / "notes.txt"
    file.write_text("My notes")

    organizer = create_organizer()

    organizer.organize_folder(
        source,
        destination,
        dry_run=False
    )

    assert not file.exists()
    assert (destination / "Documents" / "notes.txt").exists()

def test_organizer_handles_empty_folder(tmp_path):
    source = tmp_path / "empty_source"
    destination = tmp_path / "organized"

    source.mkdir()

    organizer = create_organizer()

    result = organizer.organize_folder(
        source,
        destination,
        dry_run=True
    )

    assert result["total_files"] == 0
    assert result["duplicate_count"] == 0
    assert result["category_counts"] == {}
    assert result["large_files"] == []

def test_organizer_handles_missing_folder(tmp_path):
    source = tmp_path / "missing_folder"
    destination = tmp_path / "organized"

    organizer = create_organizer()

    with pytest.raises(FileNotFoundError):
        organizer.organize_folder(
            source,
            destination,
            dry_run=True
        )

def test_organizer_rejects_file_as_source_folder(tmp_path):
    source = tmp_path / "notes.txt"
    source.write_text("This is a file")

    destination = tmp_path / "organized"

    organizer = create_organizer()

    with pytest.raises(NotADirectoryError):
        organizer.organize_folder(
            source,
            destination,
            dry_run=True
        )