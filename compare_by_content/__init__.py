from fman import DirectoryPaneCommand, show_alert
from urllib.parse import urlparse
import subprocess
import os

# Error Messages
NO_FILES_ERROR = 'Please select exactly one file in both the left and right panes or no files in either pane.'
MATCHING_FILE_NOT_FOUND_ERROR = 'Matching file not found in the other pane.'

class CompareByContent(DirectoryPaneCommand):

    def __call__(self):

        # Get the left and right panes
        left_pane = self.pane.window.get_panes()[0]
        right_pane = self.pane.window.get_panes()[1]

        # Get the selected files in each pane
        left_files = [urlparse(file_url).path for file_url in left_pane.get_selected_files()]
        right_files = [urlparse(file_url).path for file_url in right_pane.get_selected_files()]

        # Check if there is only one selected file in each panel
        if len(left_files) == 1 and len(right_files) == 1:
            left_file, right_file = left_files[0], right_files[0]

        # Check if no files are selected, and match files under the cursor
        elif len(left_files) == 0 and len(right_files) == 0:
            active_file = urlparse(self.pane.get_file_under_cursor()).path
            inactive_pane = right_pane if self.pane == left_pane else left_pane
            inactive_pane_path = urlparse(inactive_pane.get_path()).path
            inactive_file_name = os.path.basename(active_file)
            for root, dirs, files in os.walk(inactive_pane_path):
                if inactive_file_name in files:
                    inactive_file_path = os.path.join(root, inactive_file_name)
                    break
            else:
                show_alert(MATCHING_FILE_NOT_FOUND_ERROR)
                return

            left_file, right_file = (active_file, inactive_file_path) if self.pane == left_pane else (inactive_file_path, active_file)

        # If none of the above conditions are met, show an error
        else:
            show_alert(NO_FILES_ERROR)
            return

        # Open the files in the FileMerge app from Xcode
        command = ['/usr/bin/opendiff', left_file, right_file]
        subprocess.call(command)
