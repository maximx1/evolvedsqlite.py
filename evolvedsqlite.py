import os.path
from os import walk
import sqlite3
import re

def evolvedb(path, database):
	if not os.path.isfile(settings.database):
		conn = sqlite3.connect(database)
		with conn:
			cursor = conn.cursor()
			setupRegistryTable(cursor)
			latestVersion = determineLatestVersion(cursor)
			files = sortNumberedSqlFiles(filterInstalledVersion(determineEvolveScripts(path), latestVersion))
			for fname in files
				with open(fname, 'r') as f:
				isUpgrade = True
					for line in f:
						line = line.rstrip()
						if line.startswith("//--downgrade"):
							isUpgrade = False
						if isUpgrade:
							if "" != line and not line.startswith("//"):
								print("Executing: '" + line + "'")
								cursor.execute(line)
						else:
							if "" != line and not line.startswith("//"):
								loadIntoDowngrade(cursor, line, fname)
						

def determineEvolveScripts(path):
	_, _, files	= walk(path)
	return list(filter(lambda x: re.match('\d+\.sql', x), files))

def filterInstalledVersion(files, latestVersion):
	return list(filter(lambda x: int(x[:-4]) > latestVersion, files))

def sortNumberedSqlFiles(files):
	return sorted(files, key=lambda x: int(x[:-4]))

def loadIntoDowngrade(cursor, statement, script):
	cursor.execute("INSERT INTO evolutionRegistry(downgrades, scriptNumber) values (?, ?)", (statement, int(script[:-4])))

def determineLatestVersion(cursor):
	cursor.execute("SELECT max(scriptNumber) from evolutionRegistry")
	result = cursor.fetchone()
	return result[0] if result else 0

def setupRegistryTable(cursor):
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='evolutionRegistry';")
	result = cursor.fetchone()
	if not result:
		cursor.execute("CREATE TABLE evolutionRegistry(id INTEGER PRIMARY KEY AUTOINCREMENT, downgrades TEXT, scriptNumber INTEGER NOT NULL);")

def runDowngrade(files, cursor):
	latestFileNumber = int(sortNumberedSqlFiles(files)[-1][:-4])
	cursor.execute("SELECT downgrades from evolutionRegistry where scriptNumber > ? order by scriptNumber, id", (latestFileNumber,))
	for statementRow in cursor.fetchall():
		cursor.execute(statementRow[0])
	cursor.execute("DELETE from downgrades where scriptNumber > ?", (latestFileNumber,))
