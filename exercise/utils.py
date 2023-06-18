import subprocess
import tempfile
import os
import shutil
from functools import lru_cache


# Maximum size of the cache (adjust as needed)
MAX_CACHE_SIZE = 100


@lru_cache(maxsize=MAX_CACHE_SIZE)
def run_cpp(code):
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Create a temporary file for the C++ code
    code_file = os.path.join(temp_dir, "code.cpp")
    with open(code_file, "w") as file:
        file.write(code)

    # Create a temporary file for the executable
    exe_file = os.path.join(temp_dir, "code.exe")

    try:
        # Compile the C++ code using g++
        compile_result = subprocess.run(
            ["g++", code_file, "-o", exe_file], capture_output=True, text=True
        )

        if compile_result.returncode == 0:
            # Execution if compilation succeeds
            # Execute the compiled C++ code
            result = subprocess.run(exe_file, capture_output=True, text=True)

            # Return the output and error (if any)
            return result.stdout, result.stderr
        else:
            # Execution if compilation fails
            error_message = compile_result.stderr

            return None, "Compiled Error"

    finally:
        # Remove the temporary directory and its contents
        shutil.rmtree(temp_dir)
