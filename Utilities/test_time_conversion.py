# from datetime import datetime, timedelta
# import pytest
#
#
# # GET method to get all the alerts at the Account Level
# @pytest.mark.parametrize('url', [""])
# def test_tc_Time_Conversion(url):
#     try:
#         # Time Conversion in different formats
#         now_datetime = datetime.now()
#         print("\n\nCurrent Date and Time:", now_datetime)
#
#         # Create a datetime object for September 11, 2023
#         timestamp = datetime(2023, 9, 11, 0, 30, 0)
#
#         # Convert the timestamp to ISO format
#         OneWeekCustomISO = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
#
#         # Print the ISO timestamp
#         print("\nISO Timestamp for September 11, 2023:", OneWeekCustomISO)
#
#         # Start of the day (00:00:00)
#         start_of_day_datetime = now_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
#         print("\nStart of the day_datetime:", start_of_day_datetime)
#
#         # End of the day (23:59:59)
#         end_of_day_datetime = now_datetime.replace(hour=23, minute=59, second=59, microsecond=999999)
#         print("\nEnd of the day_datetime:", end_of_day_datetime)
#
#         # Convert to timestamps (milliseconds since epoch)
#         start_timestamp = int(start_of_day_datetime.timestamp() * 1000)
#         end_timestamp = int(end_of_day_datetime.timestamp() * 1000)
#
#         print("\nStart timestamp:", start_timestamp)
#         print("\nEnd timestamp:", end_timestamp)
#
#         # Convert to ISO format
#         isocurrent = now_datetime.strftime('%Y-%m-%dT%H:%M:%S.000Z')
#         print("\nISO Current:", isocurrent)
#
#         isostart = start_of_day_datetime.strftime('%Y-%m-%dT%H:%M:%S.000Z')
#         print("\n" + "ISO Start: " + isostart)
#
#         isoend = end_of_day_datetime.strftime('%Y-%m-%dT%H:%M:%S.999Z')
#         print("\n" + "ISO END: " + isoend)
#
#         # Get today's date
#         presentday = datetime.today()
#         print("\n" + "Present Day: " + str(presentday))
#
#         presentday_timestamp = int(presentday.timestamp() * 1000)
#         print("\n" + "Present Day Timestamp: " + str(presentday_timestamp))
#
#         # Calculate 7 days ago
#         Seven_Days_Ago = presentday - timedelta(days=7)
#         # Print the result
#         print("\n" + "7 days ago from present day: ", Seven_Days_Ago)
#         # Convert to timestamp in milliseconds
#         SevenDaysAgoTimestamp = int(Seven_Days_Ago.timestamp() * 1000)
#         # Print the result
#         print("\n" + "7 days ago: ", SevenDaysAgoTimestamp)
#
#         # Calculate the start of yesterday
#         yesterday_start = (presentday - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
#         yesterday_start_timestamp = int(yesterday_start.timestamp() * 1000)
#         print("\n" + "Yesterday Start Timestamp:", yesterday_start_timestamp)
#         isoyesterday_start_timestamp = datetime.utcfromtimestamp(yesterday_start_timestamp / 1000).strftime(
#             '%Y-%m-%dT%H:%M:%S.000Z')
#         print("\n" + "ISO Yesterday Start Timestamp: " + isoyesterday_start_timestamp)
#
#         # Calculate the end of yesterday
#         yesterday_end = (presentday - timedelta(days=1)).replace(hour=23, minute=59, second=59, microsecond=999999)
#         yesterday_end_timestamp = int(yesterday_end.timestamp() * 1000)
#         print("\n" + "Yesterday End Timestamp:", yesterday_end_timestamp)
#         isoyesterday_end_timestamp = datetime.utcfromtimestamp(yesterday_end_timestamp / 1000).strftime(
#             '%Y-%m-%dT%H:%M:%S.000Z')
#         print("\n" + "ISO Yesterday End Timestamp: " + isoyesterday_end_timestamp)
#
#         # Get Yesterday
#         yesterday = presentday.replace(hour=23, minute=59, second=59) - timedelta(1)
#         print("\n" + "Yesterday: " + str(yesterday))
#         yesterday_timestamp = int(round(yesterday.timestamp() * 1000))
#         print("\n" + "Yesterday Timestamp: " + str(yesterday_timestamp))
#         isoyesterday = datetime.utcfromtimestamp(yesterday_timestamp / 1000).strftime('%Y-%m-%dT%H:%M:%S.000Z')
#         print("\n" + "ISO Yesterday: " + isoyesterday)
#
#         # Get custom date
#         custom = presentday.replace(hour=23, minute=59, second=59) - timedelta(2)
#         print("\n" + "Custom:" + str(custom))
#         custom_timestamp = int(round(custom.timestamp() * 1000))
#         print("\n" + "Custom Timestamp: " + str(custom_timestamp))
#         isocustom = datetime.utcfromtimestamp(custom_timestamp / 1000).strftime('%Y-%m-%dT%H:%M:%S.000Z')
#         print("\n" + "ISO Custom: " + isocustom)
#
#         # Get custom 1 week date
#         C1week = presentday.replace(hour=23, minute=59, second=59) - timedelta(4)
#         print("\n" + "C1Week: " + str(C1week))
#         custom_1week_timestamp = int(round(C1week.timestamp() * 1000))
#         print("\n" + "Custom_1week_timestamp: " + str(custom_1week_timestamp))
#         iso1weekcustom = datetime.utcfromtimestamp(custom_1week_timestamp / 1000).strftime('%Y-%m-%dT%H:%M:%S.000Z')
#         print("\n" + "ISO 1 Week Custom: " + iso1weekcustom)
#
#         # Get Tomorrow
#         tomorrow = presentday + timedelta(1)
#         print("\n" + "Tomorrow: " + str(tomorrow))
#         customnextdate = presentday.replace(hour=23, minute=59, second=59) + timedelta(2)
#         print("\n" + "Custom Next Date: " + str(customnextdate))
#         customnextdate_timestamp = int(round(customnextdate.timestamp() * 1000))
#         print("\n" + "Custom Nextdate Timestamp: " + str(customnextdate_timestamp))
#
#         # Get month
#         month = presentday.replace(hour=23, minute=59, second=59) - timedelta(31)
#         print("\n" + "Month: " + str(month))
#
#         month_timestamp = int(round(month.timestamp() * 1000))
#         print("\n" + "Previous Month Timestamp: " + str(month_timestamp))
#
#         isomonth = datetime.utcfromtimestamp(month_timestamp / 1000).strftime('%Y-%m-%dT%H:%M:%S.000Z')
#         print("\n" + "ISO Month: " + isomonth)
#
#         # Calculate the start of the current month
#         start_of_month = presentday.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
#         print("\n" + "Start of the Month:", start_of_month)
#
#         start_of_month_timestamp = int(start_of_month.timestamp() * 1000)
#         print("\n" + "Start of Month Timestamp :", start_of_month_timestamp)
#
#         end_of_month = start_of_month.replace(day=presentday.day, hour=0, minute=0, second=0, microsecond=0)
#         print("\n" + "End of the Month:", end_of_month)
#
#         end_of_month_timestamp = int(start_of_month.timestamp() * 1000)
#         print("\n" + "End of Month Timestamp :", end_of_month_timestamp)
#
#         # Calculate the end of the previous month
#         end_of_previous_month = start_of_month - timedelta(seconds=1)
#         print("\n" + "End of Previous Month:", end_of_previous_month)
#
#         # Calculate the start of the previous month
#         start_of_previous_month = end_of_previous_month.replace(day=1)
#         print("\n" + "Start of Previous Month:", start_of_previous_month)
#
#         # Convert timestamps to milliseconds
#         start_of_previous_month_timestamp = int(start_of_previous_month.timestamp() * 1000)
#         print("\n" + "Start of Previous Month Timestamp:", start_of_previous_month_timestamp)
#
#         end_of_previous_month_timestamp = int(end_of_previous_month.timestamp() * 1000)
#         print("\n" + "End of Previous Month Timestamp:", end_of_previous_month_timestamp)
#     except Exception as e:
#         print("Exception : " + str(e))
