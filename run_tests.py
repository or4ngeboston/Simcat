import pytest
import sys

if __name__ == "__main__":
    print("Running all tests...")
    # Pass command line arguments to pytest, or default to "-v" if none provided
    args = sys.argv[1:] if len(sys.argv) > 1 else ["-v"]
    exit_code = pytest.main(args)
    sys.exit(exit_code)
