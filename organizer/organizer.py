from pathlib import Path
import logging

logger = logging.getLogger("SmartFileOrganizer")
class Organizer:

    def __init__(self, classifier, duplicate_detector, file_mover):

        self.classifier = classifier
        self.duplicate_detector = duplicate_detector
        self.file_mover = file_mover

    def organize_folder(self, folder, destination_root, dry_run=True,minimum_size_kb =10):
        folder = Path(folder)
        destination_root = Path(destination_root)
        if not folder.exists():
            raise FileNotFoundError(f"Source folder does not exist: {folder}")

        if not folder.is_dir():
            raise NotADirectoryError(f"Source path is not a directory: {folder}")
        logger.info("Organization started.")
        logger.info("Source folder: %s", folder)
        logger.info("Destination folder: %s", destination_root)
        logger.info("Mode: %s", "Preview" if dry_run else "Move")

        category_counts = {}
        duplicate_hashes = {}

        total_files = 0
        duplicate_count = 0
        large_files = []

        for file in folder.iterdir():

            if not file.is_file():
                continue

            total_files += 1

        # 1. Classify the file
            category = self.classifier.get_category(file)
            logger.info("Classified %s as %s",file.name,category)

            category_counts[category] = (category_counts.get(category, 0) + 1)

        # 2. Detect duplicates
            file_hash = self.duplicate_detector.calculate_hash(file)

            if file_hash in duplicate_hashes:
                print(
                    f"[Duplicate] {file.name} matches "
                    f"{duplicate_hashes[file_hash]}"
                )
                logger.warning("Duplicate detected: %s matches %s",file.name,duplicate_hashes[file_hash])
                duplicate_count += 1
            else:
                duplicate_hashes[file_hash] = file.name
                print(f"[UNIQUE] {file.name}")
                logger.info("Unique file detected: %s", file.name)

        # 3. Determine destination
            destination = destination_root / category

            print(file, category)

        # 4. Move or preview
            file_size = file.stat().st_size
            if dry_run:
                logger.info("Preview: %s would be moved to %s",file.name,destination)
            else:
                logger.info("Moving file: %s to %s",file.name,destination)
            self.file_mover.move_file(file,destination,dry_run)

        # 5. Detect large files (10 KB threshold)
            if  file_size> minimum_size_kb*1024:
                large_files.append((file.name,file_size))
                logger.info("Large file detected: %s (%.2f KB)",file.name,file_size / 1024)

        # 6. Display summary
        print("\nCategory Summary:")
        print("Duplicate Detection Completed!")

        print(f"\nTotal files scanned: {total_files}")
        print(f"Duplicate files found: {duplicate_count}")

        for category, count in category_counts.items():
            print(category, count)

        print("\nLarge Files Found:")

        for filename, size in large_files:
            print(f"{filename} - {size / 1024:.2f} KB")

        logger.info("Organization completed.")
        logger.info("Total files scanned: %d", total_files)
        logger.info("Duplicates found: %d", duplicate_count)
        logger.info("Large files found: %d", len(large_files))
        return {
            "total_files": total_files,
            "duplicate_count": duplicate_count,
            "category_counts": category_counts,
            "large_files": large_files
        }