# Kristen
# Sec 01

#key parameters
seconds_given = int(input('Please enter number of seconds: '))

#convert seconds to whole hours, min and sec to nearest whole second
sec_in_min = 60
min_in_hr = 60

#find total hrs, exclude decimals
total_hrs = int(seconds_given / (min_in_hr*sec_in_min))

#find minutes in given seconds (use to find remainder or 'leftover minutes')
minutes = int(seconds_given/sec_in_min)

#find seconds by finding the remainder all seconds given
total_seconds = seconds_given % 60

#find remainder of minutes after all full minutes
total_minutes = minutes % 60

#print solution
print('This is ', total_hrs, ' hours, ', total_minutes, 'minutes, ',
total_seconds, 'seconds.')
