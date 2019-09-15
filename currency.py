# Kristen Flaherty
# Sec 01

# For the tests you should not change
# the contents of this list
# HOWEVER, your program should work
# no matter what the contents
# (i.e. we could change the number of
# currencies or which currencies are
# accepted)

accepted = ["USD", "RMB", "INR", "EUR"]

#input currency to check if present in list
desired_currency = input('Enter desired currency:\n').upper()

#see if it exists within accepted list
check_accepted = desired_currency in accepted
accepted_size = len(accepted)
print('Found in database (size='+str(accepted_size)+'):', check_accepted)
