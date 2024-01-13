
import os
from pathlib import Path
import sys
import shutil

CATEGORIES = {
    "AUDIO": [".mp3", ".wav", ".flac", ".wma"],
    "DOCS": [".docx", ".txt", ".xlsx", "xls", ".pptx", ".doc"],
    "PICT": [".jpeg", ".png", ".jpg", ".svg"],
    "MOVIES": [".avi", ".mp4", ".mov", ".mkv"],
    "ARHiVE": [".zip", ".gz", ".tar"],
    "PDF": [".pdf"],
}
CYRILLIC_SYMBOLS = "aбвгдeёжзийклмнопpcтyфхцчшщъыьэюяєiїґ"
TRANSLATION = (
    "a",
    "b",
    "v",
    "g",
    "d",
    "e",
    "e",
    "j",
    "z",
    "u",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "f",
    "h",
    "ts",
    "ch",
    "sh",
    "sch",
    "",
    "u",
    "",
    "e",
    "yu",
    "ya",
    "je",
    "i",
    "ji",
    "g",
)
TRANS = {}
SYMB = ("!", "№", "$", "%", "&", "(", ")", "+", "-", "_", "#", " ")
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()
    TRANS[ord(c.lower())] = l.lower()
for i in SYMB:
    TRANS[ord(i)] = "_"

class FileManager:
    def __init__(self):
        pass

    def get_categories(self, file: Path) -> str:
        ext = file.suffix.lower()
        for cat, exts in CATEGORIES.items():
            if ext in exts:
                return cat
        return "OTHER"

    def move_file(self, file: Path, category: str, root_dir: Path) -> None:
        target_dir = root_dir.joinpath(category)
        if not target_dir.exists():
            target_dir.mkdir()
        new_path = target_dir.joinpath(file.name)
        file.replace(new_path)

    def sort_folder(self, path: Path) -> None:
        for element in path.glob("**/*"):
            if element.is_file():
                category = self.get_categories(element)
                self.move_file(element, category, path)

def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        print("No path to folder")
        sys.exit(1)
    if not path.exists():
        print("Folder does not exist")
        sys.exit(1)

    file_manager = FileManager()
    file_manager.sort_folder(path)
    print("All ok")

if __name__ == "__main__":
    main()
