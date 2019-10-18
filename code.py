##!/usr/bin/python
#Chitula Lukonde
# -*- coding: utf-8 -*-
import calendar
import datetime

def days_in_month(year, month):
    
    days_in_month=calendar.monthrange(year,month)
    return days_in_month[1]



def is_valid_date(year, month, day):
    if year >= datetime.MINYEAR and year <= datetime.MAXYEAR:
        if month >= 1 and month <= 12:
            if day >= 1 and day <= days_in_month(year, month):
                return True

    return False


def days_between(
    year1,
    month1,
    day1,
    year2,
    month2,
    day2,
    ):

    if not (is_valid_date(year1, month1, day1) and is_valid_date(year2,
            month2, day2)):
        return 0

    days = (datetime.date(year1, month1, day1) - datetime.date(year2,
            month2, day2)).days

    # print("days_bwtween:", days_between)

    if days < 0:
        return -days

    return 0


def age_in_days(year, month, day):

    if not is_valid_date(year, month, day):
        return 0

    age_days = (datetime.date.today() - datetime.date(year, month,
                day)).days

    if age_days > 0:
        return age_days

    return 0

