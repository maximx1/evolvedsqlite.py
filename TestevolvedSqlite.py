import unittest
from evolvedsqlite import *

class TestEvolvedSqlite(unittest.TestCase):
	def setUp(self):
		self.files = ["1.sql", "2.sql", "3.sql", "4.sql"]

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
