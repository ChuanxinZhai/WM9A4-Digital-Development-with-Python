"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates. 判断日期关系

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'. 现在的日期
2. scheduled_date (string): The scheduled date to compare, in the same format. 预定的日期

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today. 判断预定的日期是否已经过去，还是还没到，还是今天
- Assume the dates are in the same year. 假设日子在同一年
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
日 月
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""

from datetime import datetime

def date_passed(todays_date, scheduled_date):

    # Convert datetime format                           移除后缀                                                             日（01-31）月份（全称）
    todays_date = datetime.strptime(todays_date.replace('th', '').replace('st', '').replace('nd', '').replace('rd', ''), '%d %B')
    scheduled_date = datetime.strptime(scheduled_date.replace('th', '').replace('st', '').replace('nd', '').replace('rd', ''), '%d %B')

    # Compare 
    if todays_date > scheduled_date:
        print("Scheduled date has passed")
    elif todays_date < scheduled_date:
        print("Scheduled date is yet to pass")
    else:
        print("Scheduled date is today")

# Test cases
date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass


# 方便查阅Reference list:
# %y 两位数的年份表示（00-99）没有世纪 short year version
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称 Mon, Tue, Wed, Thu, Fri, Sat, Sun
# %A 本地完整星期名称 Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
# %b 本地简化的月份名称 Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
# %B 本地完整的月份名称 January, February, March, April, May, June, July, August, September, October, November, December
# %c 本地相应的日期表示和时间表示 Local version of date and time
# %j 年内的一天（001-366）  Day number of year 001-366
# %p A.M./P.M.
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），Sunday is 0
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示 Local version of date
# %X 本地相应的时间表示 Local version of time
# %Z 当前时区的名称  Timezone
# %% %号本身
