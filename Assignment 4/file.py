try:
    file1 = open('sample.txt', 'r')
    reading_file = file1.readlines()

    for i, line in enumerate(reading_file, start=1):
        print(f"line{i}: {line.strip()}")  # .strip() removes \n

    file1.close()

except FileNotFoundError:
    print("Error: the file sampl.txt not found..")
