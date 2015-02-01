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
	
		
if __name__ == '__main__':
	unittest.main()
