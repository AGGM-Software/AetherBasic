
# AetherWeb.py

import webbrowser
import tempfile
import os

class AetherWebModule:
    def __init__(self):
        pass
    def render_html_in_browser(self, html_code):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_file:
            temp_file.write(html_code.encode('utf-8'))
            temp_file_path = temp_file.name
        webbrowser.open(f"file://{os.path.abspath(temp_file_path)}")



