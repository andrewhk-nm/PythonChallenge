import unittest
from PythonChallenge import HelperFunctions

class Test_PythonChallenge_test1(unittest.TestCase):
    known_answers_gen_char_neighbor = [('U', 'kAeMKENi'),
                                       ('K', 'AewULNih'),
                                       ('L', 'ewtKEihr')
                                       ]
    
    def test_HelperFunctions_gen_char_neighbor_known_answers(self):
        """ Test some known answers of the generator.
        """
        test_gen = HelperFunctions.gen_char_neighbor('problem3_source_mess.txt')
        for center, neighbors in self.known_answers_gen_char_neighbor:
            print('center={}, neighbors={}'.format(center, neighbors))
            test_ans = next(test_gen)
            print('test_ans={}'.format(test_ans))
            self.assertEqual((center, neighbors), test_ans)

    
    def test_A(self):
        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
