import time
import datetime


def is_time_format(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except ValueError:
        return False


def main():
    user_input = input("Input: ")

    if is_time_format(user_input):
        values = user_input.split(":")
        hours = values[0]
        minutes = values[1]

        now = datetime.datetime.now()
        new_date = now.replace(hour=int(hours), minute=int(minutes))
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        minutes = int((new_date - midnight).seconds / 60)
        print("Output: ", minutes)
    else:
        print("Error: Received input is not a valid time format.")

main()
