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

import os


def remove_duplicates_from_file(file_path):
    """
    Reads a file, removes duplicate lines, and writes the unique lines back to the original file.

    Args:
        file_path (str): The path to the text file.
    """
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Remove duplicates by converting to a set and back to a list
        unique_lines = list(dict.fromkeys(lines))

        with open(file_path, "w") as file:
            file.writelines(unique_lines)

        print(
            f"Removed {len(lines) - len(unique_lines)} duplicate lines from {os.path.basename(file_path)}."
        )

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Get the absolute path to the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to output.txt
    file_to_process = os.path.join(script_dir, "output", "output.txt")

    remove_duplicates_from_file(file_to_process)
