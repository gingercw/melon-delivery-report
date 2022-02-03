
def melons_report (day, the_file):       ## creates a function that takes a file    
    print("Day", day)

    day_file = open(the_file)

    for line in day_file:           ## starts a for loop to go through each line in the file
        line = line.rstrip()        ## cleans each line from excessive characters
        words = line.split('|')     ## splits line into a list and list items are between the vertical lines

        melon = words[0]            ## assigns the first list item as melon
        count = words[1]            ## assigns the second list item as count
        amount = words[2]           ## assigns the third list item as amount

        print(f"Delivered {count} {melon}s for total of ${amount}")       ## prints the formatted output
    day_file.close()

melons_report(1, "um-deliveries-day-1.txt")

# print("Day 1")
# day_one = open("um-deliveries-day-1.txt")
# melons_report(day_one)
# day_one.close()

# print("Day 2")
# day_two = open("um-deliveries-day-2.txt")
# melons_report(day_two)
# day_two.close()

# print("Day 3")
# day_three = open("um-deliveries-day-3.txt")
# melons_report(day_three)
# day_three.close()