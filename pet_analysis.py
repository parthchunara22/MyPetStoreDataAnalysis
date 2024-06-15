import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df = df.dropna()  # Handle missing values
    df.columns = [col.strip() for col in df.columns]  # Strip whitespace from column names
    df.PetID = df.PetID.astype(int)
    df.Birthdate = pd.to_datetime(df.Birthdate)
    df.Price = df.Price.astype(float)
    df.Species = df.Species.astype(str)
    df.SpecialFeature = df.SpecialFeature.astype(str)
    return df

def calculate_average_price(df, species):
    species_df = df[df.Species == species]
    return species_df.Price.mean()

def find_pets_with_feature(df, feature):
    feature_df = df[df.SpecialFeature == feature]
    return feature_df.Name.tolist()

def get_species_statistics(df):
    species_stats = {}
    for species in df.Species.unique():
        species_df = df[df.Species == species]
        avg_price = species_df.Price.mean()
        avg_age = species_df.Birthdate.apply(lambda x: (datetime.now() - x).days / 365).mean()
        species_stats[species] = {'Average Price': avg_price, 'Average Age': avg_age}
    return species_stats

def plot_price_distribution(df):
    output_dir = '../Parth_Project/output'
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
    plt.hist(df.Price, bins=30)
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.title('Price Distribution')
    plt.savefig(os.path.join(output_dir, 'price_distribution.png'))
    plt.show()

def plot_average_price_by_species(df):
    output_dir = '../Parth_Project/output'
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
    species_avg_price = df.groupby('Species').Price.mean().sort_values()
    species_avg_price.plot(kind='bar')
    plt.xlabel('Species')
    plt.ylabel('Average Price')
    plt.title('Average Price by Species')
    plt.savefig(os.path.join(output_dir, 'average_price_by_species.png'))
    plt.show()

def plot_price_vs_age(df):
    output_dir = '../Parth_Project/output'
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
    df['Age'] = df.Birthdate.apply(lambda x: (datetime.now() - x).days / 365)
    sns.scatterplot(data=df, x='Age', y='Price')
    plt.title('Price vs Age')
    plt.savefig(os.path.join(output_dir, 'price_vs_age.png'))
    plt.show()

def plot_age_distribution_by_species(df):
    output_dir = '../Parth_Project/output'
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist
    df['Age'] = df.Birthdate.apply(lambda x: (datetime.now() - x).days / 365)
    fig = px.box(df, x='Species', y='Age', title='Age Distribution by Species')
    fig.write_image(os.path.join(output_dir, 'age_distribution_by_species.png'))
    fig.show()
