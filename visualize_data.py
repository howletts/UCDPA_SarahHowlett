import analyze_data as data
import matplotlib.pyplot as plt
import seaborn as sns


def get_lollipop_colours(df_col):
    # Example of using python list comprehsion
    colours = []
    [colours.append('r') if value == 'City' else colours.append('g') for value in df_col.to_list()]
    return colours


################
# Figure 1: Lollipop Chart plotting number of surfing venues per county'
################
df_surf = data.df_surf_per_cnty
fig, ax = plt.subplots(figsize=(20,16), dpi= 80)
lolly_colours = get_lollipop_colours(df_surf["Council"])
ax.vlines(x=df_surf["address_region"], ymin=0, ymax=df_surf["count_venue"], color=lolly_colours, alpha=0.7, linewidth=2)
scatter = ax.scatter(x=df_surf["address_region"], y=df_surf["count_venue"], s=75, color=lolly_colours, alpha=0.7)
ax.set_title('Figure 1: Lollipop Chart plotting number of surfing venues per county',
             fontdict={'size':22})
ax.set_ylabel('Number of venues you can surf, kitesurf and windsurf ')
ax.set_xticks(df_surf["address_region"])
ax.set_xticklabels(df_surf["address_region"], rotation=60, fontdict={'horizontalalignment': 'right', 'size':12})
ax.set_xlabel('Counties with surfing venues. Only counties in red have a city')
ax.set_ylim(0, df_surf["count_venue"].max() + 1)
plt.grid()
plt.show()
fig.savefig("./visualisations/lollipop_chart_surf_activities.png")
plt.close()


################
# For Figure 2: Bar plot subplots plotting number attractions per county for each province
################
df_all_provinces = data.df_agg_attractions
df_leinster = df_all_provinces[df_all_provinces["province"] == "Leinster"].sort_values("number_attractions", ascending=True)
df_munster = df_all_provinces[df_all_provinces["province"] == "Munster"].sort_values("number_attractions", ascending=True)
df_connacht = df_all_provinces[df_all_provinces["province"] == "Connacht"].sort_values("number_attractions", ascending=True)
df_ulster = df_all_provinces[df_all_provinces["province"] == "Ulster"].sort_values("number_attractions", ascending=True)
# Create subplots for each province
fig, ax = plt.subplots(2, 2, figsize=(16,10), dpi= 80)
fig.subplots_adjust(hspace=.5)

# Top left - plot count and number_attractions for Leinster
ax[0,0].bar(df_leinster.index, df_leinster["number_attractions"], color='r')
ax[0,0].tick_params(labelrotation=30)
ax[0,0].set_title('Figure 2a: Count of attractions per county in Leinster')
ax[0,0].grid()
# Top right - plot count and number_attractions for Munster
ax[0,1].bar(df_munster.index, df_munster["number_attractions"], color='g')
ax[0,1].tick_params(labelrotation=30)
ax[0,1].set_title('Figure 2b: Count of attractions per county in Munster')
ax[0,1].grid()
# Bottom left - plot count and number_attractions for Connacht
ax[1,0].bar(df_connacht.index, df_connacht["number_attractions"], color='b')
ax[1,0].tick_params(labelrotation=30)
ax[1,0].set_title('Figure 2c: Count of attractions per county in Connacht')
ax[1,0].grid()
# Bottom right - plot count and number_attractions for Ulster
ax[1,1].bar(df_ulster.index, df_ulster["number_attractions"], color='y')
ax[1,1].tick_params(labelrotation=30)
ax[1,1].set_title('Figure 2d: Count of attractions per county in Ulster')
ax[1,1].grid()
plt.show()
fig.savefig("./visualisations/bar_subplots_per_province.png")
plt.close()
#########

################
# For Figure 3: Histogram plotting number accommodation per county for all provinces
################
df_accommodation = data.df_accommodation
g = sns.displot(df_accommodation, x="AddressRegion", hue = "Province", aspect=50/20)
g.set_xticklabels(rotation=45)
plt.title('Figure 3: Histogram of observations (counts) of accommodations per county', y=0.95, fontsize = 16)
plt.show()
g.savefig("./visualisations/accommodation_per_county.png")
plt.close()
########

################
# For Figure 4: Scatter plots of attractions and accommodations in the same graph
################
fig, ax = plt.subplots(figsize=(20,20))
df_attractions_leinster = data.df_attractions_leinster
df_accommodation_leinster = data.df_accommodation_leinster

ax.scatter(df_attractions_leinster.index, df_attractions_leinster["number_attractions"], c = ['r'], label = 'attractions')
plt.xticks(rotation='45')
ax.scatter(df_accommodation_leinster.index, df_accommodation_leinster["number_attractions"], c = ['b'], label = 'accommodation')
plt.xticks(rotation='45')
ax.set_xlabel("Counties in Ireland - (AddressRegion)")
ax.set_ylabel("Counts")
plt.title('Figure 4: Scatter plots of attractions and accommodations counts', y=1, fontsize = 16)
plt.legend()
plt.grid()
plt.show()
fig.savefig("./visualisations/scatter_plot_aggregated_counts.png")
plt.close()

################
# For Figure 5: Scatter plot of correlation between attractions and accommodations
################

plt.style.use("ggplot")
plt.figure(figsize=(20,20))
plt.scatter(df_attractions_leinster["number_attractions"], df_accommodation_leinster["number_attractions"])
plt.title('Figure 5: Scatter plot of correlation between attractions and accommodations', y=1, fontsize = 16)
plt.xlabel("attractions")
plt.ylabel("accommodation")
plt.grid()
plt.savefig("./visualisations/scatter_plot_of_correlation.png")
plt.show()
plt.close()

