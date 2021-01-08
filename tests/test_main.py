"""
Test for main page using fastapi test client.
"""
import os
import sys
from fastapi.testclient import TestClient
import main
import messages
import random
from main import app
from messages import reminders
from messages import senior_qa_training
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#Declaring directory
REPO_DIR = os.path.dirname(os.path.dirname(__file__))
MESSAGES_DIR = os.path.join(REPO_DIR, 'messages')

# Declaring files to delete
FILE_DELETE = ['senior_qa_training.pickle']

# Delete file
def delete_file(file_name):
    """
    This method will delete a particular file
    """
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f'{file_name} deleted')

# Delete files from particular directory
def delete_files_in_dir(directory, files):
    "The method will delete files in a particular directory"
    for file_name in files:
        delete_file(os.path.join(directory, file_name))

# Delete pickle file
def delete_pickle_file():
    "The method will delete pickle file"
    delete_files_in_dir(MESSAGES_DIR, FILE_DELETE)

# Declaring test client
client = TestClient(app)

# Test case for index page
def test_index():
    "asserting main endpoint"
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["msg"] != ''
    assert response.json() == {"msg":"This is the endpoint for the home page. /message \
        and /reminder are more useful starting points."}

# Test for status code for get message
def test_get_message():
    "asserting status code"
    response = client.get("/message")
    assert response.status_code == 200

# Test for asserting random message is in the file
def test_get_message_text():
    "asserting random message is in the file"
    response = client.get("/message")
    message = response.json()
    assert response.json()["msg"] != ''
    with open(main.CULTURE_FILE, 'r') as file_handler:
        lines = [line.strip() for line in file_handler]
    assert message['msg'] in lines

# Test for Reminders status code
def test_get_reminder():
    "asserting status code"
    response = client.get("/reminder")
    assert response.status_code == 200

# Test for asserting correct reminder sent
def test_get_reminder_text_check():
    "asserting message from the file"
    response = client.get("/reminder")
    message = response.json()
    assert response.json()["msg"] != ''
    weekday = main.get_weekday()
    lines = reminders.messages.get(weekday, [''])
    message = message.get('msg', '')
    message = message.split('Reminder:</b>')[-1].lstrip()
    assert message in lines

# Test for sep20_interns status code
def test_get_sep20_message():
    "asserting status code"
    response = client.get("/sep20-interns")
    assert response.status_code == 200

# Test for asserting correct message for sep20_interns
def test_get_sep20_message_text_check():
    "asserting message from the file"
    response = client.get("/sep20-interns")
    message = response.json()
    assert response.json()["msg"] != ''
    with open(main.SEP20_INTERNS_FILE, 'r') as file_handler:
        lines = [line.strip() for line in file_handler]
    assert message['msg'] in lines

# Test for trainig status code
def test_get_trainig():
    "asserting status code"
    response = client.get("/training")
    assert response.status_code == 200

# Test for asserting message with senior_qa_training messages
def test_get_snior_qa_training_message_text_check():
    "asserting message text check"
    response = client.get("/training")
    message = response.json()
    assert response.json()["msg"] != ''
    lines = senior_qa_training.messages
    assert message['msg'] in lines

# Test for asserting user_index and message_index are generated and incremented after every call
def test_get_snior_qa_training_message():
    "asserting user index and message_index generated and incremented after every call"
    lines = senior_qa_training.messages
    message = []
    user_index_dict = []
    message_index = 0
    message = main.get_snior_qa_training_message("user")
    assert message['msg'] in lines
    user_index_dict = main.get_senior_qa_training_user_index()
    message_index = user_index_dict['user'] + message_index
    assert user_index_dict['user'] == message_index
    main.set_senior_qa_training_user_index(user_index_dict)
    assert user_index_dict['user'] == message_index
    delete_pickle_file()

# Test for asserting all messages are generated
def test_unique_messages():
    """
    asserting unique messages are generated
    """
    messages = list()
    for call_count in range(len(senior_qa_training.messages)):
        message = main.get_snior_qa_training_message("user")
        messages.append(message['msg'])
    call_count += 1
    assert call_count == len(senior_qa_training.messages)
    assert len(set(messages)) == len(messages)
    new_message = main.get_snior_qa_training_message("user")
    assert messages[0] == new_message['msg']
    print(f"\nFirst message of new cycle: {new_message['msg']}")
    delete_pickle_file()
