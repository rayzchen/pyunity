from . import example1
from . import example2
from . import example3
from . import example4
from . import example5
from ..scene import SceneManager

import sys

example_list = [
    example1,
    example2,
    example3,
    example4,
    example5,
]

def show():
    if len(sys.argv) == 1: num = 0
    else: num = int(sys.argv[1])
    if not num:
        for index, example in enumerate(example_list):
            print("\nExample", index + 1)
            example.main()
            SceneManager.RemoveScene(SceneManager.GetSceneByName("Scene"))
    else:
        example_list[num - 1].main()