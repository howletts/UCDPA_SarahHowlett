import analyze_data as data
import matplotlib.pyplot as plt

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