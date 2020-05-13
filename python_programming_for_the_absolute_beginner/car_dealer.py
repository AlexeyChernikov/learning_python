# Enter the value of the car without extra charges. The program should add 
# a few additional amounts to it: tax, registration fee, agency fee, delivery 
# price of the car at the destination. Let the tax and registration fee be 
# calculated as a fraction of the initial cost, and the remaining margins 
# will be considered fixed values.
#
# The final price of the car should be displayed.

AGENCY_FEE = 100
COST_OF_DELIVERY = 200

real_price = float(input('Enter the real value of the car: '))

tax = real_price * (5 / 100)
registration_fee = real_price *  (8 / 100)
final_price = real_price + tax + registration_fee + AGENCY_FEE + COST_OF_DELIVERY

print(f'The final price of the car: {final_price}')