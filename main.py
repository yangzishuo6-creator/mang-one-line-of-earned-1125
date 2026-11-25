# Write the One Line of Earned Pride contest entry.
import os
from pathlib import Path


TEXT = "After three nights sewing and unpicking the same zipper, Omar drew it right up to his daughter’s chin. ‘Go get cold again.’"


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
