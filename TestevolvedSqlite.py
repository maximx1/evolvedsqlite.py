import unittest
import os
import os.path
import shutil
from evolvedsqlite import *

class TestEvolvedSqlite(unittest.TestCase):
	def setUp(self):
		self.files = ["1.sql", "2.sql", "3.sql", "4.sql"]
		self.testDir = "test_dir"

	def setUpTestDir(self, filesToCreate):
		self.scrubTestBed()
		os.makedirs(self.testDir)
		list(map(lambda x: open(self.testDir + "/" + x, 'w').close(), filesToCreate))
	
	def scrubTestBed(self):
		if os.path.exists(self.testDir):
			shutil.rmtree(self.testDir)

	def test_setTmp(self):
		self.setUpTestDir(self.files)
		self.scrubTestBed()
		self.assertTrue(True)

	def test_filterInstalledVersionCanFilterAllVersions(self):
		self.assertListEqual(filterInstalledVersion(self.files, 4), [])

	def test_filterInstalledVersionCanFilterOnlyOneVersion(self):
		self.assertListEqual(filterInstalledVersion(self.files, 1), ["2.sql", "3.sql", "4.sql"])

	def test_filterInstalledVersionCanFilterMultipleVersions(self):
		self.assertListEqual(filterInstalledVersion(self.files, 2), ["3.sql", "4.sql"])
	
	def test_canSortMultipleSqlFiles(self):
		unsortedFiles = ["4.sql", "2.sql", "1.sql", "3.sql"]
		self.assertListEqual(sortNumberedSqlFiles(unsortedFiles), self.files)
		
	def test_canSortOneSqlFile(self):
		oneFile = ["1.sql"]
		self.assertListEqual(["1.sql"], sortNumberedSqlFiles(oneFile))
		
	def test_canSortEmptyList(self):
		noneFile = []
		self.assertListEqual(sortNumberedSqlFiles(noneFile), [])
		
if __name__ == '__main__':
	unittest.main()
