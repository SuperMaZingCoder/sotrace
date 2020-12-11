# StackOverflow Traces
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

## Roadmap
- [ ] Documentation
