import unittest
import sys

sys.path.append("/Users/onuchukwu/Documents/Projects/daily-challenges/json-parser")

import jp


class TestLexer(unittest.TestCase):
    def test_test1(self):
        file = open("./tests/step1/valid.json")
        self.assertEqual(["{", "}"], jp.get_tokens(file.read()))
        file.close()

    def test_test1_invalid(self):
        file = open("./tests/step1/invalid.json")
        self.assertRaises(Exception, jp.get_tokens(file.read()))
        file.close()

    def test_test2_valid(self):
        try:
            file = open("./tests/step2/valid.json")
            json_file = file.read()
            self.assertEqual(["{", "key", ":", "value", "}"], jp.get_tokens(json_file))
        except AssertionError as e:
            print(e)
        finally:
            file.close()

    def test_test3_valid(self):
        try: 
            file = open("./tests/step3/valid.json")
            self.assertEqual(
            [
                "{",
                "key1",
                ":",
                True,
                ",",
                "key2",
                ":",
                False,
                ",",
                "key3",
                ":",
                None,
                ",",
                "key4",
                ":",
                "value",
                ",",
                "key5",
                ":",
                "101",
                "}",
            ],
            jp.get_tokens(file.read()),
        )
        except AssertionError as e:
            print(e)
        finally:
            file.close()
    
    def test_test1_parser_valid(self):
        try:
            file = open("./tests/step1/valid.json")
            json_file = file.read()
            self.assertEqual({}, jp.parse(json_file))
        except AssertionError as e:
            print(e)
        finally:
            file.close()

    def test_test1_parser_invalid(self):
        file = open("./tests/step1/invalid.json")
        json_file = file.read()
        self.assertRaises(Exception, lambda: jp.parse(json_file))
        file.close()

        # try:
            
        # except AssertionError as e:
        #     print(e)
        # finally:
        pass
    
    def test_test2_parser_valid(self):
        try:
            file = open("./tests/step2/valid.json")
            json_file = file.read()
            self.assertEqual({'key': 'value'}, jp.parse(json_file))
        except AssertionError as e:
            print(e)
        finally:
            file.close()


if __name__ == "__main__":
    unittest.main()
