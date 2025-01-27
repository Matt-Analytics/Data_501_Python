import csv # Import csv to read and write csv files

transformed_data = [] # Create an empty list to write the transformed data to

with open('student_test_scores_extended(in).csv', mode='r') as reader:
    csv_reader = csv.DictReader(reader) # Use DictReader to read in rows as dictionaries

    columns = csv_reader.fieldnames

    columns_to_keep = [col for col in columns if "Score" in col or col == "Name"] # Create list of fieldnames we want to keep based on criteria given

    for row in csv_reader: # Loop through each row

        filtered_data = {i: row[i] for i in columns_to_keep} # Creating new row dictionaries with only the columns we want

        score_columns = [row[col] for col in columns_to_keep if "Score" in col] # Creates a list of score columns that will be used to compute the average score

        if score_columns:
            average_score = sum(int(score) for score in score_columns) / len(score_columns) # if the column in the data is a "score column" it will compute the average

        filtered_data['Average Score'] = average_score # Add the average_score column to the data

        transformed_data.append(filtered_data) # Append each row dictionary to the transformed data list

print(transformed_data)

with open('transformed_data.csv', mode="w", newline='') as writer:
    csv_writer = csv.DictWriter(writer, fieldnames=columns_to_keep + ['Average Score']) # Use DictWriter as each row is a dictionary

    csv_writer.writeheader()

    csv_writer.writerows(transformed_data)

