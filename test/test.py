# tests


#from os import chdir



#chdir(r'C:\Users\Noe\Documents\Visual Studio 2015\Projects\stakenannyb\stakenannyb')
#from sys import path
#path.append(r'C:\Users\Noe\Documents\Visual Studio 2015\Projects\stakenannyb\stakenannyb\candiapps')
import stakenannyb as sn



import unittest

class functionalTest(unittest.TestCase):
#def setUp(sef):
    #    self.sn = sn.commandstart()
    
    #def tearDown(self):
    #    self.sn.commandquit()

    #def test_setup_is_correct(self):
    #    self.assertTrue(sn.setup())

    #def test_issncmdfileinstantupifnodo_is_correct(self):
    #    self.assertTrue(sn.setup.issncmdfileinstartupifnodo())
        

    def test_can_place_config_file_into_environment_variables(self):
        # Jody set the stakenani.conf to the appropriate path and kept the wallets he did not want to run at None
        self.assertIn('turbostake', sn.envars['coinlist'])
        # prompt user for input on an infinite loop


        # Enter help to list commands
        self.assertIn('help', str(sn.commandhelp))
#assert 'not a valid command' in str(stakenannyb.commandstart.
# ndj skipping becuase it will test the inside of an infinite loop, not sure how to implement that in tdd just yet
# provide bad command type help for options message.
# provide option to quit
#output

    
 
    def test_can_verify_session_integrety_and_prompt_for_options_based_on_findings(self):
        # PID 1 is there a datafolder, if not make one
        self.assertTrue(sn.finddirmakeifno())

        #don't forget to test the app reaction to a session alreadly running

        # PID 2 is there a sessions.dat file, if not make one


class NewUserTest(unittest.TestCase):


    def test_can_grab_conf_and_check_it_later(self):

        
        self.assertEqual(str(sn.commandcoinssupported()), ('turbostake',))
        self.assertEqual(sn.envars['coinlist'], 'turbostake')
        

    #def test_make_file_if_not_exitst(slef): 
     
        
    # def test_can_accept_input_and_execute_fuction(self):
    #     self.assertEqual(stakenanny.commandhelp, ('help', 'quit', 'coinssupported'))

    #     output = stakenanny.commandhelp()
    #     assert(output == 'blah', 'quit')
    
        

if __name__ == '__main__':
    unittest.main()