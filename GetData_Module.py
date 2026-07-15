import csv 
# Function to get data from the CSV file
def GetData(filename):
    st_data = []
    try:
        with open (filename) as file:
            reader = csv.reader(file)
            next (reader) # skip the header row
            for row in reader:
                st_data.append(row)
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return st_data