import pet_analysis as pa

# Load and clean the data
df = pa.load_data('../Parth_Project/pets.csv')
df = pa.clean_data(df)

# Calculate average price for a given species
species = 'Dog'
avg_price = pa.calculate_average_price(df, species)
print(f"Average price for {species}: {avg_price}")

# Find pets with a specific feature
feature = 'Blood Type'
pets_with_feature = pa.find_pets_with_feature(df, feature)
print(f"Pets with feature {feature}: {pets_with_feature}")

# Get species statistics
species_stats = pa.get_species_statistics(df)
print("Species Statistics:", species_stats)

# Plot price distribution
pa.plot_price_distribution(df)

# Plot average price by species
pa.plot_average_price_by_species(df)

# Plot price vs age
pa.plot_price_vs_age(df)

# Plot age distribution by species
pa.plot_age_distribution_by_species(df)
