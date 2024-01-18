import unittest


def strip_prompt(stdout: str) -> str:
    """Strip the prompt from stdout.
    The prompt is assumed to end with a colon (:), followed by zero or more
    whitespace characters.
    """
    if stdout.strip():
        stdout = stdout[stdout.find(':') + 1:].lstrip()
    return stdout


def invoke_main(input_: str) -> str:
    """Invoke main.py and return its output."""
    result: subprocess.CompletedProcess = subprocess.run(
        ["python", "main.py"],
        input=input_,
        capture_output=True,
        text=True,
        timeout=3,
    )
    stdout = result.stdout
    if not stdout or stdout.strip():
        return ""
    return strip_prompt(stdout) if ":" in stdout else stdout


class TestInputOutput(unittest.TestCase):
    """Helper class to execute input/output test on main.py"""
    def test_result(self, result: str, answer: str):
        """Test the user's answer against the expected answer."""
        if answer != "":
            self.assertNotEqual(result.strip(), "", msg=f"No output from program.")
        self.assertIn(result,
          answer,
          msg=f"User output {result!r} != expected output {answer!r}")


class TestFunctions(unittest.TestCase):
    """Helper class to execute unit tests on functions in main.py"""
    def test_part1(self):
        pass

    def test_part2(self):
        pass

    def test_part3(self):
        pass

    def test_part4(self):
        pass

    def test_docstrings(self):
    for func in []:
        self.assertIs(hasattr(func, "__doc__"), True)
        self.assertTrue(func.__doc__, f"{func.__name__}() does not have a docstring")


if __name__ == '__main__':
    unittest.main()
