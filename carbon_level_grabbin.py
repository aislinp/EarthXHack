# farm fresh code for the Senate Stalker tool

from datapackage import Package # import Package
import datapackage              # import datapackage
import pandas as pd             #import pandas

# grabbing the url of the data
package = Package('https://datahub.io/core/co2-ppm-daily/datapackage.json')

# uncomment to print list of all resources:
#print(package.resource_names)


# read in all the relevant data
for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        co2_data = resource.read()

# turning the data into a dataframe
df = pd.DataFrame(co2_data)
# extracting today's carbon level (in ppm)
today_carbon_level = df.loc[(len(df)-1), 1]
