from typing import List
from pathlib import Path


class Parser:
    extensions = [] #type: List[str]

    def valid_extension(self, extension):
        return extension in self.extensions
    
    def parse(self, path: Path, source: Path, dest: Path):
