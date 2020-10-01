def produce_summary(file, day): # Function definition accepting 2 parameters
    print(f"Day {day}") # This prints the day of the summary
    the_file = open(file) #opens the file using the argument passed to the function call
    for line in the_file: # For each line in this file
        line = line.rstrip() # This eliminates the extra white space at the end of each line.
        words = line.split('|') # This returns a list of words in each line, separated by "|"

        melon = words[0] # takes the first word of each line
        count = words[1] # takes the second word of each line 
        amount = words[2] # takes the third word of each line

        print(f"Delivered {count} {melon}s for total of ${amount}") #prints the results in the desired format on each line
    the_file.close() # closes the file

produce_summary("um-deliveries-20140520.txt", 2) #function call