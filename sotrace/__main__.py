import argparse
import importlib
import os

from .sotrace import open_links

parser = argparse.ArgumentParser()
parser.add_argument("file", help="File to execute with sotrace.")
parser.add_argument("--results", type=int, default=1, help="Number of results to open.")
parser.add_argument("--tags", type=list, default=["python"], help="Preferenced tags.")
args = parser.parse_args()

try:
    module = importlib.import_module(os.path.splitext(args.file)[0])
except Exception as e:
    print(type(e).__name__ + ": " + str(e))
    open_links(e, tags=args.tags, num_of_results=args.results)
