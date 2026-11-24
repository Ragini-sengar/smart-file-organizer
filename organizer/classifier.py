class FileClassifier:
    def __init__(self, categories):
        self.categories = categories

    def get_category(self, file):
        ext = file.suffix.lower()
        return self.categories.get(ext, "Others")