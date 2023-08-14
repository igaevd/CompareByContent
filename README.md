# Compare By Content Plugin for fman

## Description

This plugin adds a new command "Compare By Content" to the fman command palette for macOS. When called, it launches `opendiff file1 file2`, where `file1` and `file2` are the selected files in the left and right panels. If files are not selected in both panels, an error alert will be displayed.

## Installation

1. Navigate to the fman's plugins directory.
2. Create a new folder named "CompareByContent."
3. Follow the instructions from the original guide to set up the required files.
4. Restart fman to load the new plugin.

## Usage

- Use the "Cmd+Y" keyboard shortcut or find "Compare By Content" in the command palette to launch the comparison.
- Ensure that files are selected in both the left and right panes before executing the command.

## Requirements

- macOS with Xcode and command-line tools installed.
- fman file commander for Mac.
- Ensure that the `opendiff` command is accessible from the command line.

## Support

For support or inquiries, please contact [igaevd@gmail.com](mailto:igaevd@gmail.com).

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
