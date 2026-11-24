from organizer.duplicate_detector import DuplicateDetector


def test_identical_files_have_same_hash(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    file1.write_text("Hello Smart File Organizer")
    file2.write_text("Hello Smart File Organizer")

    detector = DuplicateDetector()

    hash1 = detector.calculate_hash(file1)
    hash2 = detector.calculate_hash(file2)

    assert hash1 == hash2


def test_different_files_have_different_hashes(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    file1.write_text("Hello")
    file2.write_text("Goodbye")

    detector = DuplicateDetector()

    hash1 = detector.calculate_hash(file1)
    hash2 = detector.calculate_hash(file2)

    assert hash1 != hash2

def test_empty_files_have_same_hash(tmp_path):
    file1 = tmp_path / "empty1.txt"
    file2 = tmp_path / "empty2.txt"

    file1.write_text("")
    file2.write_text("")

    detector = DuplicateDetector()

    hash1 = detector.calculate_hash(file1)
    hash2 = detector.calculate_hash(file2)

    assert hash1 == hash2
    assert len(hash1) == 64