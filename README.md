
# Smart File Organizer

A modular Python application that automatically organizes files into categorized folders, detects duplicate files using SHA-256 hashing, identifies large files, and provides a safe preview mode before moving files.

## Features

- **Automatic File Classification:** Organizes files based on their extensions.
- **Duplicate Detection:** Uses SHA-256 hashing to identify files with identical content.
- **Large File Detection:** Identifies files exceeding a configurable size threshold.
- **Preview Mode:** Shows planned file movements without modifying files.
- **Safe File Movement:** Avoids overwriting files when a destination filename already exists.
- **Custom Configuration:** Allows users to define file categories and size thresholds through JSON.
- **Logging:** Records application activities and important events.
- **Input Validation:** Checks configuration settings and source folder paths.
- **Automated Testing:** Includes unit tests using pytest.

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- pathlib
- shutil
- hashlib
- JSON
- Logging
- pytest

## Project Structure

```text
smartfileorganizer/
│
├── organizer/
│   ├── __init__.py
│   ├── classifier.py
│   ├── duplicate_detector.py
│   ├── file_mover.py
│   └── organizer.py
│
├── tests/
│   ├── test_classifier.py
│   ├── test_config.py
│   ├── test_config_validation.py
│   ├── test_duplicate_detector.py
│   ├── test_file_mover.py
│   └── test_organizer.py
│
├── test_files/
├── main.py
├── config.json
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd smartfileorganizer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install pytest
```

## Configuration

The application uses `config.json` to define file categories and the minimum file size threshold.

Example:

```json
{
    "categories": {
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".pdf": "Documents",
        ".txt": "Documents",
        ".docx": "Documents",
        ".xlsx": "Documents",
        ".pptx": "Documents",
        ".py": "Python",
        ".mp4": "Videos",
        ".mkv": "Videos",
        ".mp3": "Audio",
        ".csv": "Spreadsheets"
    },
    "minimum_size_kb": 10
}
```

You can customize the extensions, categories, and file size threshold.

## Usage

1. Place the files you want to organize inside the source folder.
2. Configure the file categories in `config.json`.
3. Run the application:

```bash
python main.py
```

Follow the application's prompts to preview or execute file organization.

**Tip:** Use preview mode first to inspect the planned changes.

## Running Tests

Run the complete test suite:

```bash
python -m pytest -v
```

The project currently includes **28 automated tests** covering classification, configuration, duplicate detection, file movement, and organization.

## Learning Outcomes

This project demonstrates practical experience with:

- Python modular programming
- Object-Oriented Programming
- File-system operations
- Exception handling
- JSON configuration management
- Cryptographic hashing
- Logging and debugging
- Unit testing with pytest

## Future Improvements

- Graphical User Interface (GUI)
- AI-powered file categorization
- File metadata analysis
- Advanced duplicate management
- File organization reports and analytics

## Author

👤 Ragini_Sengar
