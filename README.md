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

## Data Sources

### 1. **Property Finder** 
- **Website**: [Property Finder](https://www.propertyfinder.ae)
- **Data Extracted**:
  - Property Price
  - Location (City/Neighborhood)
  - Number of Bedrooms
  - Area (in square feet)
  - Property Type (e.g., Apartment, Villa)

### 2. **Visual Crossing Weather API**
- **API Documentation**: [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api)
- **Data Extracted**:
  - Average Temperature (in Celsius)
  - Humidity (%)
  
These data sources are combined to create a comprehensive dataset for trend analysis.

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
git clone https://github.com/your-username/WeatherEstate-Insights.git
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
VISUAL_CROSSING_API_KEY=your_api_key_here
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
├── data/                       # Directory to store datasets
│   └── property_listings_with_weather.csv  # The cleaned dataset
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
