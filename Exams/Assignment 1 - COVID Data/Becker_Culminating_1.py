import sys

"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

### YOUR CODE HERE ###

# turn the data into something i can work with better using the function given.
#actual data for the project
data = parse_nyt_data('data/covid/us-counties.csv')

#data for testing (hawaii data)
#data = parse_nyt_data("\Users\nateb\OneDrive\Documents\GitHub\ENGR315-fa2026-student\data\covid\us-counties-Hawaii-Alaska.csv")


#Question 1: When was the first positive COVID case in Harrisonburg? When was the first positive case in Rockingham County?

#find the length of the data to use in loops
Length = len(data)

#set veriables to count with and know if the first case has been found, boolen and int
HCounter=0
founditH = False
RCounter=0
founditR = False

# both blocks below function the same but are focused on different counties. 
# the loops first check if the counter variable is below the length of the list and if the first case has already been found.
# the if statement checks if there was atleast one case of covid and if it is in the desired county
# if it finds a case it prints the date of the case and changes the boolean for first case to true so the loop ends and doesnt keep looking for and printing case dates
# finally outside of the if statement the counter/index variable goes up one to move the next search down one row

while HCounter < Length and founditH == False:
    if data[HCounter][4] > 0 and data[HCounter][1] == "Harrisonburg city":
        print("Harrisonburgs first case was on " + data[HCounter][0])
        founditH = True
    HCounter = HCounter + 1


while RCounter < Length and founditR == False:
    if data[RCounter][4] > 0 and data[RCounter][1] == "Rockingham":
        print("Rockinghams first case was on " + data[RCounter][0])
        founditR = True
    RCounter = RCounter + 1

# this print command puts a space between Q1s results and Q2
print()

#Question 2: On what date was the greatest number of new cases reported in Harrisonburg? What date in Rockingham County?

# more variables for counting, date of max cases, and max cases

HCounter2 = 0
HmaxC=0
HmaxD=""

RCounter2 = 0
RmaxC=0
RmaxD=""

# both blocks of code do the same thing for different counties
# this loop goes through the list of data and checks to see if the county is the one we are looking for and if the current amount of cases is larger than the max
# if the current amount of cases is larger than the previous max the current amount will be assigned to max

while(HCounter2 < Length):
    if(data[HCounter2][1] == "Harrisonburg city" and data[HCounter2][4] > HmaxC):
        HmaxC = data[HCounter2][4]
        HmaxD = data[HCounter2][0]

    HCounter2 = HCounter2 + 1


while(RCounter2 < Length):
    if(data[RCounter2][1] == "Rockingham" and data[RCounter2][4] > RmaxC):
        RmaxC = data[RCounter2][4]
        RmaxD = data[RCounter2][0]

    RCounter2 = RCounter2 +1


# these print out the data found in the blocks above and create a space for the next question
print("Harrisonburgs day of most cases is ", HmaxD, " with ", HmaxC, " cases.")

print("Rockinghams day of most cases is ", RmaxD, " with ", RmaxC, " cases.")

print()

#Question 3: What was the worst seven-day period in Harrisonburg city for new COVID cases? What period in Rockingham County? These are the seven-day periods when the number of new cases was maximal.

# more variables for counting and stuff their functions will be explained in the text below
WeekSumH=0
WeekSumR=0
HCounter3=0
RCounter3=0
MaxH = 0
MaxR = 0
MaxStartH = ''
MaxEndH = '' 
MaxStartR = '' 
MaxEndR = ''


Rockingham_data =[]
Harrisonburg_data =[]
# this first for loop seperates the data from the larger data set into two that just have harrisonburg and rockingham data
for stuff in data:
    date, county, state, fips, cases, deaths = stuff

    if county == "Rockingham":
        Rockingham_data.append(stuff)

    if county == "Harrisonburg city":
        Harrisonburg_data.append(stuff)

# both while loops below do the same thing just for different counties
#  this block sums the cases for 7 days in a row and then checks to see if that value is higher than the previous max, similar to question two,
# if the 7 day sum is higher than the previous max the 7 day sum will be assigned as the new max and the start and end dates will be saved in variables

while HCounter3 < (len(Harrisonburg_data)-6):

    WeekSumH=0

    for i in range(7):
        WeekSumH += Harrisonburg_data[HCounter3 + i][4]

        if WeekSumH > MaxH:
            MaxH = WeekSumH
            MaxStartH = Harrisonburg_data[HCounter3][0]
            MaxEndH = Harrisonburg_data[HCounter3+6][0]

        
    HCounter3 = HCounter3 + 1


while RCounter3 < (len(Rockingham_data)-6):

    WeekSumR=0

    for i in range(7):
        WeekSumR += Rockingham_data[RCounter3 + i][4]

        if WeekSumR > MaxR:
            MaxR = WeekSumR
            MaxStartR = Rockingham_data[RCounter3][0]
            MaxEndR = Rockingham_data[RCounter3+6][0]

        
    RCounter3 = RCounter3 + 1

# this prints out the data calculated above with a space inbetween the two counties

print("Harrisonburg city:")
print("Worst 7-day period:", MaxStartH, "to", MaxEndH)
print("New cases:", WeekSumH)

print()

print("Rockingham County:")
print("Worst 7-day period:", MaxStartR, "to", MaxEndR)
print("New cases:", WeekSumR)