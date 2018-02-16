import unittest
#from PythonChallenge import HelperFunctions
import dependencies
#from helperfunctions import helperfunctions as hf
import helperfunctions

helperfunctions.who_am_i


# This should go in the python challenge test module
class Test_PythonChallenge_test1(unittest.TestCase):
    known_answers_gen_char_neighbor = [('U', 'kAeMKENi'),
                                       ('K', 'AewULNih'),
                                       ('L', 'ewtKEihr')
                                       ]
    
    def test_HelperFunctions_gen_char_neighbor_known_answers(self):
        """ Test some known answers of the generator.
        """
        test_gen = hf.gen_char_neighbor('problem3_source_mess.txt')
        for center, neighbors in self.known_answers_gen_char_neighbor:
            print('center={}, neighbors={}'.format(center, neighbors))
            test_ans = next(test_gen)
            print('test_ans={}'.format(test_ans))
            self.assertEqual((center, neighbors), test_ans)
    
    

if __name__ == '__main__':
    unittest.main()
