import requests
import json
import argparse
import random
import csv
import os
from collections import Counter
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
api_key = os.getenv('NUMBEO_API_KEY')
if not api_key:
    raise ValueError("No NUMBEO_API_KEY found in environment variables")

# Function to get a list of cities from the Numbeo API
def get_all_cities(country_code=None):
    url = f"https://www.numbeo.com/api/cities?api_key={api_key}"
    if country_code:
        url += f"&country={country_code}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()['cities']
    else:
        print("Failed to retrieve the list of cities")
        return []

# Function to get cost of living data for a city using its identifier
def get_cost_of_living(city_id):
    url = f"https://www.numbeo.com/api/city_prices?api_key={api_key}&city_id={city_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for city ID {city_id}")
        return None

# Function to extract rent data from cost of living data
def extract_rent_data(cost_of_living_data):
    rent_data = {}
    if 'prices' in cost_of_living_data:
        for item in cost_of_living_data['prices']:
            if 'apartment' in item['item_name'].lower() and 'rent' in item['item_name'].lower():
                rent_data[item['item_name']] = item['average_price']
    else:
        print("No 'prices' key in cost of living data:", cost_of_living_data)
    return rent_data

# Function to count cities by state
def count_cities_by_state(cities):
    state_counts = Counter()
    for city in cities:
        city_name = city['city']
        state = city_name.split(", ")[1] if ", " in city_name else "Unknown"
        state_counts[state] += 1
    return dict(sorted(state_counts.items()))

# Function to count cities by country
def count_cities_by_country(cities):
    country_counts = Counter(city['country'] for city in cities)
    return dict(sorted(country_counts.items()))

# Function to write results to CSV
def write_to_csv(data, output_file, header=None):
    with open(output_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if header:
            writer.writerow(header)
        for key, value in data.items():
            writer.writerow([key, value])

def main():
    parser = argparse.ArgumentParser(description="Retrieve cost of living data for cities using the Numbeo API.")
    parser.add_argument('--us-cities', action='store_true', help="Retrieve data for US cities only.")
    parser.add_argument('--all-cities', action='store_true', help="Retrieve data for all cities.")
    parser.add_argument('--dry-run', action='store_true', help="Perform a dry run with a limited number of cities.")
    parser.add_argument('--count-by-state', action='store_true', help="Count cities by state in the US.")
    parser.add_argument('--count-by-country', action='store_true', help="Count cities by country for all countries.")
    parser.add_argument('-o', '--output', type=str, help="Output the results to a CSV file with the specified filename.")

    args = parser.parse_args()

    if args.us_cities:
        cities = get_all_cities(country_code="US")
    else:
        cities = get_all_cities()

    if not cities:
        print("No cities retrieved. Exiting.")
        return

    if args.count_by_state:
        us_cities = get_all_cities(country_code="US")
        state_counts = count_cities_by_state(us_cities)
        if args.output:
            write_to_csv(state_counts, args.output, header=["State", "Count"])
        else:
            print(json.dumps(state_counts, indent=4))
        return

    if args.count_by_country:
        country_counts = count_cities_by_country(cities)
        if args.output:
            write_to_csv(country_counts, args.output, header=["Country", "Count"])
        else:
            print(json.dumps(country_counts, indent=4))
        return

    if not (args.us_cities or args.all_cities):
        print("No specific city option selected, defaulting to dry run.")
        args.dry_run = True

    if args.dry_run:
        cities = random.sample(cities, min(5, len(cities)))

    # Set up CSV file for writing rent data
    if args.output:
        with open(args.output, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["City", "Item", "Price"])

    # Iterate through the list of cities and get rent data
    for city in cities:
        city_id = city['city_id']
        city_name = city['city']
        cost_of_living_data = get_cost_of_living(city_id)
        if cost_of_living_data:
            rent_data = extract_rent_data(cost_of_living_data)
            if args.output:
                with open(args.output, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    for item, price in rent_data.items():
                        writer.writerow([city_name, item, price])
            else:
                print(f"City: {city_name}, Rent Data: {rent_data}")

if __name__ == "__main__":
    main()
