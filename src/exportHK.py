from tabulate import tabulate
import sys
import datetime
from util.XMLParser import XMLParser 
from util.GoogleHandler import GoogleHandler

def checkCommandLineArg():
    if len(sys.argv) < 2:
        #print("Please provide the file name as command line argument.")
        #sys.exit(1)
        return "export.xml" ## DELETE LATER

    return sys.argv[1]

def populateWorkouts():
    # Get Filename from sysargs and parse xml data
    fileName = checkCommandLineArg() 
    xmlObject = XMLParser(fileName)
    xmlObject.parse()
    
    # populate our working data
    workouts = xmlObject.getWorkouts()
    
    return workouts

# created a dictionary of different workout types
def createWorkoutDict(workouts):
    sortedWorkouts = {}

    for workout in workouts:
        activityType = workout.workoutActivityType
        activityType = activityType.replace('HKWorkoutActivityType', '') # change dictionary key for more uniqueness and easier readability when debugging
        if activityType not in sortedWorkouts:
            sortedWorkouts[activityType] = []
            
        sortedWorkouts[activityType].append(workout)

    return sortedWorkouts

def main():
    workouts = populateWorkouts()

    # set up googlehandler and connect
    email = 'romangroenewold@gmail.com'
    credentials = 'credentials.json'
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    spreadsheet = 'Apple_Watch_Spreadsheet_Data_{}'.format(today)
    myGoogleHandler = GoogleHandler(email, credentials,spreadsheet)

    # create and populates workouts
    numRows = len(workouts)
    numCols = len(workouts[0])

    myGoogleHandler.createWorksheet("Workouts", numRows, numCols)
    myGoogleHandler.populateWorksheet("Workouts", workouts)

    sortedWorkouts = createWorkoutDict(workouts)
    
    for activityType, workoutList in sortedWorkouts.items():
        numRows = len(workoutList)
        
        myGoogleHandler.createWorksheet(activityType, numRows, numCols)
        myGoogleHandler.populateWorksheet(activityType, workoutList)
        

    print(myGoogleHandler.__str__())

if __name__ == '__main__':
    main()