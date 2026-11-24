import shutil
from pathlib import Path

class FileMover:

    def move_file(self, source, destination, dry_run=True):

        destination = Path(destination)

        if dry_run:
            print(f"[PREVIEW] {source.name} would be moved to {destination}")
            return

        destination.mkdir(parents=True, exist_ok=True)

        target = destination / source.name

        if target.exists():
            print(f"[SKIPPED] {source.name} already exists!")
            return

        shutil.move(str(source), str(target))

        print(f"[MOVED] {source.name} -> {destination}")