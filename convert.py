import csv
import pickle

print("""Would you like to:
1 - Convert .csv to .dab
2 - Convert .dab to .csv""")
choice = input(">")
print()

if choice == "1":
    file = input("What csv file would you like to read?\n>")
    file += ".csv"
    name = input("What would you like to call your file?\n>")
    name += ".dab"

    with open(file) as csvf:
        a = csv.reader(csvf)
        b = [i for i in a if i != []]
        out_file = open(name,"wb")
        pickle.dump(b, out_file)
        print("dumped:\n" + str(b))
        out_file.close()
elif choice == "2":
    file = input("What dab file would you like to read?\n>")
    file += ".dab"
    name = input("What would you like to call your file?\n>")
    name += ".csv"

    in_file = open(file, "rb")
    data = pickle.load(in_file)
    new_data = [i for i in data if i != []]
    in_file.close

    with open(name, 'w') as csvf:
        writer = csv.writer(csvf)
        for row in data:  
            writer.writerow(row)
            print("added:", row)
else:
    print("Invalid Choice")
          
enter = input("Press Enter to Continue...")
