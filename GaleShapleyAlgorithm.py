"""
Razie Hyria
Lab #1 - GS matching code
CMPSC 463
1/13/2022
"""

# creating employer rankings table
employerTable = {
            "Google"    : [["Lisa","Tom","Sarah","Bob","Jane"],[]],
            "Amazon"    : [["Sarah","Tom","Jane","Lisa","Bob"],[]],
            "Meta"      : [["Jane","Lisa","Bob","Tom","Sarah"],[]],
            "Apple"     : [["Jane","Bob","Tom","Sarah","Lisa"],[]],
            "Microsoft" : [["Bob","Tom","Sarah","Lisa","Jane"],[]]
                }

#creating employee rankings table
employeeTable = {
            "Lisa"  : ["Google","Amazon","Apple","Meta","Microsoft"],
            "Sarah" : ["Amazon","Apple","Meta","Google","Microsoft"],
            "Bob"   : ["Microsoft","Meta","Google","Apple","Amazon"],
            "Tom"   : ["Meta","Google","Apple","Amazon","Microsoft"],
            "Jane"  : ["Apple","Google","Amazon","Microsoft","Meta"]
                }


def isProposed(dict):
    pass


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
        w rejects m'''

if __name__ =="__main__":
    print(employeeTable,"\n")