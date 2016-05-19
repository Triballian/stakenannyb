# tests


#from os import chdir



#chdir(r'C:\Users\Noe\Documents\Visual Studio 2015\Projects\stakenannyb\stakenannyb')
from sys import path as spath
#path.append(r'C:\Users\Noe\Documents\Visual Studio 2015\Projects\stakenannyb\stakenannyb\candiapps')
#spath.append('..\stakenannyb')
import stakenannyb as sn
from finddirmakeifno import finddirmakeifno



import unittest


class NewUserTest(unittest.TestCase):


    def test_can_grab_conf_and_check_it_later(self):

        
        #self.assertEqual(str(stakenannyb.commandcoinssupported()), 'turbostake')
        self.assertTrue(sn.commandcoinssupported())
        self.assertEqual(sn.envars['coinlist'], 'turbostake')
        

    #def test_make_file_if_not_exitst(slef): 
     
        
    # def test_can_accept_input_and_execute_fuction(self):
    #     self.assertEqual(stakenanny.commandhelp, ('help', 'quit', 'coinssupported'))

    #     output = stakenanny.commandhelp()
    #     assert(output == 'blah', 'quit')
    
        

if __name__ == '__main__':
    unittest.main()