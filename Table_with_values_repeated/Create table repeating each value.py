# Create base datatable, with dates, brazilian state and product, for a report
# This code repeats each value of column A for each value of column B and C
# This code was created to use in Power BI as a Python Query

import pandas as pd
import datetime


# Creates fixed lists and variable
states = [
    "AC", "AM", "AP", "PA", "RO", "RR", "TO", "AL",
    "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE",
    "GO", "MS", "MT", "ES", "MG", "RJ", "SP", "PR",
    "RS", "SC", "DF", "GO+DF"
]
monthnum = [
    "01", "02", "03", "04", "05", "06", "07", "08",
    "09", "10", "11", "12"
]
products = ["Corn", "Soybean"]
thisyear = datetime.date.today().year
newlist = []

# Creates a changing list of dates (first day of month), from year-1 to year+1
months = []

for i in range(36):
    if i <= 11:
        months.append("01/" + monthnum[i] + "/" + str(thisyear - 1))
    elif i <= 23:
        months.append("01/" + monthnum[i - 12] + "/" + str(thisyear))
    else:
        months.append("01/" + monthnum[i - 24] + "/" + str(thisyear + 1))

# Creates a new list. Each data is replicated to all states, each state is
# replicated to all products
for month in range(0, len(months)):
    for state in range(0, len(states)):
        for product in range(0, len(products)):
            newlist.append([months[month], states[state], products[product]])

# Creates the dataframe on Pandas, to upload to PowerBI
df = pd.DataFrame(
    newlist,
    columns=["months", "states", "products"]
)

df
