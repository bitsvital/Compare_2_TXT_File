"""
Copyright (C) 2026 BitsVital LLC

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


def sort_file_lines(file_path):
    """
    Sorts the lines of a text file alphabetically.

    Args:
        file_path (str): The path to the text file.
    """
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()

        lines.sort()

        with open(file_path, "w") as f:
            f.writelines(lines)

        print(f"Successfully sorted the lines in {file_path}")

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    sort_file_lines("output/output.txt")
