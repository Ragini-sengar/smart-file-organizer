from pathlib import Path
import logging
import json
from organizer.classifier import FileClassifier
from organizer.duplicate_detector import DuplicateDetector
from organizer.file_mover import FileMover
from organizer.organizer import Organizer


# Logger configuration
logger = logging.getLogger("SmartFileOrganizer")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:
    handler = logging.FileHandler("organizer.log", encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)


# Creating path objects
folder = Path("test_files")
destination = Path("organized_files")
    
#JSon configuration 

def load_config(config_path=Path("config.json")):
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)

        validate_config(config)

        return config

    except FileNotFoundError:
        print("Configuration file not found!")
        return None

    except json.JSONDecodeError as e:
        print(
            f"Invalid JSON at line {e.lineno}, "
            f"column {e.colno}: {e.msg}"
        )
        return None

    except ValueError as e:
        print(f"Invalid configuration: {e}")
        return None


def validate_config(config):

    if not isinstance(config, dict):
        raise ValueError("Configuration must be a JSON object.")

    if "categories" not in config:
        raise ValueError("Missing 'categories' in configuration.")

    if not isinstance(config["categories"], dict):
        raise ValueError("'categories' must be a dictionary.")

    for extension, category in config["categories"].items():

        if not isinstance(extension, str) or not extension.startswith(".") or len(extension) < 2:
            raise ValueError(f"Invalid file extension: {extension}")

        if not isinstance(category, str) or not category.strip():
            raise ValueError(f"Invalid category for extension: {extension}")

    if "minimum_size_kb" not in config:
        raise ValueError("Missing 'minimum_size_kb' in configuration.")

    size = config["minimum_size_kb"]

    if isinstance(size, bool) or not isinstance(size, (int, float)):
        raise ValueError("'minimum_size_kb' must be a number.")

    if size <= 0:
        raise ValueError("'minimum_size_kb' must be greater than zero.")

    return True


def main():
    config = load_config()
    if config is None:
        print("Organizer cannot start without a valid configuration.")
        raise SystemExit

    categories = config["categories"]
    minimum_size = config["minimum_size_kb"]
    classifier = FileClassifier(categories)
    duplicate_detector = DuplicateDetector()
    file_mover = FileMover()
    organizer = Organizer(classifier,duplicate_detector,file_mover)

#Application

    if folder.is_dir():
        print("Welcome to Smart File Organizer!")
        print("Test Folder found successfully.")

    # Select Preview or Move mode
        while True:
            choice = input("Choose mode (Preview/Move): ").strip().lower()

            if choice == "preview":
                dry_run = True
                print("You selected Preview mode!")
                break

            elif choice == "move":
                dry_run = False
                print("You selected Move mode!")
                break

            else:
                print("Invalid choice!")

        organizer.organize_folder(folder,destination,dry_run,minimum_size)
    
    else:
        print("Error: Test Folder does not exist!")
        logger.error("Source folder does not exist: %s", folder)

if __name__ == "__main__":
    main()
