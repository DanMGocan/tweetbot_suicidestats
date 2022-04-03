import csv
import math

csvPath = "data/data.csv"
data_dict = []

def convert_data(data_path):
    with open(data_path) as csvFile:
        csvReader = csv.DictReader(csvFile)

        for row in csvReader:

            # Converting the Both sexes / Male / Female strings to integers

            both_sexes = float(row["Both sexes"][:row["Both sexes"].index("[")].replace(",", "."))
            male = float(row["Male"][:row["Male"].index("[")].replace(",", "."))
            female = float(row["Female"][:row["Female"].index("[")].replace(",", "."))

            if both_sexes <= 1 or male <= 1 or female <= 1:
                continue

            else:

                new_entry = {
                    "country": row["Country"],
                    "year": int(row["Year"]),
                    "both_sexes": int(math.ceil(both_sexes)),
                    "male": int(math.ceil(male)),
                    "female": int(math.ceil(female))
                }

            # Option to write all dictionaries to file, for verification purpose    
            # with open('data_dict.py', 'a') as f:
            #     f.write(str(new_entry))

            data_dict.append(new_entry)
    
    return data_dict

all_data = convert_data(csvPath)