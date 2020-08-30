"""
Code level tests for the reminders endpoint
"""
from unittest.mock import Mock, patch
import main
from messages import reminders

@patch('main.get_weekday')
def test_reminder_day(mock_obj):
    "Test that the right reminder is coming for the right day"
    print("\n")
    for i in range(0,7):
        mock_obj.return_value = i
        message = main.get_reminder()
        message = message.get('msg', 'Incorrect value!!')
        message = message.split('Reminder:</b>')[-1].lstrip()
        assert message in reminders.messages.get(i, [''])
        print(f'Got a valid reminder for day {i}')
