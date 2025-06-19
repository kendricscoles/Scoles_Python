from business_logic.hotel_search_logic import search_hotels_combined, display_hotel_info

def hotel_search_prompt():
    print("\nWelcome to the Hotel Search!\nPlease enter the following preferences:")

    # 1. City
    print("1. City options:")
    cities = ["Basel", "Zürich", "Genève", "Bern", "Luzern"]
    for i, city in enumerate(cities, start=1):
        print(f"  {i}. {city}")
    city_choice = int(input("Choose a city by number (1-5): "))
    city = cities[city_choice - 1]

    # 2. Minimum stars
    print("\n2. Minimum stars:")
    for i in range(1, 6):
        print(f"  {i}. {i}★ and up")
    stars_choice = int(input("Choose minimum stars (1-5): "))
    min_stars = stars_choice

    # 3. Guest count
    print("\n3. Number of guests:")
    guests = int(input("How many guests? (1–6): "))

    # 4. Date range
    print("\n4. Date range:")
    check_in = input("Check-in date (YYYY-MM-DD): ")
    check_out = input("Check-out date (YYYY-MM-DD): ")

    print("\n🔎 Searching for matching hotels...\n")
    hotels = search_hotels_combined(city, min_stars, guests, check_in, check_out)

    if hotels:
        display_hotel_info(hotels)
    else:
        print("⚠️ No hotels found matching your criteria.")

# 🧪 Call the function to start
hotel_search_prompt()
