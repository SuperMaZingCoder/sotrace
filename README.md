# sotrace
This package opens up StackOverflow posts for your errors. It's the ultimate efficiency tool!

## Example Usage
```py
from sotrace import open_link


try:
    my_dict = {}
    print(my_dict[1])
except Exception as e:
    open_link(e)
```
```py
from sotrace import open_link


open_link("What does the yield keyword do?", tags=["python", "generator"], num_of_results=3)
```

`sotrace` can also be run from the command line as a wrapper of sorts.
```
❯ python3 -m sotrace example2.py
Traceback (most recent call last):
  File "example2.py", line 2, in <module>
    print(my_dict[1])
KeyError: 1
(Opens links)
```
More arguments can be found using `python3 -m sotrace -h`, which gives:
```
❯ python3 -m sotrace -h
usage: __main__.py [-h] [--results RESULTS] [--tags TAGS [TAGS ...]] [--not-pretty] file

positional arguments:
  file                  File to execute with sotrace.

optional arguments:
  -h, --help            show this help message and exit
  --results RESULTS     Number of results to open.
  --tags TAGS [TAGS ...]
                        Preferred tags.
  --not-pretty          Don't use prettier tracebacks from the rich library. (not recommended)
```

## Roadmap
- [ ] Documentation
- [ ] Default issue template
- [ ] Github Actions
