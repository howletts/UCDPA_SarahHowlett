import analyze_data as data
import matplotlib.pyplot as plt
import seaborn as sns

df_surf = data.df_surf_per_cnty


def get_lollipop_colours(df_col):
    # Example of using python list comprehsion
    colours = []
    [colours.append('r') if value == 'City' else colours.append('g') for value in df_col.to_list()]
    return colours


fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
lolly_colours = get_lollipop_colours(df_surf["Council"])
ax.vlines(x=df_surf["address_region"], ymin=0, ymax=df_surf["count_venue"], color=lolly_colours, alpha=0.7, linewidth=2)
ax.scatter(x=df_surf["address_region"], y=df_surf["count_venue"], s=75, color=lolly_colours, alpha=0.7)
ax.set_title('Figure 1: Lollipop Chart plotting number of surfing venues per county', fontdict={'size':22})
ax.set_ylabel('Count of venues you can surf, kitesurf and windsurf')
ax.set_xticks(df_surf["address_region"])
ax.set_xticklabels(df_surf["address_region"], rotation=60, fontdict={'horizontalalignment': 'right', 'size':12})
ax.set_ylim(0, df_surf["count_venue"].max() + 1)
plt.show()
fig.savefig("./data/surf_venue_count_per_region.png")
plt.clf()


# Draw Stripplot
fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
sns.stripplot(df_surf["address_region"], df_surf["count_venue"], ax=ax)

plt.show()

plt.clf()

# Create a regression plot
#sns.lmplot(data=data.df_surf_per_cnty,
#           x="address_region",
#           y="count_venue")


# Create a PairGrid with a scatter plot for fatal_collisions and premiums
g = sns.PairGrid(df_surf, vars=["address_region", "count_venue"])
g2 = g.map(plt.scatter)

plt.show()
plt.clf()

# Create a boxplot
sns.boxplot(data=df_surf,
         x='address_region',
         y='count_venue')

plt.show()
#plt.clf()

# Remove the spines
sns.despine(top = True, right = True)

# Show the plot and clear the figure
plt.show()
plt.clf()

# Create a regression plot using hue
sns.lmplot(data=df,
           x="insurance_losses",
           y="premiums",
           hue="Region")

# Show the results
plt.show()



df_munster = data.df_attractions_munster.sort_values("number_attractions", ascending=True)
#df_leinster = data.df_attractions_leinste
fig, ax = plt.subplots()
# Plot counties from df_munster against the number_attractions there
ax.plot(df_munster.index, df_munster["number_attractions"], color='b', marker='o', linestyle='None')
plt.show()
fig.savefig("./data/df_munster.png")

# Plot counties from df_munster against the number_activites there
#ax.plot(df_munster["county"], df_munster["number_attractions"])
#plt.show()


df_all_provinces = data.df_attractions_per_cnty
df_leinster = df_all_provinces[df_all_provinces["province"] == "Leinster"].sort_values("number_attractions", ascending=True)
df_munster = df_all_provinces[df_all_provinces["province"] == "Munster"].sort_values("number_attractions", ascending=True)
df_connacht = df_all_provinces[df_all_provinces["province"] == "Connacht"].sort_values("number_attractions", ascending=True)
df_ulster = df_all_provinces[df_all_provinces["province"] == "Ulster"].sort_values("number_attractions", ascending=True)
# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)
# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(df_leinster.index, df_leinster["number_attractions"], color='r', marker='o', linestyle='None')

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(df_munster.index, df_munster["number_attractions"], color='r', marker='o', linestyle='None')

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1, 0].plot(df_connacht.index, df_connacht["number_attractions"], color='r', marker='o', linestyle='None')

# In the bottom right (1, 1) plot month and Austin temperatures
ax[1, 1].plot(df_ulster.index, df_ulster["number_attractions"], color='r', marker='o', linestyle='None')
plt.show()


# attraction with most tags in Dublin
# county with most activities in each province

#compare percentage of unknown phone numbers per county
#compare percentage of unknown urls numbers per county

a = "end"
# Plot first column of df
#pd.DataFrame.hist(df.ix[:, 0:1])
#plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
#plt.ylabel('count')
#plt.show()