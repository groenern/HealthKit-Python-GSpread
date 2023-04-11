class Workout:
    def __init__(self, workoutElement):
        # parse directly 
        self.workoutActivityType = workoutElement.get('workoutActivityType')
        self.duration = workoutElement.get('duration')
        self.durationUnit = workoutElement.get('durationUnit')
        self.creationDate = workoutElement.get('creationDate')

        # Metadata Entires
        self.indoorWorkout = None
        self.weatherTemperature = None
        self.weatherHumidity = None
        self.elevationAscended = None

        # Workout Statistics
        self.totalDistance = None
        self.totalDistanceUnit = None
        self.totalActiveEnergy = None
        self.totalActiveEnergyUnit = None

        metadataEntries = workoutElement.findall('.//MetadataEntry')
        for entry in metadataEntries:
            if entry.get('key') == 'HKIndoorWorkout':
                self.indoorWorkout = entry.get('value')
            elif entry.get('key') == 'HKWeatherTemperature':
                self.weatherTemperature = entry.get('value')
            elif entry.get('key') == 'HKWeatherHumidity':
                self.weatherHumidity = entry.get('value')
            elif entry.get('key') == 'HKElevationAscended':
                self.elevationAscended = entry.get('value')

        workoutStatistics = workoutElement.findall('.//WorkoutStatistics')
        for entry in workoutStatistics:
            if entry.get('type') == "HKQuantityTypeIdentifierActiveEnergyBurned":
                self.totalActiveEnergy = entry.get('sum')
                self.totalActiveEnergyUnit = entry.get('unit')
            elif entry.get('type') == "HKQuantityTypeIdentifierDistanceWalkingRunning":
                self.totalDistance = entry.get('sum')
                self.totalDistanceUnit = entry.get('unit')
    
    def __str__(self):
        if self.indoorWorkout:
            return f'{self.workoutActivityType}, Indoor: {self.indoorWorkout}, Duration: {self.duration} {self.durationUnit}, Distance: {self.totalDistance} {self.totalDistanceUnit}, Energy Burned: {self.totalActiveEnergy} {self.totalActiveEnergyUnit}, Created on: {self.creationDate}'
        else:
            return f'{self.workoutActivityType}, Duration: {self.duration} {self.durationUnit}, Distance: {self.totalDistance} {self.totalDistanceUnit}, Energy Burned: {self.totalActiveEnergy} {self.totalActiveEnergyUnit}, Created on: {self.creationDate}, Elevation Ascended: {self.elevationAscended}, Temperature: {self.weatherTemperature}, Humidity: {self.weatherHumidity}'

    def __len__(self):
        return len(vars(self))