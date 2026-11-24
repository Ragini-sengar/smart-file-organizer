from pathlib import Path
from organizer.file_mover import FileMover


def test_preview_mode_does_not_move_file(tmp_path):
    source = tmp_path / "sample.txt"
    destination = tmp_path / "organized"

    source.write_text("Hello World")

    mover = FileMover()
    mover.move_file(source, destination, dry_run=True)

    assert source.exists()
    assert not (destination / "sample.txt").exists()


def test_file_moves_successfully(tmp_path):
    source = tmp_path / "sample.txt"
    destination = tmp_path / "organized"

    source.write_text("Hello World")

    mover = FileMover()
    mover.move_file(source, destination, dry_run=False)

    target = destination / "sample.txt"

    assert target.exists()
    assert not source.exists()
    assert target.read_text() == "Hello World"


def test_destination_folder_is_created_automatically(tmp_path):
    source = tmp_path / "sample.txt"
    destination = tmp_path / "new_folder" / "organized"

    source.write_text("Testing folder creation")

    mover = FileMover()
    mover.move_file(source, destination, dry_run=False)

    assert destination.exists()
    assert (destination / "sample.txt").exists()


def test_existing_file_is_not_overwritten(tmp_path):
    source = tmp_path / "sample.txt"
    destination = tmp_path / "organized"

    source.write_text("New content")
    destination.mkdir()
    target = destination / "sample.txt"
    target.write_text("Original content")

    mover = FileMover()
    mover.move_file(source, destination, dry_run=False)

    assert source.exists()
    assert target.read_text() == "Original content"