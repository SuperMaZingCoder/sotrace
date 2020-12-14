import argparse
import importlib
import os
import subprocess

from .sotrace import open_links

parser = argparse.ArgumentParser()
parser.add_argument("file", help="File to execute with sotrace.")
parser.add_argument("--results", type=int, default=1, help="Number of results to open.")
parser.add_argument("--tags", default=["python"], help="Preferenced tags.", nargs="+", type=str)
args = parser.parse_args()

# Someone please make a pull request to make this code better
try:
    subprocess.call(f"python3 {args.file}", shell=True)
    importlib.import_module(os.path.splitext(args.file)[0])
except Exception as e:
    open_links(e, tags=args.tags, num_of_results=args.results)
