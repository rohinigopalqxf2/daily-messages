"""
Test for the index page.
"""
import main

def test_index_contents():
    "Test the index page contents"
    expected_message = "This is the endpoint for the home page. /message \
        and /reminder are more useful starting points."
    message = main.index()
    assert message.get('msg', '') == expected_message
