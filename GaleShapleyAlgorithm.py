"""
Razie Hyria
Lab #1 - GS matching code
CMPSC 463
1/13/2022
"""

'''
GS Algorithm

Initialize each person to be free.
while (some man is free and hasn't proposed to every woman) {
    Choose such a man m
    w = 1st woman on m's list to whom m has not yet proposed
    if (w is free)
        assign m and w to be engaged
    else if (w prefers m to her fiancé m')
        assign m and w to be engaged, and m' to be free
    else
        w rejects m

Resources:
https://www.youtube.com/watch?v=FhRf0j068ZA
'''

'''I was thinking of just adding two more list components to the dict and 
comparing the matches that way but im not sure if it would be more optimal'''

# creating employer rankings table
employerTable = {
            "Google"    : ["Lisa", "Tom", "Sarah", "Bob", "Jane"],
            "Amazon"    : ["Sarah", "Tom", "Jane", "Lisa", "Bob"],
            "Meta"      : ["Jane", "Lisa", "Bob", "Tom", "Sarah"],
            "Apple"     : ["Jane", "Bob", "Tom", "Sarah", "Lisa"],
            "Microsoft" : ["Bob", "Tom", "Sarah", "Lisa", "Jane"],
                }



#creating employee rankings table
employeeTable = {
            "Lisa"  : ["Google", "Amazon", "Apple", "Meta", "Microsoft"],
            "Sarah" : ["Amazon", "Apple", "Meta", "Google", "Microsoft"],
            "Bob"   : ["Microsoft", "Meta", "Google", "Apple", "Amazon"],
            "Tom"   : ["Meta", "Google", "Apple", "Amazon", "Microsoft"],
            "Jane"  : ["Apple", "Google", "Amazon", "Microsoft", "Meta"]
                }
# stores combo of people who are linked
currently_hired = []

# track which employer has not yet made an offer and was accepted
make_offer = []

# resets the active offer list and adds all the names of the employers
def making_offers():
    for employer in employerTable:
        make_offer.append(employer)


# start matchmaking algorithm
def start_matching():
    while(len(make_offer)> 0):
        for employer in make_offer:
            matchmaking(employer)

# match making (GS) algorithm
def matchmaking(employer):
    print('Finding %s a job!'%(employer))
    for employee in employerTable[employer]:
        
        # this will check to see if the employees name already appears in another match
        temp_match = [match for match in currently_hired if employee in match]
        
        #if the len is zero, then the employee doesnt have any outstanding matches/making_offers
        if (len(temp_match)==0): 
            currently_hired.append([employer,employee]) # in which case you append them both to hired list
            make_offer.remove(employer) # and remove the employer from making offers
            print('%s is no longer hiring! Congrats to Their new employee %s'%(employer,employee))
            # let the user know whos paired, and then exit when done
            break

        #however, if thats not the case, and they DO have an existing match; then the better offer wins
        elif (len(temp_match)>0):
            print('%s is taken! Lets see if we can switch things around... :'%(employee))

            # acess temp employer match to see where that current employee is ranked, by return their index in the list
            current_employer_rank = employeeTable[employee].index(temp_match[0][0])
            # we repeat the same process to get the index of the new employer from the employees list
            potentional_employer_rank = employeeTable[employee].index(employer)

            #now we compare and check to see if the current match is ranked higher (lower) than the potential match
            if (current_employer_rank < potentional_employer_rank):
                print('sorry! %s"s offers too good to pass up!'%(temp_match[0][0]))
            else:
                print('%s offer is better than %s! So hes making offers again!'%(employer,temp_match[0][0]))

               # remove the employer from making offers
                make_offer.remove(employer)
               
               # add the old employer back to making offers
                make_offer.append(temp_match[0][0])
                
                # reset current employer to new employer
                temp_match[0][0] = employer
                break 
            # and exit the loop

if __name__ =="__main__":
    making_offers()
    start_matching()
    print("Matches Complete :)\n")
    print(currently_hired)