from typing import NewType
from components import ROTOR_NOTCHES, Rotor, Reflector, Plugboard, ALPHABET
from machine import Enigma
import unittest
from unittest.mock import Mock, patch, call
import io, sys

class TestRoter(unittest.TestCase):

    def setUp(self):
        self.rotor1 = Rotor("I", "A")
        self.rotor2 = Rotor("II", "B")
        self.rotor3 = Rotor("III", "C")
        self.rotor1.next_rotor = self.rotor2
        self.rotor2.prev_rotor = self.rotor1
        self.rotor2.next_rotor = self.rotor3
        self.rotor3.prev_rotor = self.rotor2
        # set stdout to capturedOutput
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput
    
    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_constructor_error(self):
        with self.assertRaises(ValueError):
            Rotor("IV", "A")
        Rotor("I", "A")
        Rotor("II", "A")
        Rotor("III", "A")
        Rotor("V", "A")

    def test_constructor(self):
        rotor = Rotor("II", "d")
        attr = hasattr(rotor, "rotor_num") \
            and hasattr(rotor, "wiring") \
            and hasattr(rotor, "notch") \
            and hasattr(rotor, "window") \
            and hasattr(rotor, "offset") \
            and hasattr(rotor, "next_rotor") \
            and hasattr(rotor, "prev_rotor")
        self.assertTrue(attr)

    def test_repr(self):
        expected = "Wiring:\n{'forward': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'backward': 'UWYGADFPVZBECKMTHXSLRINQOJ'}\nWindow: A"
        self.assertEqual(str(self.rotor1), expected)

    def test_step(self):
        # single step
        with patch.object(self.rotor2, "step") as step2:
            self.rotor1.step()
            self.assertEqual(self.rotor1.window, "B")
            self.assertEqual(step2.call_count, 0)

    def test_step_singlestep(self):
        # when rotor1 reaches Q, triggers rotor2 to move
        self.rotor1.change_setting("Q")
        self.rotor1.step()
        self.assertEqual(self.rotor1.window, "R")
        self.assertEqual(self.rotor2.window, "C")
    
    def test_step_doublestep(self):
        # when rotor2 is at E,
        # stepping rotor1 will cause all three rotors to rotate
        self.rotor1.change_setting("Q")
        self.rotor2.change_setting("D")
        self.rotor3.change_setting("A")

        self.rotor1.step()
        self.assertEqual(self.rotor1.window, "R")
        self.assertEqual(self.rotor2.window, "E")
        self.assertEqual(self.rotor3.window, "A")

        self.rotor1.step()
        self.assertEqual(self.rotor1.window, "S")
        self.assertEqual(self.rotor2.window, "F")
        self.assertEqual(self.rotor3.window, "B")
    
    def test_step_no_doublestep(self):
        self.rotor3.change_setting("V")
        with patch.object(self.rotor3, "step") as step3:
            self.rotor2.step()
            self.assertEqual(step3.call_count, 0)

    def test_encode_letter_as_input(self):
        "Check that letter inputs are dealt with properly."
        ret = self.rotor3.encode_letter("Q")
        self.assertEqual(ret, 4)
        with self.assertRaises(TypeError):
            self.rotor2.encode_letter("AB")

    def test_encode_printit(self):
        "Check the printit works."
        self.rotor1.encode_letter("Q", printit=True)
        self.assertEqual(self.capturedOutput.getvalue(), "Rotor I: input = Q, output = X\n")
        
    def test_encode_call_next_rotor(self):
        "Check that calling encode_letter will call the encode_letter of the next rotor."
        with patch.object(self.rotor1, "encode_letter") as encode1:
            with patch.object(self.rotor3, "encode_letter") as encode3:
                self.rotor2.encode_letter(4)
                self.assertEqual(encode3.call_count, 1)
                self.assertEqual(encode1.call_count, 0)
    
    def test_encode_call_prev_rotor(self):
        """Check that calling encode_letter with forward=False 
        will call the encode_letter of previous rotor."""
        with patch.object(self.rotor1, "encode_letter") as encode1:
            with patch.object(self.rotor3, "encode_letter") as encode3:
                self.rotor2.encode_letter(24, forward=False)
                self.assertEqual(encode1.call_count, 1)
                self.assertEqual(encode3.call_count, 0)

    def test_encode_return_next_rotor(self):
        """Check that encode_letter correct returns the
        return value of next_rotor.encode_letter."""
        self.assertEqual(self.rotor1.encode_letter(6), 24)
        self.assertEqual(self.rotor3.encode_letter(6, forward=False), 11)

    def test_encode_return(self):
        "Returning number vs. letter from encode_letter"
        ret = self.rotor3.encode_letter(3, return_letter=True)
        self.assertEqual(ret, "J")
        

    def test_change_setting(self):
        self.rotor1.change_setting("c")
        self.assertEqual(self.rotor1.window, "C")
        self.assertEqual(self.rotor1.offset, 2)

