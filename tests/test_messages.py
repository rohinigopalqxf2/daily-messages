"""
Code level tests for messages endpoint
"""
import os
from unittest.mock import patch
import main

@patch('main.get_messages_from_file')
def test_message_selection(mock_obj):
    "Test that /message gets the right content"
    print("\n")
    test_msg_1 = "Hello! This is unit test message 1!"
    test_msg_2 = "Hello! This is unit test message 2!"
    expected_messages = [test_msg_1, test_msg_2]
    mock_obj.return_value = expected_messages
    message = main.get_message()
    assert message.get('msg', '') in expected_messages
    print("/message is selecting the right message")

def test_message_file_exists():
    "Test the message file exists"
    assert os.path.exists(main.CULTURE_FILE)
    print("Culture file exists")

def test_message_content_matches():
    "Test that the selected message is in the culture file"
    with open(main.CULTURE_FILE, 'r') as file_handler:
        lines = [line.strip() for line in file_handler]
    message = main.get_message()
    assert message['msg'] in lines
    print("Found message selected by /message in culture file")
