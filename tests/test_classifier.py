from pathlib import Path
from organizer.classifier import FileClassifier
import pytest

@pytest.fixture
def classifier():
    categories = {
        ".pdf": "Documents",
        ".docx": "Documents",
        ".txt": "Documents",
        ".py": "Python",
        ".jpg": "Images",
        ".png": "Images"
    }
    return FileClassifier(categories)

def test_python_file_is_classified_correctly(classifier):
    result = classifier.get_category(Path("script.py"))
    assert result == "Python"

def test_pdf_is_classified_as_document(classifier):
    result = classifier.get_category(Path("notes.pdf"))
    assert result == "Documents"

def test_image_is_classified_correctly(classifier):
    result = classifier.get_category(Path("photo.jpg"))
    assert result == "Images"

def test_unknown_extension_returns_others(classifier):
    result = classifier.get_category(Path("random.xyz"))
    assert result == "Others"