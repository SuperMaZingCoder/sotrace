import argparse
import importlib
import os
import traceback
import subprocess


from .sotrace import open_links

parser = argparse.ArgumentParser()
parser.add_argument("file", help="File to execute with sotrace.")
parser.add_argument("--results", type=int, default=1, help="Number of results to open.")
parser.add_argument("--tags", default=["python"], help="Preferred tags.", nargs="+", type=str)
parser.add_argument("--not-pretty", action="store_true", help="Don't use prettier tracebacks from the rich library. (not recommended)")
args = parser.parse_args()

if not(args.not_pretty):
    from rich.console import Console
    console = Console()

try:
    importlib.import_module(os.path.splitext(args.file)[0])
except ModuleNotFoundError as e:
    print(f"Module {args.file} not found, are you sure you spelled the name correctly?")
except Exception as e:
    if not(args.not_pretty):
        console.print_exception()
    else:
        traceback.print_tb(e.__traceback__)
    open_links(e, tags=args.tags, num_of_results=args.results)