class TestReflector(unittest.TestCase):

    def setUp(self):
        self.reflector = Reflector()
    
    def test_repr(self):
        ret = str(self.reflector)
        expected = "Reflector wiring: \n{'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L', 'H': 'D', 'I': 'P', 'J': 'X', 'K': 'N', 'L': 'G', 'M': 'O', 'N': 'K', 'O': 'M', 'P': 'I', 'Q': 'E', 'R': 'B', 'S': 'F', 'T': 'Z', 'U': 'C', 'V': 'W', 'W': 'V', 'X': 'J', 'Y': 'A', 'Z': 'T'}"
        self.assertEqual(ret, expected)

class TestPlugboard(unittest.TestCase):

    def setUp(self):
        self.plug = Plugboard(['XY', "MN"])
        # set stdout to capturedOutput
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput
    
    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_constructor_noSwap(self):
        plug = Plugboard(None)
        self.assertEqual(len(plug.swaps), 0)
        plug2 = Plugboard([])
        self.assertEqual(len(plug2.swaps), 0)
    
    def test_constructor_swap(self):
        self.assertEqual(len(self.plug.swaps), 4)
        self.assertEqual(self.plug.swaps['X'], 'Y')
        self.assertEqual(self.plug.swaps['Y'], 'X')
        self.assertEqual(self.plug.swaps['M'], 'N')
        self.assertEqual(self.plug.swaps['N'], 'M')
    
    def test_repr(self):
        ret = str(self.plug)
        expected = "X <-> Y\nM <-> N"
        self.assertEqual(ret, expected)
    
    def test_update_replace(self):
        self.plug.update_swaps(['AB'], replace=True)
        self.assertEqual(len(self.plug.swaps), 2)
        self.plug.update_swaps(['MN', 'ZR'])
        self.assertEqual(len(self.plug.swaps), 6)
    
    def test_update_noNewSwap(self):
        self.plug.update_swaps(None)
        self.assertEqual(len(self.plug.swaps), 4)
        self.plug.update_swaps("uvw")
        self.assertEqual(len(self.plug.swaps), 4)
    
    def test_update_moreThanSix(self):
        self.plug.update_swaps(["AB","CD","EF","GH","IJ","KL","MN"])
        expected = 'Only a maximum of 6 swaps is allowed.\n'
        self.assertEqual(self.capturedOutput.getvalue(), expected)
        

