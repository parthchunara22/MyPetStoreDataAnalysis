# MyPetStoreDataAnalysis

## Description
This project manages and analyzes pet data from the provided `pets.csv` file. It includes functions for data loading, cleaning, statistical analysis, and visualization.

## Requirements
- Python 3.x
- pandas
- matplotlib
- seaborn
- plotly

## Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/MyPetStoreDataAnalysis.git
    cd MyPetStoreDataAnalysis
    ```

2. Install the required libraries:
    ```bash
    pip install pandas matplotlib seaborn plotly
    ```

## Usage
1. Run the main script to perform the analysis:
    ```bash
    python main_script.py
    ```

## Functions
- `load_data(file_path)`: Loads the CSV file into a pandas DataFrame.
- `clean_data(df)`: Cleans the data, handling missing values and ensuring appropriate data types.
- `calculate_average_price(df, species)`: Calculates the average price of pets for a given species.
- `find_pets_with_feature(df, feature)`: Finds pets with a specified special feature.
- `get_species_statistics(df)`: Returns statistics for each species.
- `plot_price_distribution(df)`: Plots the price distribution.
- `plot_average_price_by_species(df)`: Plots the average price by species.
- `plot_price_vs_age(df)`: Plots price vs. age.
- `plot_age_distribution_by_species(df)`: Plots age distribution by species.

## Screenshots
Include screenshots showing the project running here.
