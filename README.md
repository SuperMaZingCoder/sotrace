# StackOverflow Traces
This package opens up StackOverflow posts for your errors. It's the ultimate efficiency tool!

## Example Usage
```py
from sotrace.open_link import open_link


try:
    my_dict = {}
    print(my_dict[1])
except Exception as e:
    open_link(e)
