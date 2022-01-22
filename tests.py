from audioop import add
import unittest
import scraper
import csv
import os

class testSampleData(unittest.TestCase):
        
    def test_csv_output(self):
        """Testing CSV Creation and Integrity"""
        file_name = "test_file.csv"
        header = ['Company', 'Street', 'City', 'St', 'ZIPCode']
        test_content = [['BEND PAWN & TRADING CO-LAPINE', '52504 U.S. 97', 'LA PINE', 'OR', '97739']]
        scraper.create_csv(file_name, header, test_content)
        # Now to ensure that the content is as expected and then delete test
        with open(file_name, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            self.assertEqual(header, next(reader, None))
            for line in reader:
                self.assertEqual(line, test_content[0])
        os.remove(file_name)
        
    def test_address_query(self):
        """Test Address Lookup"""
        address = ['BEND PAWN & TRADING CO-LAPINE', '52504 U.S. 97', 'LA PINE', 'OR', '97739']
        scraper.query_address(address)
        self.assertEqual(address[5], False)
        address_true = ['CARDIOSTART RESALE THRIFT STR', '435 W CASCADE AVE', 'SISTERS', 'OR', '97759']
        scraper.query_address(address_true)
        self.assertEqual(address_true[5], True)
        
        
if __name__ == "__main__":
    unittest.main();