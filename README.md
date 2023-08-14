# CompareByContent Plugin for fman

This fman plugin provides a feature to compare two files by content on Mac. It integrates with the `opendiff` tool (FileMerge app from Xcode) to compare the contents of selected files in the left and right panes.

## Requirements

- **Mac Only**: This plugin is developed specifically for Mac and won't work on other operating systems.
- **Xcode**: The plugin uses the FileMerge app from Xcode, so Xcode must be installed on your Mac.

## Installation

You can install the CompareByContent plugin in two ways:

1. **Manually**:
    - Clone this repository.
    - Copy the files to `/Users/<username>/Library/Application Support/fman/Plugins/User/` directory.
    - Restart fman.
    - [More details on manual installation](https://fman.io/docs/plugins-introduction)

2. **Through fman Install Plugins feature**:
    - Press Shift+Cmd+P in fman.
    - Choose "Install Plugins".
    - Search for "Compare By Content" and install.
    - [More details on installing plugins through fman](https://fman.io/docs/installing-plugins)

## Usage

- Press CMD+Y to initiate the comparison. This shortcut can be customized in the `Key Bindings.json` file.
- Select one file in both the left and right panes or no files in either pane.
- If no files are selected, the file under the cursor will be compared with a matched file by name from the opposite pane.

## Support

If you encounter any issues or have any questions, please open an issue in this repository [CompareByContent](hhttps://github.com/igaevd/CompareByContent)