from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests

# Visual Crossing Weather API URL
weather_api_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
api_key = process.env.WEATHER_API_KEY

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()

# Scrape property data from Property Finder using Selenium
def scrape_property_page(page_number):
    base_url = f"https://www.propertyfinder.ae/en/search?l=3-41-172&c=2&fu=0&rp=y&ob=mr&page={page_number}"
    driver.get(base_url)

    try:
        # Wait until the properties are visible (use a general element that's always there)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "article"))
        )
    except Exception as e:
        print(f"Error: Page took too long to load or no properties found: {e}")
        return []

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    property_data = []
    
    # Update the class selectors based on the current page structure
    properties = soup.find_all('article', {'class': 'property-card-module_property-card__wrapper__ZZTal'})

    if not properties:
        print(f"No properties found on page {page_number}")
    
    for property in properties:
        try:
            price_element = property.find('p', class_='styles-module_content__price__SgQ5p')
            location_element = property.find('p', class_='styles-module_content__location__bNgNM')
            bedrooms_element = property.find('p', {'data-testid': 'property-card-spec-bedroom'})
            area_element = property.find('p', {'data-testid': 'property-card-spec-area'})
            property_type_element = property.find('p', class_='styles-module_content__property-type__QuVl4')

            # Check if each element exists before attempting to extract text
            if not price_element or not location_element or not bedrooms_element or not area_element or not property_type_element:
                print(f"Skipping a property on page {page_number} due to missing data.")
                continue

            price = price_element.text.strip()
            location = location_element.text.strip()
            bedrooms = bedrooms_element.text.strip()
            area = area_element.text.strip()
            property_type = property_type_element.text.strip()

            property_data.append({
                'Price': price,
                'Location': location,
                'Bedrooms': bedrooms,
                'Area': area,
                'Property Type': property_type
            })
        except AttributeError as e:
            print(f"Error processing property on page {page_number}: {e}")
            continue

    return property_data

# Fetch weather data from Visual Crossing API
def fetch_weather_data(location):
    location_parts = location.split(', ')
    
    for i in range(len(location_parts)):
        query_location = ', '.join(location_parts[i:])
        query = f"{weather_api_url}{query_location}?key={api_key}&unitGroup=metric&include=days"
        response = requests.get(query)
        
        if response.status_code == 200:
            weather_data = response.json()
            avg_temp = weather_data['days'][0].get('temp', None)
            humidity = weather_data['days'][0].get('humidity', None)
            return avg_temp, humidity
        else:
            print(f"Failed to retrieve weather data for {query_location}")
    
    return None, None

# Main script to scrape properties and combine with weather data
all_data = []
for i in range(1, 3):  # Scraping only 2 pages for this example
    property_data = scrape_property_page(i)
    
    if not property_data:
        print(f"No data scraped for page {i}")
        continue
    
    for prop in property_data:
        # Fetch weather data for the property location
        avg_temp, humidity = fetch_weather_data(prop['Location'])
        if avg_temp is not None and humidity is not None:
            prop['Avg Temperature'] = avg_temp
            prop['Humidity'] = humidity
        
        all_data.append(prop)
    
    time.sleep(2)  # Respectful rate limiting

# If there is no data, skip processing
if not all_data:
    print("No data collected from the website.")
else:
    # Convert to DataFrame and clean data
    df = pd.DataFrame(all_data)

    if 'Price' in df.columns:
        # Clean the price column to remove any non-numeric characters
        df['Price'] = df['Price'].str.replace(',', '')\
                                 .str.replace('AED', '')\
                                 .str.replace('/year', '')\
                                 .str.replace('/month', '')\
                                 .str.strip()  # Ensure any leading/trailing spaces are removed
        # Convert cleaned price to float
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')  # Convert to float, invalid parsing will result in NaN
    
    if 'Bedrooms' in df.columns:
        df['Bedrooms'] = df['Bedrooms'].str.extract('(\d+)').astype(float)
    
    if 'Area' in df.columns:
        df['Area'] = df['Area'].str.replace(',', '').str.replace('sqft', '').astype(float)

    # Drop rows with NaN values in the Price column (if necessary)
    df.dropna(subset=['Price'], inplace=True)

    # Save to CSV
    df.to_csv('property_listings_with_weather.csv', index=False)
    print("Scraping complete, data saved to property_listings_with_weather.csv.")

# Close the Selenium WebDriver when done
driver.quit()