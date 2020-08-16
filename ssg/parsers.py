from typing import List
from pathlib import Path


class Parser:
    extensions = [] #type: List[str]

    def valid_extension(self, extension):
        return extension in self.extensions
    
    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, 'r') as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, 'w') as file:
            file.write(content)
