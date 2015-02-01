import os.path
from os import walk
import sqlite3
import re

def evolvedb(path, database):
	if not os.path.isfile(settings.database):
		conn = sqlite3.connect(database)
		with conn:
			cursor = conn.cursor()
			with open(settings.schema, 'r') as f:
				for line in f:
					line = line.rstrip()
					if "" != line and not line.startswith("//"):
						print("Executing: '" + line + "'")
						cursor.execute(line)

def determineEvolveScripts(path):
	_, _, files	= walk(path)
	return list(filter(lambda x: re.match('\d+\.sql', x), files))

def sortNumberedSqlFiles(files):
	return sorted(files, key=lambda x: int(x[:-4]))

def loadIntoDowngrade(cursor, statement, script):
	cursor.execute("INSERT INTO evolutionRegistry(downgrades, scriptNumber) values (?, ?)", (statement, int(script[:-4])))

def setupRegistryTable(cursor):
	cursor.execute("CREATE TABLE evolutionRegistry(id INTEGER PRIMARY KEY AUTOINCREMENT, downgrades TEXT, scriptNumber INTEGER NOT NULL);")

def runDowngrade(files, cursor):
	latestFileNumber = int(sortNumberedSqlFiles(files)[-1][:-4])
	cursor.execute("SELECT downgrades from evolutionRegistry where scriptNumber > ? order by scriptNumber, id", (latestFileNumber,))
	for statementRow in cursor.fetchall():
		cursor.execute(statementRow[0])
	cursor.execute("DELETE from downgrades where scriptNumber > ?", (latestFileNumber,))
