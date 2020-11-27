def split_dates(s):
    dates = s.split(' ')
    dates_dict = [{'year':int(date[:4]), 'month':int(date[5:7]), 'day':int(date[8:])} for date in dates]
    return dates_dict

s = input().strip()
from pprint import pprint
pprint(split_dates(s))
