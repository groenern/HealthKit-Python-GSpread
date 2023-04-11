import xml.etree.ElementTree as ET
from model.Workout import Workout

class XMLParser:
    def __init__(self, fileName):
        self.fileName = fileName
        self.workouts = []
        self.runs = []
        self.walks = []
    
    # fill self.workouts will all workout data
    def parse(self):
        tree = ET.parse(self.fileName)
        root = tree.getroot()

        # Find all Workout elements and create a Workout object for each one
        for workout in root.findall('.//Workout'):
            # Generic List of All Workouts
            self.workouts.append(Workout(workout))

    def getWorkouts(self):
        return self.workouts
    