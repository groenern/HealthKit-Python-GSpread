from tabulate import tabulate
import sys
import datetime
from util.WorkoutUtility import WorkoutUtility
from util.XMLParser import XMLParser 
from model.Workout import Workout
from util.GoogleHandler import GoogleHandler

def checkCommandLineArg():
    if len(sys.argv) < 2:
        #print("Please provide the file name as command line argument.")
        #sys.exit(1)
        return "export.xml" ## DELETE LATER

    return sys.argv[1]

def populateData():
    # Get Filename from sysargs and parse xml data
    fileName = checkCommandLineArg() 
    xmlObject = XMLParser(fileName)
    xmlObject.parse()

    # create workout utility
    workUtility = WorkoutUtility()
    
    # populate our working data
    workouts = xmlObject.getWorkouts()
    runs, walks = xmlObject.getRunsWalks()
    
    # get rows and cols -> didn't want to create second utility object
    rowWidth, colLength = workUtility.calcRowsCols(workouts=workouts)

    return workouts, runs, walks, rowWidth, colLength


def main():
    workouts, runs, walks, rowWidth, colLength = populateData()

    # set up googlehandler and connect
    email = 'romangroenewold@gmail.com'
    credentials = 'credentials.json'
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    spreadsheet = 'Apple_Watch_Spreadsheet_Data_{}'.format(today)
    myGoogleHandler = GoogleHandler(email, credentials,spreadsheet)

    # create and populates workouts
    myGoogleHandler.createWorksheet("Workouts", rowWidth, colLength)
    myGoogleHandler.populateWorksheet("Workouts", workouts)

    # create and populate runs
    myGoogleHandler.createWorksheet("Runs", rowWidth, colLength)
    myGoogleHandler.populateWorksheet("Runs", runs)

    # create and populate walks
    myGoogleHandler.createWorksheet("Walks", rowWidth, colLength)
    myGoogleHandler.populateWorksheet("Walks", walks)

    print(myGoogleHandler.__str__())

if __name__ == '__main__':
    main()