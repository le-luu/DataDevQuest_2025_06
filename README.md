# DataDev Quest Challenge 2025_06

![image](https://github.com/le-luu/DataDevQuest_2025_03/blob/main/img/logo.svg)

### Challenged By: 
Paula Muñoz

### Objective
- Connect Tableau Desktop to Python using Table Extensions
- Use Python to fetch live job data via the API
- Clean and enrich the data within Python Script (e.g., split City and State from the job location)
- Return the data to Tableau to build simple visualizations
- Build an interactive Tableau Dashboard with dynamic parameters
- Fetch live job data based on the user's input in parameters

### Solution Video

### Beginner Challenge
Link to the Beginner Challenge: https://datadevquest.com/ddq2025-06-tableau-table-extensions-job-search-api-beginner/

**Solution Expectation:**

**Part 1:** Update and Extend the Python Script
- Fix ‘id’ and ‘salary’ Issues in Tableau
- Import at Least 120 Job Records
- Update Python Script to extract City and State from the Location Field
- 
**Part 2:** Create a Tableau Dashboard

**Output**

![image](https://github.com/le-luu/DataDevQuest_2025_06/blob/main/img/DDQ_2025_06_Beginner_Solution_Script_img.png)

The Python script to apply in the Table Extension in Tableau Desktop. After setting the API key, number of pages, and initialize the jobs list. Iterate to each page to fetch the data (by default, each page shows 30 records), parse JSON. Then, convert the id data type to string and extract the city and state from the location field. To build the dashboard later, I need to build the U.S. map, so I added 50 U.S. states to join them with the data from API. I also test the data by looking at the response status, number of pages can fetch, number of records before/after removing duplicates.

![image](https://github.com/le-luu/DataDevQuest_2025_06/blob/main/img/DDQ_2025_06_Beginner_cmd_output.png)

Check the data after fetching. 

![image](https://github.com/le-luu/DataDevQuest_2025_06/blob/main/img/DDQ_2025_06_Beginner_Dashboard.png)

Finally, build an interactive dashboard. The user can drill down the map to get the number of jobs in each state and city. The lollipop chart will show the trend line when the jobs were posted. The table at the bottom will list all the jobs for each state, city, company, posted date, salary. If the user click on the title of the job, it will link to the job description page on jooble.org.

### Intermediate Challenge
Link to the Intermediate Challenge: https://datadevquest.com/ddq2025-06-tableau-table-extensions-dynamic-job-search-with-parameters-and-duckdb-intermediate/

**Solution Expectation:**

**Part 1:** Update the Python Script from the beginner challenge to call Jooble API with the dynamic ‘keyword’ and ‘location’ parameters
- Incorporate the dynamic keyword and location parameters to dynamically fetch data from the Jooble API.
- Fix ‘id’ and ‘salary’ Issues in Tableau
- Import at Least 120 Job Records
- Update Python Script to extract City and State from the Location Field
**Part 2:** Create a Tableau Dashboard

**Output**

![image](https://github.com/le-luu/DataDevQuest_2025_06/blob/main/img/DDQ_2025_06_Intermediate_Solution_Script_img.png)

The Python script to apply in the Table Extension in Tableau Desktop. The Python code is mostly same as the Beginner solution above. The difference is the keyword and location at line 21 and 22. Now, those parameters are dynamic. It will get the input from the user via the parameters in Tableau Desktop. 

![image](https://github.com/le-luu/DataDevQuest_2025_06/blob/main/img/DDQ_2025_06_Intermediate_cmd_output.png)

Check the data 

![image](https://github.com/le-luu/DataDevQuest_2025_06/blob/main/img/DDQ_2025_06_Intermediate_Dashboard.png)

The dashboard for Intermediate challenge. The difference here is the map. It shows the total jobs of the location and each city. If the user clicks on each city, it will filter the other charts.

### Instructions
- You need to install Python in your local computer first
- For this repository and clone it to your local computer
- Open the Command Prompt (for Windows) and Terminal (for Mac), change the directory to the DataDevQuest_2025_05
    ```
    cd DataDevQuest_2025_06
    ```
- Install and activate the virtual environment
    ```
    pip install virtualenv
    virtualenv venv
    venv\Scripts\activate
    ```    
- Install the packages in the Command Prompt
    ```
    pip install -r requirements.txt
    ```
    It may takes a few seconds to install all packages:
    - pandas
    - requests
    - tabpy
    - duckdb
- To run connect to the duckdb database, you need to download and copy the JAR file to your local computer. Check this docs: https://duckdb.org/docs/stable/guides/data_viewers/tableau.html
- Activate tabpy by typing tabpy in the Command Prompt or Terminal, press y and enter.

**Beginner Challenge**
  
- In the Beginner folder, open Le_DDQ_2025_06_Beginner_Dashboard.twb file.
- Go to Help > Settings and Performance > Manage Analytics Extension Connection ...
    - Check the host name and port number
    - If you run tabpy on your local computer, hostname is localhost and port number is 9004
- Go to the Datasource tab, double click to the Table Extension. Then, put your API key from jooble.org into the variable key
- Click apply and test the dashboard

**Intermediate Challenge**

- Open the Command Prompt or the Terminal, change the directory to Intermediate folder and run the duckdb_input Python script to create the keywords.duckdb
    ```
    cd DataDevQuest_2025_06
    python duckdb_input.py
    ```
- Open Le_DDQ_2025_06_Intermediate_Dashboard.twb file, click on the DataSource tab
- Change the directory of the duckdb file in Connections (Right click on jdbc:duckdb line and choose Edit Connections)
    - The directory looks like this: jdbc:duckdb:/Users/<Your_username>/Documents/.../DataDevQuest_Challenges/2025_06/Intermediate/keywords.duckdb
- Double Click on the Table Extension, change the API key
- Click apply and test the dashboard
