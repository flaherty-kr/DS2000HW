# Kristen Flaherty
# Sec 01 

#enter number of use dollars
USD = float(input('Please enter number of US dollars:\n'))
conversion_rate = float(input('1 USD = ? foreign units:\n'))
conversion_fee = float(input('Fee for buying currency in USD:\n'))

#account for fee on given USD
USD_after_fee = USD - conversion_fee

#calculate foreign units based on rate and USD after fee
foreign_units = int(conversion_rate * USD_after_fee)

print('You have', foreign_units, 'full unit(s) of foreign currency.')
