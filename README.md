# Mouse Debugger

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Mouse Debugger is a lightweight tool for people who want to check the sensitivity of their mouse. It always stays on top of the screen, so you don't need to limit yourself to testing the mouse functionality on one screen or page anymore.

## Features
- Monitor left, right, and middle mouse button status.
- Track mouse scroll events.
- Display real-time mouse position.
- Provide technical information about the connected mouse.
- Always on top of the screen for continuous monitoring.

## Installation

### Requirements
- Python 3.6+
- `pynput` library

### Install using pip
1. Clone the repository:
    ```sh
    git clone https://github.com/Weikang01/mouse_debugger.git
    cd mouse_debugger
    ```

2. Install the package:
    ```sh
    pip install .
    ```

## Building Executable

If you want to create a standalone executable for Windows, you can use `pyinstaller`. Follow these steps:

1. Install `pyinstaller`:
    ```sh
    pip install pyinstaller
    ```

2. Build the executable:
    ```sh
    pyinstaller --onefile --noconsole ./mousestatusapp.py
    ```

The executable will be created in the `dist` directory.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
Created by [Weikang Liu](https://github.com/Weikang01).
