"""
Razie Hyria
Lab #1 - GS matching code
CMPSC 463
1/13/2022
"""
from timeit import default_timer as timer
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
https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm
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
# also tracks
make_offer = []

# resets the active offer list and adds all the names of the employers
def making_offers():
    for employer in employerTable:
        make_offer.append(employer)

# resets the make offer list to add all the names of the employees actively searching
# used for setting employees as'proposer'
def looking_for_offers():
    for employee in employeeTable:
        make_offer.append(employee)

# start matchmaking algorithm
def start_matching(proposer): # initlize matching based off whos asking to "propose"
    while(len(make_offer)> 0): # while there are names in the offer list, seeking job/employee
        for proposer in make_offer:
            matchmaking(proposer) #sends over first name from making offers table


# match making (GS) algorithm
def matchmaking(proposer):
    #initialize free variables used to control what gets accessed depending on whos proposing
    who = proposer

    # changing the details depening on who we assign as proposer
    if who in employeeTable.keys():
        rankings = employerTable
        proposee = "employer"
        proposers_ranking = employeeTable

    else:
        rankings = employeeTable
        proposee = "employee"
        proposers_ranking = employerTable

    #print(who,"\nmatching table", rankings,"\n\nproposee =",proposee, "\n\nproposers table=", proposers_ranking)
    print('\nWorking with %s!...'%(proposer))

    for proposee in proposers_ranking[proposer]:
        print('\nproposer: %s and proposee: %s!'%(proposer,proposee))
        # this will check to see if the employees name already appears in another match
        temp_match = [match for match in currently_hired if proposee in match]
        
        #if the len is zero, then the employee doesnt have any outstanding matches/making_offers
        if (len(temp_match)==0): 
            currently_hired.append([proposer,proposee]) # in which case you append them both to hired list
            make_offer.remove(proposer) # and remove the employer from making offers
            print('%s is matched! Congrats to their new partnership with %s'%(proposer,proposee))
            # let the user know whos paired, and then exit when done
            break

        #however, if thats not the case, and they DO have an existing match; then the better offer wins
        elif (len(temp_match)>0):
            print('%s is taken! Lets see if we can switch things around...'%(proposee))

            # acess temp employer match to see where that current employee is ranked, by return their index in the list
            current_proposer_rank = rankings[proposee].index(temp_match[0][0])
            # we repeat the same process to get the index of the new employer from the employees list
            potentional_proposer_rank = rankings[proposee].index(proposer)

            #now we compare and check to see if the current match is ranked higher (lower) than the potential match
            if (current_proposer_rank < potentional_proposer_rank):
                print('sorry! %s"s offers too good to pass up!'%(temp_match[0][0]))
            else:
                print('%s offer is better! So %s is unmatched again!'%(proposer,temp_match[0][0]))

               # remove the employer from making offers
                make_offer.remove(proposer)
               
               # add the old employer back to making offers
                make_offer.append(temp_match[0][0])
                
                # reset current employer to new employer
                temp_match[0][0] = proposer
                break 
            # and exit the loop



if __name__ =="__main__":
    proposer = 'employer'
    making_offers()
    start = timer()
    start_matching(proposer)
    end = timer()
    print("\nMatches Complete :")
    print(currently_hired)
    print("\nEmployers elapsed time: ", end - start)

    currently_hired = [] #resetting list of matches to zero in order to add matches from different proposer
    prop = "employee"
    looking_for_offers()
    start = timer()
    start_matching(prop)
    end = timer()
    print("Matches Complete :)\n")
    print(currently_hired)
    print("Employees elapsed time: ", end - start)
