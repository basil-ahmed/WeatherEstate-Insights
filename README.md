# WeatherEstate Insights

### Real Estate Price Trends Based on Real Time Weather Conditions

---

## Project Overview

**WeatherEstate Insights** is a data pipeline project aimed at exploring the correlation between real estate prices and weather conditions in various neighborhoods. The project combines web scraping and API integration to provide unique insights into how environmental factors like temperature and humidity can influence property values. 

By scraping property listing data from **Property Finder** and fetching historical weather data using the **Visual Crossing Weather API**, this project generates a novel dataset that can be used by investors, property developers, and real estate enthusiasts for trend analysis.

---

## Features

- **Web Scraping**: Collects real estate data such as price, bedrooms, area, and property type from the Property Finder website.
- **API Integration**: Fetches weather data (temperature and humidity) for each property's location using the Visual Crossing Weather API.
- **Data Cleaning**: Cleans and formats the scraped data to make it suitable for analysis.
- **Unique Dataset**: Creates a dataset that is not publicly available, combining real estate and weather insights.

---

## Data Collection

### Description of Data Gathered

This project gathers two main types of data:

1. **Real Estate Data (from Property Finder)**
    - **Data Extracted**:
        - **Price**: The listing price of the property in AED.
        - **Location**: The neighborhood or city where the property is located.
        - **Bedrooms**: The number of bedrooms in the property.
        - **Area**: The size of the property in square feet.
        - **Property Type**: Type of property (e.g., Apartment, Villa, etc.).

   **Purpose**: Property Finder was chosen for its comprehensive coverage of real estate listings across different locations in the UAE. The platform provides granular details about various properties that allow for robust data analysis, such as price trends and property characteristics in specific neighborhoods. Scraping this data enables the generation of unique insights into how the real estate market varies across different regions.

2. **Weather Data (from Visual Crossing Weather API)**
    - **Data Extracted**:
        - **Average Temperature**: Historical average temperature for the location.
        - **Humidity**: Historical humidity levels for the location.
        
   **Purpose**: The weather API was chosen to understand the impact of environmental conditions, such as temperature and humidity, on real estate pricing. The weather data allows us to explore correlations between climatic factors and property desirability, thus adding a new layer of insight to real estate analysis.

### Value Proposition of the Dataset

The dataset created by this project merges two critical pieces of information—real estate prices and weather data—which are not readily available together in publicly accessible datasets. Here's the value it offers:

- **Unique Cross-Domain Insights**: Combining real estate prices with environmental factors provides insights into how weather conditions might affect property demand and value, which is especially relevant in regions with extreme climates, like the UAE. 
- **Actionable for Stakeholders**: 
    - **Property Investors** can leverage the dataset to make more informed decisions by identifying patterns between climate and property value.
    - **Real Estate Developers** can use the data to understand how the weather might influence construction trends or buyer preferences in certain areas.
    - **Researchers** can utilize this dataset for studying the socio-economic impacts of climate on urban development.

### Why Such a Dataset Is Not Freely Available

While real estate data or weather data might be available individually through certain platforms or APIs, a combined dataset that links real estate listings to weather patterns is not typically available for free for several reasons:

- **Data Silos**: Real estate platforms focus on property data while weather platforms focus on environmental data. There is rarely an incentive for these separate industries to collaborate and offer integrated datasets.
- **Specialized Demand**: The intersection of weather conditions and real estate prices is a niche area of analysis. Due to its specialized nature, only a limited number of platforms may create such datasets, often offering them as premium services.

By creating this combined dataset, the project offers a unique tool for those who wish to gain deeper insights into real estate trends in relation to weather conditions.

---

## Dataset

The final dataset will include the following columns:
- **Price**: The price of the property (in AED).
- **Location**: The neighborhood or city where the property is located.
- **Bedrooms**: The number of bedrooms in the property.
- **Area**: The size of the property in square feet.
- **Property Type**: Whether the property is an apartment, villa, etc.
- **Avg Temperature**: The average temperature in the property's location (in Celsius).
- **Humidity**: The average humidity level (%) in the property's location.

---

## Installation and Setup

### 1. Clone the Repository

To get started, clone the repository:

```bash
git clone https://github.com/basil-ahmed/WeatherEstate-Insights.git
cd WeatherEstate-Insights
```

### 2. Set Up Virtual Environment

It’s recommended to use a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Set Up API Key

You'll need to sign up for an account on [Visual Crossing](https://www.visualcrossing.com/weather-api) and get your API key. Once you have the key, create a `.env` file in the root of your project and add your key:

```bash
WEATHER_API_KEY=your_api_key_here
```

### 5. Run the Script

Now, you're ready to run the script:

```bash
python main.py
```

The script will scrape property data from Property Finder, fetch weather data, and save the combined dataset as a CSV file.

---

## Project Structure

```
WeatherEstate-Insights/
│
├── main.py                    # The main Python script for scraping and API integration
├── requirements.txt            # List of dependencies
├── README.md                   # Project documentation
├── ETHICS.md                   # Ethical considerations
├── .gitignore                  # Files to be ignored by Git
├── property_listings_with_weather.csv  # The cleaned dataset
└── .env                        # Environment variables (store your API key here)
```

---

## Example Dataset Output

| Price (AED) | Location       | Bedrooms | Area (sqft) | Property Type | Avg Temperature (°C) | Humidity (%) |
|-------------|----------------|----------|-------------|---------------|----------------------|--------------|
| 1,200,000   | Downtown Dubai | 2        | 1500        | Apartment     | 30                   | 50           |
| 950,000     | Marina Walk    | 1        | 900         | Apartment     | 32                   | 45           |
| 3,500,000   | Palm Jumeirah  | 4        | 3200        | Villa         | 33                   | 60           |

---

## Ethical Considerations

Please refer to the **[ETHICS.md](./ETHICS.md)** file for a discussion of how ethical concerns have been addressed in this project, including scraping practices, API usage, and privacy considerations.

---

## Value Proposition

This dataset offers unique insights by merging real estate and weather data, a combination that isn’t readily available in public datasets. Here are some potential applications:
- **Property Developers**: Gain insights into how weather conditions might influence property desirability in different areas.
- **Investors**: Identify locations with favorable real estate prices and conditions for long-term investments.
- **Real Estate Agents**: Use weather data to improve marketing strategies, promoting properties that are more attractive in certain conditions (e.g., cooler locations in hot climates).

---

## How to Use the Data

You can use this dataset for various types of analysis, including:
- **Price Trends**: Analyze real estate prices in different neighborhoods.
- **Weather Impact**: Identify correlations between weather conditions (temperature and humidity) and property prices.
- **Predictive Models**: Build predictive models to forecast property values based on location and weather factors.

---

## Future Work

- **Additional Weather Factors**: Integrate more weather data (e.g., wind speed, precipitation).
- **Time-Series Analysis**: Explore the impact of seasonal weather changes on real estate prices over time.
- **Expand Geographical Scope**: Extend the scraping and analysis to multiple cities or countries for a broader perspective.

---

## License

This project is licensed under the MIT License. See the **[LICENSE](./LICENSE)** file for more details.

---

## Contact

For any queries or suggestions, feel free to reach out:

- **Name**: Basil Ahmed Qureshi
- **Email**: [basil.ahmed@nyu.edu]
