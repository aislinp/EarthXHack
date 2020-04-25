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

df[2] = df[0]

df[3] = df[2]

for i in range(len(df[2])):

    date = str(df.loc[i, 2])

    date = datetime.strptime(date, '%Y-%m-%d')

    s = pd.Series(pd.date_range(date, periods = 1))


    is_start = s.dt.is_month_start

    df.at[i, 2] = is_start[0]


    is_end = s.dt.is_month_end

    df.at[i, 3] = is_end[0]

today_date = str(df.loc[(len(df)- 1), 0])
today_carbon_level = df.loc[(len(df)- 1), 1]




month1 = []
month2 = []

if df.loc[(len(df)- 1), 2] == True:
    if len(month1) > 0:
        month2.append(today_carbon_level)
    else:
        month1.append(today_carbon_level)
elif df.loc[(len(df)- 1), 3] == True:
    if len(month2) > 0:
        month2.append(today_carbon_level)
        # Tweet TODO
        month1avg = mean(month1)
        month2avg = mean(month2)
        if month2 > month1:
            # sad tweet
        else:
            # happy tweet
    else:
        month1.append(today_carbon_level)
else:
    if len(month2) > 0:
        month2.append(today_carbon_level)
    else:
        month1.append(today_carbon_level)


