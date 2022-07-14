from importlib.resources import path
from msilib.schema import Directory
from pathlib import Path

path=Path()

for files in path.glob('*.*'):
    print(files);
    
    # we can make Directory and remove Directory from this path method
    # mkdir and rmdir