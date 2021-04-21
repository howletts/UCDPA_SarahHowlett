import import_data as data
import pandas as pd

df_attractions = data.df_attractions
df_accomodation = data.df_accomodation
df_activities = data.df_activities
df_county_in_provence = data.df_county_province
df_region_type = data.df_area_type

# create a reusable function to extract the value of the 'addressRegion' from a dictionary
def extract_region(address):
    address_region = address['addressRegion']
    return address_region

# get distinct tags in tag list
def count_tags(tags):
    #tags = ['Accommodation', 'Hotel', 'Follow the Shamrock', 'Standard', 'Covid Safety Charter', 'Visit Dublin']
    dist_tag_count = len(list(set(tags)))
    return dist_tag_count

# extract the address_region from the 'address' column for joining
df_activities['address_region'] = df_activities['address'].apply(extract_region)
df_accomodation['address_region'] = df_accomodation['address'].apply(extract_region)

# sorting by "Name" first and then region "AddressRegion" and populate the df_attractions DataFrame
df_attractions = df_attractions.sort_values(["Name", "AddressRegion"], ascending=True)
df_activities = df_activities.sort_values(["Name", "AddressRegion"], ascending=True)
df_accomodation = df_accomodation.sort_values(["Name", "AddressRegion"], ascending=True)

# drop duplicates
df_attractions = df_attractions.drop_duplicates(["Name", "AddressRegion"], keep='last')
df_activities = df_activities.drop_duplicates(["Name", "AddressRegion"], keep='last')
df_accomodation = df_accomodation.drop_duplicates(["Name", "AddressRegion"], keep='last')

##fill na,

## call count_tags

# select only the "Name", "AddressRegion", "Tags" columns using the .loc
df_attractions = df_attractions.loc[:, ["Name", "AddressRegion", "Tags"]]

# groupby "AddressRegion" and get the count (Name column) per County ("AddressRegion")
df_attractions_per_cnty = df_attractions.groupby(["AddressRegion"]).agg(number_attractions=pd.NamedAgg(column="Name", aggfunc="count"))
df_accomodation_per_cnty = df_accomodation.groupby(["AddressRegion"]).agg(number_accomdations=pd.NamedAgg(column="Name", aggfunc="count"))
# check if the County ("AddressRegion") is the index
print(df_attractions_per_cnty.index)

# add a county column for joining
df_activities['county'] = df_activities['address'].apply(extract_region)

# set the index to "county"
df_county_in_provence = df_county_in_provence.set_index("county")

# merge the df_attractions_count and df_county_in_provence so every row on df_attractions_count remains on index
df_attractions_per_cnty = df_attractions_per_cnty.merge(df_county_in_provence, how = 'left', left_index = True, right_index = True)

# Get any "Name"/"AddressRegion" pair dups and remove them if they exist keeping the last record
##df_dup_attractions = df_attractions[df_attractions.duplicated(["Name", "AddressRegion"], keep=False)]
#if not df_dup_attractions.empty:
#    print("Attractions that are duplicated in the list" + str(df_dup_attractions))


# For insight 1:
df_attractions_munster = df_attractions_per_cnty[df_attractions_per_cnty["province"] == "Munster"]
df_attractions_leinster = df_attractions_per_cnty[df_attractions_per_cnty["province"] == "Leinster"]
df_attractions_connacht= df_attractions_per_cnty[df_attractions_per_cnty["province"] == "Connacht"]
df_attractions_ulster = df_attractions_per_cnty[df_attractions_per_cnty["province"] == "Ulster"]






df_region_type = df_region_type.sort_values(["Council"], ascending=True)
df_region_type = df_region_type.reset_index(drop=True)
# Slice in both directions, the first 3 columns and rows 5-9 to get counties that contain a city
df_cities = df_region_type.iloc[5:10,0:3]

#create dictionary from dup_attractions datafrome

#.is_unique



# order by province
#for activities take a dictiry and extract a region - put as column

#attractions get count of attractions per regoin
#attractions per province
#attractions per is city to no is city
#city.sort_index(axis=1, inplace=True)