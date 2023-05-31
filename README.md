# Workdays Calculator and Payment

This script calculates the number of working days in the current month and calculates the payment based on the number of worked days and additional hours.

## Prerequisites

- Python 3.x
- `calendar` module
- `datetime` module

## How to Use

1. Clone the repository or copy the script into a Python file.
2. Ensure that you have the required modules (`calendar` and `datetime`) installed.
3. Run the script using a Python interpreter.
4. The script will display the following information:
   - The first day of the month.
   - The total number of days in the month.
   - The number of working days in the month.
   - The calendar of the current month.
5. Enter the following inputs when prompted:
   - `add_days`: The number of additional work days you had.
   - `add_hours`: The number of additional hours you had.
   - `pay`: Your pay per hour.
   - `hours`: The number of hours you worked per day.
6. The script will calculate and display the following information:
   - The total number of hours you worked in the month.
   - Your payment for the month.

Note: Make sure to enter valid integers for the inputs; otherwise, an error message will be displayed.

## Example Output

```
The first day of the month is: Monday
This month has: 31 days
This month has: 22 working days
      May 2023
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31

How many additional work days did you have? 2
How many additional hours did you have? 5
What is your pay per hour? 10
How many hours did you work per day? 8

You worked for 176 hours this month
Your payment for this month is: 1410 zł
```