class TestMachine(unittest.TestCase):

    def setUp(self):
        self.enigma1 = Enigma(key="EFG", swaps=["MN"], rotor_order=["I","III","II"])
        self.enigma2 = Enigma()
        # set stdout to capturedOutput
        self.capturedOutput = io.StringIO()
        sys.stdout = self.capturedOutput
    
    def tearDown(self):
        sys.stdout = sys.__stdout__
    
    def test_constructor_maxLen(self):
        with self.assertRaises(ValueError):
            Enigma(key="ABCD")
        
    def test_constructor_attributes(self):
        with patch("machine.Plugboard") as plugboard:
            myEnigma = Enigma(key="ABC", swaps=["XY"])
            attr = hasattr(myEnigma, "key") \
                and hasattr(myEnigma, "rotor_order") \
                and hasattr(myEnigma, "reflector") \
                and hasattr(myEnigma, "plugboard") \
                and hasattr(myEnigma, "l_rotor") \
                and hasattr(myEnigma, "m_rotor") \
                and hasattr(myEnigma, "r_rotor")
            self.assertTrue(attr)
            plugboard.assert_called_once_with(["XY"])

    def test_repr(self):
        expected = "Keyboard <-> Plugboard <->  Rotor I <-> Rotor  III <-> Rotor  II <-> Reflector \nKey:  + EFG"
        ret = str(self.enigma1)
        self.assertEqual(ret, expected)

    def test_encipher_error(self):
        with self.assertRaises(ValueError):
            self.enigma1.encipher("asdhihsihoi2")
        self.enigma1.encipher(ALPHABET + ALPHABET.lower())

    def test_encipher(self):
        with patch.object(self.enigma1, "encode_decode_letter") as ed:
            ed.return_value = "C"
            cipher = self.enigma1.encipher(" he l lo    ")
            self.assertEqual(ed.call_count, 5)
            self.assertEqual(cipher, "CCCCC")
    
    def test_decipher(self):
        with patch.object(self.enigma1, "encipher") as en:
            en.return_value = "deciphered"
            cipher = self.enigma1.decipher(" he llo    ")
            self.assertEqual(en.call_count, 1)
            self.assertEqual(cipher, "deciphered")
    
    def test_decipher_letterCase(self):
        letterY = self.enigma2.decipher("y")
        newEnigma = Enigma()
        newEnigma.plugboard.update_swaps(["XY"], replace=True)
        letterX = newEnigma.decipher("x")
        self.assertEqual(letterY, letterX)

    def test_encode_decode_letter_error(self):
        with self.assertRaises(ValueError):
            self.enigma1.encode_decode_letter("_")
        
    def test_encode_decode_letter_plugboard(self):
        letterY = self.enigma1.encode_decode_letter("Y")
        newEnigma = Enigma(key="EFG", swaps=["MN"], rotor_order=["I","III","II"])
        newEnigma.plugboard.update_swaps(["XY"])
        letterX = newEnigma.encode_decode_letter("X")
        self.assertEqual(letterY, letterX)

    def test_encode_decode_letter_stepRotor(self):
        letterL = self.enigma1.encode_decode_letter("L")
        letterL2 = self.enigma1.encode_decode_letter("L")
        self.assertNotEqual(letterL, letterL2)

    def test_encode_decode_letter_rotor(self):
        """Pass letter through the rotors.
        Each rotor should be passed twice."""
        with patch.object(self.enigma1.r_rotor, "encode_letter") as en:
            self.enigma1.encode_decode_letter("C")
            self.assertEqual(en.call_count, 2)
        with patch.object(self.enigma1.m_rotor, "encode_letter") as en:
            self.enigma1.encode_decode_letter("C")
            self.assertEqual(en.call_count, 2)
        with patch.object(self.enigma1.l_rotor, "encode_letter") as en:
            self.enigma1.encode_decode_letter("C")
            self.assertEqual(en.call_count, 2)

    def test_encode_decode_letter_reflector(self):
        with patch.object(self.enigma1.r_rotor, "encode_letter") as enR:
            with patch.object(self.enigma1.l_rotor, "encode_letter") as enL:
                enR.return_value = 0
                self.enigma1.encode_decode_letter('C')
                enL.assert_called_with(24, forward=False)
                enR.return_value = 8
                self.enigma1.encode_decode_letter('C')
                enL.assert_called_with(15, forward=False)

    def test_encode_decode_letter_finalSwap(self):
        with patch.object(self.enigma1.l_rotor, "encode_letter") as enL:
            enL.return_value = 10       # K
            self.enigma1.plugboard.update_swaps(["CY","LK"])
            ret = self.enigma1.encode_decode_letter("C")
            self.assertEqual(ret, "L")
            
            # no final swap
            self.enigma1.plugboard.update_swaps([], replace=True)
            ret = self.enigma1.encode_decode_letter("C")
            self.assertEqual(ret, "K")

    def test_set_rotor_position_error(self):
        self.enigma1.set_rotor_position("invalid")
        self.assertEqual(self.capturedOutput.getvalue(), "Please provide a three letter position key such as AAA.\n")
        
    def test_set_rotor_position_error2(self):
        self.enigma1.set_rotor_position(123)
        self.assertEqual(self.capturedOutput.getvalue(), "Please provide a three letter position key such as AAA.\n")
        

    def test_set_rotor_position(self):
        with patch.object(self.enigma1.l_rotor, "change_setting") as chL:
            with patch.object(self.enigma1.m_rotor, "change_setting") as chM:
                with patch.object(self.enigma1.r_rotor, "change_setting") as chR:
                    self.enigma1.set_rotor_position("CFG")
                    chL.assert_called_once_with('C')
                    chM.assert_called_once_with('F')
                    chR.assert_called_once_with('G')
                    self.assertEqual(self.enigma1.key, "CFG")

    def test_set_rotor_position_print(self):
        self.enigma2.set_rotor_position("XYZ")
        self.assertEqual(self.capturedOutput.getvalue(), "")
        self.enigma1.set_rotor_position("DEF", printIt=True)
        self.assertEqual(self.capturedOutput.getvalue(), "Rotor position successfully updated. Now using DEF.\n")
    
    def test_set_rotor_order(self):
        self.enigma1.key = 'XYZ'
        with patch('machine.Rotor') as rotor:
            # note the patching happens in machine, not components!
            self.enigma1.set_rotor_order(['II','III','I'])
            rotor.assert_has_calls([call('II', 'X'),\
                                call('III', 'Y', self.enigma1.l_rotor),\
                                call('I', 'Z', self.enigma1.m_rotor)])
        
        self.enigma1.set_rotor_order(['II','III','I'])
        self.assertEqual(self.enigma1.m_rotor.prev_rotor, self.enigma1.r_rotor)
        self.assertEqual(self.enigma1.l_rotor.prev_rotor, self.enigma1.m_rotor)
    
    def test_set_plugs(self):
        with patch.object(self.enigma1.plugboard, "update_swaps") as update:
            self.enigma1.set_plugs(["CD","PO","HI"])
            update.assert_called_with(["CD","PO","HI"], False)
            self.enigma1.set_plugs(["TF"], replace=True)
            update.assert_called_with(["TF"], True)
        
    def test_set_plugs_print(self):
        self.enigma1.set_plugs(["AB"])
        self.assertEqual(self.capturedOutput.getvalue(), "")
        self.enigma1.set_plugs(["CD","PO","HI"], printIt=True)
        expected = "Plugboard successfully updated. New swaps are:\n" + str(self.enigma1.plugboard) + '\n'
        self.assertEqual(self.capturedOutput.getvalue(), expected)

    

if __name__ == "__main__":
    unittest.main()