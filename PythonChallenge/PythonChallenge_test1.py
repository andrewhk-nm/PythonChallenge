import unittest
from PythonChallenge import HelperFunctions

class Test_PythonChallenge_test1(unittest.TestCase):
    known_answers_gen_char_neighbor = {'U': 'kAeMKENi',
                                       'K': 'AewULNih',
                                       }
    
    def test_HelperFunctions_gen_char_neighbor_known_answers(self):
        """ Test some known answers of the generator.
        """
        test_gen = HelperFunctions.gen_char_neighbor('problem3_source_mess.txt')
        for ans in self.known_answers_gen_char_neighbor:
            print('ans_tuple={}, ans_list={}'.format(ans, self.known_answers_gen_char_neighbor[ans]))
            ans_dict = {ans: self.known_answers_gen_char_neighbor[ans]}
            print('ans_dict={}'.format(ans_dict))
            test_ans = next(test_gen)
            print('test_ans={}'.format(test_ans))
            self.assertDictEqual(ans_dict, test_ans)

    
    def test_A(self):
        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
