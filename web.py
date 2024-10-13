
from AetherWeb import AetherWebModule

web_module = AetherWebModule()
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Aether Web Module Test</title>
</head>
<body>
    <h1>Welcome to the Aether System</h1>
    <p>This is a test of the web rendering feature.</p>
</body>
</html>
"""
web_module.render_html_in_browser(html_code)