import http.client
import json
import pandas as pd
import math

#Set the credentials and headers
key = '276eecc9-026b-4519-b031-91953b089386'
host = 'jooble.org'
pages = 6  # Number of pages to fetch (30 records per page)
jobs = [] #initialize an empty list to store all jobs

print("============================================")
print("=== DataDevQuest - 2025_06 - Beginner    ===")
print("=== Challenged by: Paula Muñoz           ===")
print("=== Solved by: Le Luu                    ===")
print("============================================")
print()
#iterate to each page
for page in range(pages):
    print(f"Extracting data from page {page + 1}:")

    connection = http.client.HTTPConnection(host)
    headers = {"Content-type": "application/json"}
    
    body = json.dumps({
        "keywords": "tableau",
        "location": "",
        "page": page
    })
    #Send the POST request
    connection.request('POST', f'/api/{key}', body, headers)
    #Get the response
    response = connection.getresponse()
    #Check the status
    print("Status:", response.status, response.reason)

    #Parse JSON and load data
    data = response.read().decode('utf-8')
    data_json = json.loads(data)

    #Store the data from the jobs
    jobs_data = data_json.get("jobs", [])
    #Store total records after extracting data
    total_records = data_json.get("totalCount")
    #Store the jobs_data into the jobs list
    jobs.extend(jobs_data)

    connection.close()

# Convert to DataFrame
job_df = pd.DataFrame(jobs)
job_df["id"] = job_df["id"].astype(str)
# Get the city and state from the location field
job_df["city"] = job_df['location'].str.extract(r'(.*)\,.*') #get everything at the front of comma
job_df['state'] = job_df['location'].str.extract(r'.*\,\s(\w+)') #get all chars after comma and the space

#Create a list of all states
abbreviation_to_name = {
    # https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States#States.

    "AL": "Alabama",
    "AR": "Arkansas",
    "AZ": "Arizona",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "IA": "Iowa",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "MA": "Massachusetts",
    "MD": "Maryland",
    "ME": "Maine",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MO": "Missouri",
    "MS": "Mississippi",
    "MT": "Montana",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "NE": "Nebraska",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NV": "Nevada",
    "NY": "New York",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VA": "Virginia",
    "VT": "Vermont",
    "WA": "Washington",
    "WI": "Wisconsin",
    "WV": "West Virginia",
    "WY": "Wyoming",
    # https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States#Federal_district.
    "DC": "District of Columbia",
}
#Join all the states together
state_df = pd.DataFrame(list(abbreviation_to_name.items()), columns=["abbr", "State Name"])
df = pd.merge(job_df,state_df, left_on='state', right_on='abbr',how='outer')

print("==============================================")
print(f"Total records to extract: {total_records}")
print(f"Total pages can fetch: {math.ceil(total_records/30)}")
print(f"Total jobs fetched: {len(df)}")
df.drop_duplicates(inplace=True)
notnull = df.dropna(subset=['id'])
print(f"Total jobs after removed duplicates: {len(notnull)}")
return df.to_dict(orient="list")