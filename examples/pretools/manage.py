#!/usr/bin/env python
import sys
from pathlib import Path

from cogsol.core.management import execute_from_command_line


def main():
    project_path = Path(__file__).resolve().parent
    execute_from_command_line(sys.argv, project_path=project_path)


if __name__ == "__main__":
    main()
