from fman import DirectoryPaneCommand, show_alert
from urllib.parse import urlparse
import subprocess

class CompareByContent(DirectoryPaneCommand):
    def __call__(self):
        left_pane = self.pane.window.get_panes()[0]
        right_pane = self.pane.window.get_panes()[1]

        left_files = left_pane.get_selected_files()
        right_files = right_pane.get_selected_files()

        if len(left_files) != 1 or len(right_files) != 1:
            show_alert('Please select exactly one file in both the left and right panes.')
            return

        left_file = urlparse(left_files[0]).path
        right_file = urlparse(right_files[0]).path

        command = ['/usr/bin/opendiff', left_file, right_file]
        subprocess.call(command)