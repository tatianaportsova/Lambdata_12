
# test.college_test.py

import unittest
from my_lambdata.college_oop import College

class EDU(unittest.TestCase):

    def test_edu(self):
        college_dicts = [{"city": "New York", "state": "NY",
        "funding": "Private, non-profit", "name": "Columbia University"},
        {"city": "New York", "state": "NY",
        "funding": "Private, non-profit", "name": "New York University"},
        {"city": "New York", "state": "NY",
        "funding": "Private, non-profit", "name": "Barnard College"},
        {"city": "New York", "state": "NY",
        "funding": "Public", "name": "Baruch College"},
        {"city": "New York", "state": "NY",
        "funding": "Private, non-profit", "name": "Fordham University"}]
         # test to make sure this test was setup properly

        for idx, college_dict in enumerate(college_dicts):
            college = College(college_dict["name"], college_dict["city"], college_dict["state"],college_dict["funding"])
            
        
            # assert there exists a "name" index in college dictionaries
            self.assertTrue(college.name == college_dicts[idx]['name'])

            # assert there are string values in the "name" index
            self.assertEquals(isinstance(college.name[3], str))
        



if __name__ == '__main__':
    unittest.main()