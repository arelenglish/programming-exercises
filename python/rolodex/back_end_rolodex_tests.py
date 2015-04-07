import os
import unittest
from back_end_rolodex import *


class TestRolodexFunctions(unittest.TestCase):
    """Tests for the filter_addresses() function."""

    def setUp(self):
        """Fixtures that creates a file for the test methods to use,
           and the output that should be produced from that file.
        """
        
        self.test_data = "data_test_file.in"
        with open(self.test_data, mode='w', encoding='utf-8') as f:
            f.write('Noah, Moench, 123123121, 232 695 2394, yellow\n'
                    'Ria Tillotson, aqua marine, 97671, 196 910 5548\n'
                    'Liptak, Quinton, (653)-889-7235, yellow, 70703\n'
                    '0.547777482345\n') 
            f.close()

        self.sorted_data = [['Noah, Moench, 123123121, 232 695 2394, yellow',
                             'Ria Tillotson, aqua marine, 97671, 196 910 5548',
                             'Liptak, Quinton, (653)-889-7235, yellow, 70703'],
                             [3]]

        self.spaces_data = ['Noah', 'Moench', '123123121', '232 695 2394', 'yellow'] 
        self.spaces_dict = {
                             "color": "yellow",
                             "firstname": "Noah",
                             "lastname": "Moench",
                             "phonenumber": "232-695-2394",
                             "zipcode": "123123121"
                           } 
        
        self.full_name_data = ['Ria Tillotson', 'aqua marine', '97671', '196 910 5548']  
        self.full_name_dict = {
                                "color": "aqua marine",
                                "firstname": "Ria",
                                "lastname": "Tillotson",
                                "phonenumber": "196-910-5548",
                                "zipcode": "97671"
                              }                 
        
        self.paren_data = ['Liptak', 'Quinton', '(653)-889-7235', 'yellow', '70703']
        self.paren_dict = {
                            "color": "yellow",
                            "firstname": "Quinton",
                            "lastname": "Liptak",
                            "phonenumber": "653-889-7235",
                            "zipcode": "70703"
                          }

        self.final_dict = {"entries": [
                                        self.paren_dict,
                                        self.spaces_dict, 
                                        self.full_name_dict, 
                                      ], 
                                      "errors": self.sorted_data[1]}

        self.json_output = """{
  "entries": [
    {
      "color": "yellow",
      "firstname": "Quinton",
      "lastname": "Liptak",
      "phonenumber": "653-889-7235",
      "zipcode": "70703"
    },
    {
      "color": "yellow",
      "firstname": "Noah",
      "lastname": "Moench",
      "phonenumber": "232-695-2394",
      "zipcode": "123123121"
    },
    {
      "color": "aqua marine",
      "firstname": "Ria",
      "lastname": "Tillotson",
      "phonenumber": "196-910-5548",
      "zipcode": "97671"
    }
  ],
  "errors": [
    3
  ]
}
"""


    def tearDown(self):
        """Fixture that deletes the files used by the test methods"""
        try:
            os.remove(self.test_data)
            os.remove('json.out')
        except:
            pass


    def test_filter_addresses(self):
        """Sorts data into error list and address list and 
           returns a list containing each list
        """
        self.assertEqual(filter_addresses(self.test_data), self.sorted_data)


    def test_address_with_spaces(self):
            """Returns a formatted dictionary of addresses
               that have phone numbers with spaces a seperators.
            """    
            self.assertEqual(address_with_spaces(self.spaces_data), self.spaces_dict)


    def test_address_with_full_name(self):
        """Returns a formatted dictionary of addresses
           that have full names instead of names separated 
           into first and last names.
        """
        self.assertEqual(address_with_full_name(self.full_name_data), self.full_name_dict)
    

    def test_address_with_parens(self):
        """Returns a formatted dictionary of addresses that have 
           phone numbers with parentheses around the area code. 
        """
        self.assertEqual(address_with_parens(self.paren_data), self.paren_dict)


    def test_pick_format(self):
        """Chooses the correct function to format an address
           Given an address.
        """
        first_address = self.sorted_data[0][0]
        self.assertEqual(pick_format(first_address), self.spaces_dict)


    def test_build_rolodex(self):
        """Builds the final sorted rolodex dictionary"""
        self.assertEqual(dict(build_rolodex(self.test_data)), self.final_dict)

    
    def test_phone_number_formatter(self):
        """Formats valid phone numbers to follow the 123-456-7890 format"""    
        self.assertEqual(phone_number_formatter('(123)-456-7890'), '123-456-7890')
        self.assertEqual(phone_number_formatter('123 456 7890'), '123-456-7890')
        self.assertEqual(phone_number_formatter('123-456-7890'), '123-456-7890')
        self.assertEqual(phone_number_formatter('1234567890'), '123-456-7890')


    def test_generate_output(self):
        """Converts final address dictionary to JSON and writes it to a file"""
        generate_output(self.test_data)
        generated_file = self.read_generated_file()

        self.assertTrue(os.path.exists('json.out'))
        self.assertEqual(generated_file.strip(), self.json_output.strip())


    def test_rolodex(self):
        """Just calls generate_output() and should produce the same result"""
        rolodex(self.test_data)
        generated_file = self.read_generated_file()

        self.assertTrue(os.path.exists('json.out'))
        self.assertEqual(generated_file.strip(), self.json_output.strip())
        

    def read_generated_file(self):
        f = open('json.out', mode='r', encoding='utf-8')
        generated_file = f.read()
        f.close()
        return generated_file


if __name__ == '__main__':
    unittest.main()
