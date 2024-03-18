import csv

# Path to the text file
text_file_path = "Bangla Emotion-Messaage List-1.txt"

# Path to the CSV file
csv_file_path = "output.csv"

# Open the text file and CSV file
with open(text_file_path, "r", encoding="utf-8") as file, open(csv_file_path, "w", newline="",
                                                               encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["emotion", "message"])  # Write column headers

    # Read each line of the text file
    for line in file:
        # Split the line into emotion and message
        emotion, message = line.strip().split(" ", 1)

        # Write emotion and message to CSV file
        csv_writer.writerow([emotion, message])

print("CSV file created successfully.")
