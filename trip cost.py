"""pay attention, this is exemple only and the price changes from one hotel to another. please notice the price of your hotel."""
def hotel_cost(nights):
    return 140 * nights
def plane_ride_cost(city):
    """it is posible to add more cities to this function. The price is an exemple only!"""
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
"""it can be that the cost of the rental and the discount is changing from one country to another or from one company to another. pay attention, this is an exemple only"""
def rental_car_cost(days):
    cost = 40 * days
    """discount canculation"""
    if days >= 7:
        cost -=50
    elif days >= 3:
        cost -= 20
    return cost
def trip_cost(city, days, spending_money):
    """total price of the vacation + extra money"""
    return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days) + spending_money
"""exemple for the function trip_cost"""
print trip_cost("Los Angeles", 5, 600)
