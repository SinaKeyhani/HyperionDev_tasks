hotel_prices = {
    'Majestic Resort': 402.08,
    'Comfort House': 261.45,
    'Prestige Resort': 116.09,
    'Royal Palace': 406.04,
    'Deluxe Hotel': 216.16,
    'Prestige Lodge': 469.23,
    'Grand Hotel': 418.73,
    'Luxury Villa': 355.94,
    'Deluxe Suites': 376.48,
    'Grand Inn': 296.2,
    'Luxury Motel': 204.17,
    'Paradise Villa': 389.42,
    'Luxury Palace': 307.41,
    'Prestige Retreat': 124.0,
    'Elegant Hotel': 302.89,
    'Paradise Hotel': 263.05,
    'Elegant Motel': 209.77,
    'Deluxe Motel': 330.95,
    'Majestic Palace': 219.29,
    'Royal Retreat': 447.78,
    'Luxury Suites': 179.07,
    'Serenity House': 289.04,
    'Paradise Palace': 477.92,
    'Majestic Villa': 499.74,
    'Elegant Lodge': 373.89,
    'Serenity Palace': 50.43,
    'Majestic Hotel': 285.83,
    'Prestige Suites': 76.31,
    'Grand Motel': 422.96,
    'Comfort Lodge': 285.35,
    'Comfort Retreat': 476.19,
    'Royal Motel': 111.7,
    'Comfort Resort': 483.42,
    'Luxury Retreat': 433.44,
    'Prestige Inn': 240.95,
    'Paradise Motel': 86.16,
    'Grand House': 191.61,
    'Luxury Inn': 195.53,
    'Majestic Motel': 247.09,
    'Deluxe House': 451.72,
    'Majestic Retreat': 312.24,
    'Comfort Villa': 369.85,
    'Royal Suites': 312.98,
    'Serenity Hotel': 203.12,
    'Paradise Suites': 283.01,
    'Elegant Villa': 345.87,
    'Serenity Inn': 114.76,
    'Grand Retreat': 332.16,
    'Royal Hotel': 320.19,
    'Deluxe Retreat': 411.87
}

city_flight_costs = {
    'New York': 300,
    'Los Angeles': 400,
    'Chicago': 350,
    'Houston': 375,
    'Phoenix': 360
}

car_rental_cost_per_day = 50  # Example car rental cost per day

def get_hotel_choice():
    while True:
        hotel_choice = input('Please enter the hotel that you want to book: ').title()
        if hotel_choice in hotel_prices:
            print(f'{hotel_choice} price per night is ${hotel_prices[hotel_choice]:.2f}')
            return hotel_choice
        else:
            print('Invalid hotel name, please choose between our available hotels.')

def get_num_nights(hotel_choice):
    while True:
        try:
            num_nights = int(input('Please enter the number of nights you will be staying at this hotel: '))
            if num_nights > 0:
                if num_nights <= 3:
                    total_cost = num_nights * hotel_prices[hotel_choice]
                elif 3 < num_nights <= 6:
                    total_cost = num_nights * hotel_prices[hotel_choice] * 0.8
                else:
                    total_cost = num_nights * hotel_prices[hotel_choice] * 0.6
                
                return num_nights, total_cost
            else:
                print('Number of nights must be a positive integer.')
        except ValueError:
            print('Please enter a valid number.')

def get_city_choice():
    print("\nAvailable cities for flights:")
    for city in city_flight_costs:
        print(city)
    
    while True:
        city_choice = input('Please enter the city you will be flying to: ').title()
        if city_choice in city_flight_costs:
            print(f'Flight cost to {city_choice} is ${city_flight_costs[city_choice]:.2f}')
            return city_choice
        else:
            print('Invalid city name, please choose from the available cities.')

def get_rental_days():
    while True:
        try:
            rental_days = int(input('Please enter the number of days you will be hiring a car: '))
            if rental_days > 0:
                return rental_days
            else:
                print('Number of rental days must be a positive integer.')
        except ValueError:
            print('Please enter a valid number.')

def main():
    print('''
                    -------------------------------------------
                        WELCOME TO TRAVEL PLANNING PROGRAM
          
        PLEASE ENTER YOUR CITY, HOTEL, NUMBER OF NIGHTS, NUMBER OF DAYS TO RENT A CAR
          
                        TO FIND OUT HOW MUCH YOUR TRAVEL COSTS
                    -------------------------------------------
          ''')

    city_choice = get_city_choice()
    hotel_choice = get_hotel_choice()
    num_nights, total_hotel_cost = get_num_nights(hotel_choice)
    rental_days = get_rental_days()
    flight_cost = city_flight_costs[city_choice]
    rental_cost = rental_days * car_rental_cost_per_day

    print(f"\nSummary of your choices:")
    print(f"City: {city_choice}")
    print(f"Flight cost: ${flight_cost:.2f}")
    print(f"Hotel: {hotel_choice}")
    print(f"Number of nights: {num_nights}")
    print(f"Total cost for hotel stay: ${total_hotel_cost:.2f}")
    print(f"Number of rental days: {rental_days}")
    print(f"Total cost for car rental: ${rental_cost:.2f}")
    print(f"Grand total cost: ${flight_cost + total_hotel_cost + rental_cost:.2f}")

main()
