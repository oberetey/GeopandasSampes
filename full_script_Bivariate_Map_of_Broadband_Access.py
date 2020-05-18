# in this script we want to map two variables at once, a so-called bivariate map. 
# One way to do this is by combining a choropleth map and a proportional symbol map.

# Remember that choropleth maps should show rates or proportions, not counts. 
# After loading the data, you will calculate the percentage of households 
# with no internet access, using columns no_internet and total households.

# Import geopandas using the alias gpd
import geopandas as gpd
import matplotlib.pyplot as plt




# Use the read_file method of geopandas 
# To load the file "states_internet.gpkg"
# Load geospatial data
geo_state = gpd.read_file("states_internet.gpkg")

# if this is accessible at the census site here are the column names,
# geometry will need to be made as well.
col_names = ['state', 'postal', 'name', 'total', 'internet', 'dial_up',
             'broadband', 'satellite', 'other_service', 'internet_without_subscription',
             'no_internet', 'label_x', 'label_y', 'geometry']

# View GeoDataFrame columns
print(geo_state.columns)

# Calculate the percentage of households with no internet access as
# 100 times the number of households with no_internet, divided by the total
# Calculate percent of households with no internet
geo_state["pct_no_internet"] = 100 * (geo_state["no_internet"] / geo_state["total"])

# Create a choropleth map of this percentage by setting the column parameter 
# To the name of the new column; 
# Set the colormap (cmap parameter) to "YlGnBu"
# Create choropleth map using YlGnBu colormap
geo_state.plot(column = "pct_no_internet", cmap="YlGnBu")
plt.show()


 
# You will use the geo_state GeoDataFrame again to create a choropleth of 
# the percentage of internet households with broadband access, 
# and overaly a proportional symbol map of the count of households with internet access.

# You will set an alpha transparency on the proportional symbol marker 
# so as to not completely obscure the underlying choropleth.

# geopandas is imported using the usual alias, 
# and the sqrt function has been imported from numpy.

# The geo_state GeoDataFrame has been loaded.



# Create point GeoDataFrame at centroid of states
geo_state_pt = geo_state.copy()
geo_state_pt["geometry"] = geo_state_pt.centroid

# Calculate percentage of internet households with broadband
# Use the broadband and internet columns to 
# calculate the percentage of internet households with broadband
geo_state["pct_broadband"] = 100 * geo_state["broadband"] / geo_state["internet"]

# Set choropleth basemap
#Create a choropleth basemap of the new pct_broadband column using a yellow-green-blue colormap
basemap = geo_state.plot(column = "pct_broadband", cmap = "YlGnBu")

# Plot transparent proportional symbols on top of basemap
# the basemap is passed to the variable ax
# Set the markersize of the centroid points to
# the square root of the number of households with internet access divided by 5; 
# make the markers partially transparent by setting the alpha parameter to 0.7
geo_state_pt.plot(ax = basemap, markersize = (sqrt(geo_state["internet"]) / 5), color = "lightgray", edgecolor = "darkgray", alpha=0.7)
plt.show()
