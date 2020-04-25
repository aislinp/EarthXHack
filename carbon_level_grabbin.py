# farm fresh code for the Senate Stalker tool

from datapackage import Package # import Package
import datapackage              # import datapackage
import pandas as pd             #import pandas
from datetime import datetime
from dateutil.parser import parse

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

today_date = str(df.loc[(len(df)-1), 0])
today_date = datetime.strptime(today_date, '%Y-%m-%d')
s = pd.Series(pd.date_range(today_date) '''needs more parameters added''')
s.dt.is_month_start()
#monthstart = s.dt.is_month_start()
#monthend = s.dt.is_month_end()


'''
month1 = []
month2 = []

if monthstart.loc[(len(monthstart)-1), 1] == True:
    if len(month1) > 0:
        month2.append(today_carbon_level)
    else:
        month1.append(today_carbon_level)
elif monthend.loc[(len(monthend)-1), 1] == True:
    if len(month2) > 0:
        month2.append(today_carbon_level)
        # Averages/Tweet TODO
    else:
        month1.append(today_carbon_level)
else:
    if len(month2) > 0:
        month2.append(today_carbon_level)
    else:
        month1.append(today_carbon_level)
'''
