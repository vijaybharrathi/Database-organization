""" Implementation of
			1. Cartesian Product
			2. Natural Join
			3. Inner Join
			4. Full Outer Join
	@Author : Vijay Bharrathi (A20356386)  """


import io
import csv
import itertools

""" Class to create objects out of records in Player details Table """
class PlayerDetails:
	playerCount = 0

	""" Constructor for PlayerDetails Class """
	def __init__(self,playerList):
		self.playerName = playerList[0]
		self.goals = playerList[1]
		self.offSides = playerList[2]
		self.fouls = playerList[3]
		PlayerDetails.playerCount += 1

""" Class to create objects out of records in Country Details Table """
class CountryDetails:

	""" Constructor for CountryDetails Class """
	def __init__(self,countryList):
		self.playerName = countryList[0]
		self.country = countryList[1]


"""  Function to read lines from the text file and convert them to list.
	 Arguments : None
	 Returns : x: List  corresponding to records in Player details Table
	 		   y: List  corresponding to records in Country details Table"""

def importTable(): 
	aRecords = []
	bRecords = []
	with open('file1.txt') as a,open('file2.txt') as b:
		aValues = map(str.rstrip, a)
		bValues = map(str.rstrip, b)
		for aValue in aValues[1:] :
	   		aRecords.append(aValue)
	   	for bValue in bValues[1:] :
	   		bRecords.append(bValue)
		x = list(csv.reader(aRecords))
		y = list(csv.reader(bRecords))
	return x,y

"""  Function to return cartesian product of the tables
	 Arguments : playerListOfObjects,countryListOfObjects
	 Returns : Cartesian product of two tables """

def cartesianProduct(playerListOfObjects,countryListOfObjects): 
	print "-----------------------------CARTESIAN PRODUCT------------------------------------------"
	#print "PLAYERNAME GOALS OFFSIDES FOULS PLAYERNAME COUNTRY"
	for i in playerListOfObjects:
		for j in countryListOfObjects:
			print i.playerName,i.goals,i.offSides,i.fouls,j.playerName,j.country

"""  Function to return cartesian product of the tables
	 Arguments : playerListOfObjects,countryListOfObjects
	 Returns : Natural join of two tables """

def naturalJoin(playerListOfObjects,countryListOfObjects):
	print "-----------------------------NATUARL JOIN-----------------------------------------------"
	for i in playerListOfObjects:
		for j in countryListOfObjects:
			if(i.playerName == j.playerName):
				print i.playerName,i.goals,i.offSides,i.fouls,j.country

"""  Function to return cartesian product of the tables
	 Arguments : playerListOfObjects,countryListOfObjects
	 Returns : Inner Join of two tables """


def innerJoin(playerListOfObjects,countryListOfObjects):
	print "-----------------------------INNER JOIN-------------------------------------------------"
	for i in playerListOfObjects:
		for j in countryListOfObjects:
			if(i.playerName == j.playerName):
				print i.playerName,i.goals,i.offSides,i.fouls,j.playerName,j.country


"""  Function to return cartesian product of the tables
	 Arguments : playerListOfObjects,countryListOfObjects
	 Returns : Full outer join of two tables """

def fullOuterJoin(playerListOfObjects,countryListOfObjects):
	print "-----------------------------FULL OUTER JOIN--------------------------------------------"
	p = {}
	for i in playerListOfObjects:
		for j in countryListOfObjects:
			if(i.playerName == j.playerName):
				p[i.playerName] = True
				#p[j.playerName] = True
				print i.playerName,i.goals,i.offSides,i.fouls,j.playerName,j.country
				
	for i in playerListOfObjects:
		if i.playerName not in p.keys():
			print i.playerName,i.goals,i.offSides,i.fouls

	for j in countryListOfObjects:
		if j.playerName not in p.keys() :
			print "              ",j.playerName,j.country
			
""" Main Function """	

def main():
	x,y = importTable() ##call to importTable funtion to get list  corresponding to records
	playerListOfObjects = []
	for records in x :
		playerObject = 	PlayerDetails(records)
		playerListOfObjects.append(playerObject)
	countryListOfObjects = []
	for records in y:
		countryObject = CountryDetails(records)
		countryListOfObjects.append(countryObject)
	cartesianProduct(playerListOfObjects,countryListOfObjects)  # call to cartesianProduct funtion
	naturalJoin(playerListOfObjects,countryListOfObjects)  # call to naturalJoin funtion
	innerJoin(playerListOfObjects,countryListOfObjects) # call to innerJoin funtion
	fullOuterJoin(playerListOfObjects,countryListOfObjects) # call to fullOuterJoin funtion 
	
""" Invoking Main Function """		
if __name__=="__main__":
	main() 