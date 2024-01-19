import unittest

from autograding import TestInputOutput, TestFunction
from autograding.case import InOut, FuncCall


if __name__ == '__main__':
    import os
    if not os.listdir("autograding"):
        import subprocess
        subprocess.run(["git", "submodule", "update", "--init"])
    unittest.main()
