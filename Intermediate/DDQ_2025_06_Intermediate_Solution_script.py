import http.client
import json
import pandas as pd
import math

key = '276eecc9-026b-4519-b031-91953b089386'
host = 'jooble.org'
pages = 5  # Number of pages to extract
jobs = []  # Initialize job list

print("================================================")
print("=== DataDevQuest - 2025_06 - Intermediate    ===")
print("=== Challenged by: Paula Muñoz               ===")
print("=== Solved by: Le Luu                        ===")
print("================================================")
print()

#Handle error if enter invalid location or keyword
try:
    input_df = pd.DataFrame(_arg1)
    keyword = input_df['keyword'].iloc[0]
    location = input_df['location'].iloc[0]
except Exception as e:
    return {"error": f"Invalid Location or Keyword: {e}"}

#Iterate to each page
for page in range(pages):
    try:
        print(f"Extracting data from page {page + 1}: ")
        connection = http.client.HTTPConnection(host)
        headers = {"Content-type": "application/json"}

        body = json.dumps({
            "keywords": keyword,
            "location": location,
            "page": page
        })

        #Send the POST request
        connection.request('POST', f'/api/{key}', body, headers)
        #Get the response
        response = connection.getresponse()

        #Print the response status and reason
        print(f"Status {response.status}: {response.reason}")

        #Read and load data into data_json
        data = response.read().decode('utf-8')
        data_json = json.loads(data)

        #Store all the jobs data from json
        jobs_data = data_json.get("jobs", [])
        #Store the total records from the totalCount key value
        total_records = data_json.get("totalCount", 0)
        #Store each job into the jobs list
        jobs.extend(jobs_data)

        #Close the connection
        connection.close()

    except Exception as e:
        return {"error": f"Error on page {page + 1}: {e}"}

# Convert to DataFrame
df = pd.DataFrame(jobs)
# Convert the id type to string
df["id"] = df["id"].astype(str)
# Extract the city and state from location field
df["city"] = df['location'].str.extract(r'(.*)\,.*')
df['state'] = df['location'].str.extract(r'.*\,\s(\w+)')

print("==============================================")
print(f"Total records to extract: {total_records}")
print(f"Total pages can fetch: {math.ceil(total_records / 30)}")
print(f"Total jobs fetched: {len(df)}")
df.drop_duplicates(inplace=True)
print(f"Total jobs after removed duplicates: {len(df)}")

return df.to_dict(orient="list")