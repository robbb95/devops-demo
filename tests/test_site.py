"""
Simple tests for our DevOps demo site.
These run automatically in the CI/CD pipeline on every push.
"""


def read_index():
    with open("index.html", "r") as f:
        return f.read()


def test_html_has_title():
    """Check that the page has a <title> tag."""
    html = read_index()
    assert "<title>" in html, "Missing <title> tag"
    assert "</title>" in html, "Missing closing </title> tag"


def test_html_has_devops_heading():
    """Check that the main heading contains 'DevOps'."""
    html = read_index()
    assert "DevOps" in html, "Page should mention DevOps"


def test_html_has_body():
    """Check basic HTML structure."""
    html = read_index()
    assert "<body>" in html, "Missing <body> tag"
    assert "</body>" in html, "Missing closing </body> tag"


def test_html_has_version():
    """Check that a version number is displayed."""
    html = read_index()
    assert "Version" in html, "Page should display a version"


def test_html_is_not_empty():
    """Check that the file has actual content."""
    html = read_index()
    assert len(html) > 100, "HTML file seems too short"
