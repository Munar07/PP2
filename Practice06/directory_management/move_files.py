import shutil
import os

os.makedirs("destination", exist_ok=True)

shutil.move("sample.txt", "destination/sample.txt")
shutil.copy("destination/sample.txt", "sample_copy.txt")