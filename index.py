from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_corporate_profits_and_losses'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

# find the table by its class name, wiki table class names are the same, "find" finds the first
table = soup.find('table', class_='wikitable sortable')

# check if the table is found (table class can be finicky in wikipedia)
if table is None:
    print("Table not found.")
else:
    # extract the table headers
    world_titles = table.find_all('th')
    world_table_titles = [title.text.strip() for title in world_titles]

    # create a DataFrame with extracted headers
    df = pd.DataFrame(columns=world_table_titles)

    # extract all rows from table
    column_data = table.find_all('tr')
    for row in column_data[1:]:
        row_data = row.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data]

        # append the data to the DataFrame
        length = len(df)
        df.loc[length] = individual_row_data
 
    # print(df.to_string())
    # print the DataFrame 
    print(df)
   
    # save as spreadsheet
    df.to_csv('largest_corporate_profits_and_losses.csv', index=False)


