from __future__ import annotations

import ast
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PREFIXES = ("%", "!", "get_ipython(")


def notebook_code(source: str) -> str:
    kept = []
    for line in source.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(SKIP_PREFIXES):
            continue
        kept.append(line)
    return "\n".join(kept)


class RepositoryChecks(unittest.TestCase):
    def test_all_python_files_compile(self):
        files = sorted(ROOT.rglob("*.py"))
        self.assertTrue(files, "No Python files found")
        for path in files:
            with self.subTest(file=path.relative_to(ROOT)):
                source = path.read_text(encoding="utf-8")
                compile(source, str(path), "exec")

    def test_all_notebooks_are_valid_and_code_cells_compile(self):
        notebooks = sorted(ROOT.rglob("*.ipynb"))
        self.assertTrue(notebooks, "No Jupyter notebooks found")
        for path in notebooks:
            with self.subTest(notebook=path.relative_to(ROOT)):
                notebook = json.loads(path.read_text(encoding="utf-8"))
                self.assertIn("cells", notebook)
                for number, cell in enumerate(notebook["cells"], start=1):
                    if cell.get("cell_type") != "code":
                        continue
                    source = cell.get("source", [])
                    if isinstance(source, list):
                        source = "".join(source)
                    cleaned = notebook_code(source)
                    if not cleaned.strip():
                        continue
                    compile(cleaned, f"{path.name}:cell {number}", "exec")

    def run_script(self, relative_path: str, user_input: str = ""):
        path = ROOT / relative_path
        with tempfile.TemporaryDirectory() as working_directory:
            result = subprocess.run(
                [sys.executable, str(path)],
                input=user_input,
                text=True,
                capture_output=True,
                cwd=working_directory,
                timeout=15,
            )
        self.assertEqual(
            result.returncode,
            0,
            msg=f"{relative_path} failed.\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}",
        )

    def test_basic_and_logic_scripts_run(self):
        scripts = [
            "Class_and_Objects/Basic_Class_Example.py",
            "Conditional_Statements/Python_Conditional_Statements.py",
            "Daily_Practice/Python_Daily_Practice.py",
            "Functions/Python_Functions.py",
            "Generators_and_Iterators/Python_Generators.py",
            "Lists_and_Comprehensions/Python_Lists_and_Comprehensions.py",
            "Logic_Practice/Python_Logic_Practice.py",
            "Loops/Python_Loops.py",
            "Python_Assignments/Basic_Python_Assignments.py",
            "String_Methods/Python_String_Methods.py",
        ]
        for script in scripts:
            with self.subTest(script=script):
                self.run_script(script)

    def test_numpy_script_runs(self):
        self.run_script("NumPy/Python_NumPy_Basics.py")

    def test_input_based_scripts_run_with_sample_inputs(self):
        cases = [
            ("Python Basics/Python_Basics.py", "Divyansh\n10\n5\n"),
            ("Pattern Printing/Pattern Printing via Input.py", "2\n2\n3\n"),
            ("Pattern Printing/Types of Pattern Printing.py", "3\n"),
        ]
        for script, sample_input in cases:
            with self.subTest(script=script):
                self.run_script(script, sample_input)

    def test_pattern_scripts_run(self):
        scripts = [
            "Pattern Printing/Number and Alphabet Triangle.py",
            "Pattern Printing/Pattern Printing Using While Loop.py",
            "Pattern Printing/Simple Pattern Printing.py",
        ]
        for script in scripts:
            with self.subTest(script=script):
                self.run_script(script)

    def test_mini_projects_run_with_sample_inputs(self):
        cases = [
            ("Mini_Projects/QR_Code_Generator/qr_code_generator.py", "https://example.com\n"),
            ("Mini_Projects/UPI_QR_Generator/upi_qr_generator.py", "demo@upi\nTest User\n10\n"),
            ("Mini_Projects/Text_Image_Conversion/text_image_conversion.py", "Hello from test\nmissing-image.png\n"),
        ]
        for script, sample_input in cases:
            with self.subTest(script=script):
                self.run_script(script, sample_input)


if __name__ == "__main__":
    unittest.main(verbosity=2)
