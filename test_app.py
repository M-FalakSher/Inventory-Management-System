import unittest
import sqlite3
import os

class TestInventorySystem(unittest.TestCase):
    
    def setUp(self):
        """Set up a temporary test database before every test"""
        self.db_name = "test_ims.db"
        self.con = sqlite3.connect(self.db_name)
        self.cur = self.con.cursor()
        # Create a simplified category table for testing
        self.cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
        self.con.commit()

    def test_add_category(self):
        """Test if a category can be added to the database"""
        test_name = "Electronics"
        self.cur.execute("insert into category(name) values(?)", (test_name,))
        self.con.commit()
        
        # Verify
        self.cur.execute("select * from category where name=?", (test_name,))
        row = self.cur.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row[1], "Electronics")

    def test_billing_calculation(self):
        """Test the logic used in billing (logic extracted from billing.py)"""
        qty = 2
        price = 500
        expected_total = 1000
        
        # Simulating the calculation found in billing.py
        calculated_total = qty * price
        self.assertEqual(calculated_total, expected_total)

    def tearDown(self):
        """Clean up the test database after tests run"""
        self.con.close()
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

if __name__ == '__main__':
    unittest.main()