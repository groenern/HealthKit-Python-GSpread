from datetime import datetime
from model.Workout import Workout

class WorkoutUtility:
    def groupByWeek(self, workouts):
        weekGroups = {}
        weekStart = datetime.strptime(workouts[0].creationDate, '%Y-%m-%d %H:%M:%S %z')

        for workout in workouts:
            creationDate = datetime.strptime(workout.creationDate, '%Y-%m-%d %H:%M:%S %z')
            weekNumber = (creationDate - weekStart).days // 7 + 1
            if weekNumber not in weekGroups:
                weekGroups[weekNumber] = []
            weekGroups[weekNumber].append(workout)

        # Create empty lists for weeks without any workouts that didn't already get added
        minWeek = min(weekGroups.keys())
        maxWeek = max(weekGroups.keys())
        for weekNumber in range(minWeek, maxWeek+1):
            if weekNumber not in weekGroups:
                weekGroups[weekNumber] = []

        return weekGroups

    # Calculate weekly totals with percent change from previous week
    def calculateWeeklyTotals(self, workouts):

        weeklyTotals = {}
        totalMiles = 0
        totalCalories = 0

        weekGroups = self.groupByWeek(workouts)
        for weekNumber, weekWorkouts in weekGroups.items():
            weeklyTotalDistance = sum(float(workout.totalDistance) for workout in weekWorkouts if workout.totalDistance)
            weeklyTotalActiveEnergy = sum(float(workout.totalActiveEnergy) for workout in weekWorkouts if workout.totalActiveEnergy)
            weeklyTotals[weekNumber] = {
                'totalDistance': round(weeklyTotalDistance, 2),
                'totalDistanceUnit': weekWorkouts[0].totalDistanceUnit if weekWorkouts else 'N/A',
                'totalActiveEnergy': round(weeklyTotalActiveEnergy, 2),
                'totalActiveEnergyUnit': weekWorkouts[0].totalActiveEnergyUnit if weekWorkouts else 'N/A',
            }

            totalMiles += weeklyTotalDistance
            totalCalories += weeklyTotalActiveEnergy

            if weekNumber == 1 or weekNumber-1 not in weeklyTotals:
                weeklyTotals[weekNumber]['percentChange'] = 'N/A'
            else:
                previousWeekTotalDistance = weeklyTotals[weekNumber-1]['totalDistance']
                if previousWeekTotalDistance == 0:
                    weeklyTotals[weekNumber]['percentChange'] = 0
                else:
                    percentChange = (weeklyTotalDistance - previousWeekTotalDistance) / previousWeekTotalDistance * 100
                    weeklyTotals[weekNumber]['percentChange'] = f'{percentChange:.2f}%'

        return weeklyTotals
    
    def calcRowsCols(self, workouts):
        # +1 for blank space in top left
        rows = len(workouts) + 1
        cols = len(workouts[0]) + 1

        return rows, cols