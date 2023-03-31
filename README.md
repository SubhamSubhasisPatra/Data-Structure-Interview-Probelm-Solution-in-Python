# Data-Structure-Interview-Problem-Solution-in-Python

## Directory Structure 

```
project/
├── src/
│   ├── linked_list
│   ├── tree
└── tests/
    ├── test_linked_list
    ├── ...
```

```
┌───────────┐     imports     ┌─────────────┐
│ test_main ├───┬───────────►│    main.py   │
└───────────┘   │             └─────────────┘
                │
┌────────────────────┐   imports   ┌───────────────┐
│ test_linked_list.py ├───┬───────►│ linked_list.py│
└────────────────────┘   │         └───────────────┘
                          │
                     defines
                          │
                 ┌───────────────┐
                 │ linked_list.py│
                 └───────────────┘
```