import import_data as data
import pandas as pd
import numpy as np

df_surf_act = data.df_surf_activities
df_attractions = data.df_attractions
df_accommodation = data.df_accommodation
df_county_in_province = data.df_county_province
# Having sorted the DataFrame, iloc is used as the exact rows and cols of interest are known
df_region_type = data.df_area_type.sort_values('Council').iloc[5:10,1:3]


# reusable function to extract the value of the 'addressRegion' from a dictionary
def extract_region(address):
    address_region = address['addressRegion']
    return address_region


# reusable function to create a dictionary from a DataFrame and lookup the dictionary using the region passed as the key
def get_province(value):
    province_lkup = df_county_in_province.to_dict()['province']
    return province_lkup[value]

def get_lollipop_colours(df_col):
    # Example of using python list comprehsion
    colours = []
    [colours.append('r') if value == 'City' else colours.append('g') for value in df_col.to_list()]
    return colours


########################################
#  1. Analyse and process the activities dataset, specifically for venues suitable for all 3 surfing types
########################################
# extract the 'address_region' (county) from the 'address' column using a reusable custom function, add as new column
df_surf_act['address_region'] = df_surf_act['address'].apply(extract_region)
# sort the data by 'name' and 'address_region' (county) in ascending order
df_surf_act = df_surf_act.sort_values(['name', 'address_region'], ascending=True)
# remove records that are duplicate on 'name' and 'address_region', where there are many keep the last
df_surf_act = df_surf_act.drop_duplicates(['name', 'address_region'], keep='last')
# use .loc to select 'name', 'address_region', 'tags' columns only
df_surf_act = df_surf_act.loc[:, ['name', 'address_region', 'tags']]
# count the number of rows per 'address_region' (county) and save in a new dataframe df_surf_venue_per_region
df_surf_venue_per_region = df_surf_act.groupby(['address_region'], as_index=False).agg(count_venue=pd.NamedAgg(column='name', aggfunc='count'))
# left join with the df_region_type DafaFrame which contains a list of counties that have cities, use columns with different names to join on
df_surf_per_cnty = df_surf_venue_per_region.merge(df_region_type, how = 'left', left_on=['address_region'], right_on=['Core County'])
# there are only 5 counties with cities so fill the empty fields with the value 'No City'
df_surf_per_cnty[['Council']] = df_surf_per_cnty[['Council']].fillna(value = 'No City')

########################################
#  2. Analyse and process the attractions dataset
########################################

# drop records with duplicate 'Name' and 'AddressRegion', keep lats record in case of duplicates
df_attractions = df_attractions.drop_duplicates(['Name', 'AddressRegion'], keep='last')
# drop records that don't have an 'AddressRegion' as this field is needed for analysis
df_attractions = df_attractions.dropna(subset = ['AddressRegion'])
# fill any other empty cells in the other columns with 'Unknown'
if df_attractions.isnull().values.any():
    df_attractions = df_attractions.fillna(value = 'Unknown')
# select only the 'Name', 'AddressRegion', 'Tags' columns using the .loc
df_attractions = df_attractions.loc[:, ['Name', 'AddressRegion', 'Tags', 'Url', 'Telephone']]
# sort the dataframe by 'Name', 'AddressRegion'
df_attractions = df_attractions.sort_values(['Name', 'AddressRegion'], ascending=True)
# Get any 'Name'/'AddressRegion' pair dups and remove them if they exist keeping the last record
df_attractions = df_attractions.drop_duplicates(['Name', 'AddressRegion'], keep='last')
# groupby 'AddressRegion' and get the count per County ('AddressRegion'), has index as default so keep it
df_agg_attractions = df_attractions.groupby(['AddressRegion']).agg(number_attractions=pd.NamedAgg(column='Name', aggfunc='count'))
# set the index to 'county' in df_county_in_province for joining efficiency
df_county_in_province = df_county_in_province.set_index('county')
# left join the df_attractions_count and df_county_in_province so every row on df_attractions_count remains
df_agg_attractions = df_agg_attractions.merge(df_county_in_province, how = 'left', left_index = True, right_index = True)

########################################
#  Analyse and process data for figure 3
########################################

# drop duplicates
df_accommodation = df_accommodation.drop_duplicates(["Name", "AddressRegion"], keep='last')
# drop records that don't have an "AddressRegion" set, this field is needed for analysis
df_accommodation = df_accommodation.dropna(subset = ["AddressRegion"])
# select only the "Name", "AddressRegion", "Tags" columns using the .loc
df_accommodation = df_accommodation.loc[:, ["Name", "AddressRegion"]]
# sort the dataframe
df_accommodation = df_accommodation.sort_values(["Name", "AddressRegion"], ascending=True)
# groupby "AddressRegion" and get the count (Name column) per County ("AddressRegion"), has index as default
df_accommodation["Province"] = df_accommodation["AddressRegion"].apply(get_province)

########################################
#  Analyse and process data for figure 4
########################################

df_agg_accommodation = df_accommodation.groupby(["AddressRegion"]).agg(number_attractions=pd.NamedAgg(column="Name",
                                                                            aggfunc="count"))
df_agg_accommodation = df_agg_accommodation.merge(df_county_in_province, how = 'left', left_index = True, right_index = True)


df_attractions_leinster = df_agg_attractions[df_agg_attractions["province"] == "Leinster"]
df_accommodation_leinster = df_agg_accommodation[df_agg_accommodation["province"] == "Leinster"]

# use numpy to check for correlation between the lists - 0.97128864 means it is a strong positive correlation
np.corrcoef(df_attractions_leinster["number_attractions"], df_accommodation_leinster["number_attractions"])

# use numpy to
dict_accommod_percent = {}
total = np.sum(df_agg_accommodation["number_attractions"])
array_accommod_counts = np.array(df_agg_accommodation["number_attractions"])

array_accommod_percent = np.rint(((array_accommod_counts * 100) / total)).tolist()
counties =  (df_agg_accommodation.index).tolist()
for i, item in enumerate(counties):
    dict_accommod_percent[item] = array_accommod_percent[i]

a = 0



