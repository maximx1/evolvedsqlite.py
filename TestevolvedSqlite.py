import unittest
from evolvedsqlite import *

class TestEvolvedSqlite(unittest.TestCase):
	def setUp():
		self.files = ["1.sql", "2.sql", "3.sql", "4.sql"]

	def test_filterInstalledVersionCanFilterAllVersions():
		self.assertFalse(filterInstalledVersion(self.files, 4))

	def test_filterInstalledVersionCanFilterOnlyOneVersion():
		self.assertFalse(filterInstalledVersion(self.files, 1))

	def test_filterInstalledVersionCanFilterMultipleVersions():
		self.assertFalse(filterInstalledVersion(self.files, 2))
	
	def test_canSortMultipleSqlFiles():
		unsortedFiles = ["4.sql", "2.sql", "1.sql", "4.sql"]
		self.assertEqual(sortNumberedSqlFiles(unsortedFiles), self.files)
		
	def test_canSortOneSqlFile():
		oneFile = ["1.sql"]
		self.assertEqual(["1.sql"], sortNumberedSqlFiles(oneFile))
		
	def test_canSortEmptyList():
		noneFile = []
		self.assertEmpty(sortNumberedSqlFiles(noneFile))
		
if __name__ == '__main__':
	unittest.main()
