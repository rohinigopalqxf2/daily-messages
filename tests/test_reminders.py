"""
Code level tests for the reminders endpoint
"""
from datetime import datetime
from unittest.mock import patch
import main
from messages import reminders

@patch('main.get_weekday')
def test_reminder_day(mock_obj):
    "Test that the right reminder is coming for the right day"
    print("\n")
    for i in range(0, 7):
        mock_obj.return_value = i
        message = main.get_reminder()
        message = message.get('msg', 'Incorrect value!!')
        message = message.split('Reminder:</b>')[-1].lstrip()
        assert message in reminders.messages.get(i, [''])
        print(f'Got a valid reminder for day {i}')

def test_weekday():
    "Check if current weekday returned is right"
    #This is a super weird test just to get to 100% line coverage
    #Ideally, we will not need a test for a method that returns
    #only built in calls
    #I'm using an alternative way to get weekday and then checking
    today = int(datetime.today().strftime('%w'))
    assert (main.get_weekday() + 1)%7 == today
