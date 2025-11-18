import unittest
import script

# * Run: python3 -m unittest -v


class TestMain(unittest.TestCase):  # inheriting TestCase class

    def setUp(self):  # this method will run before starting all the other test methods
        print(f"Starting a method/test: {self}")

    def test_add(self):
        """This is the info for this particular test"""
        test_param = 10
        result = script.add(test_param)
        self.assertEqual(result, 15)

    def test_add2(self):
        test_param = "random string"
        result = script.add(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_add3(self):
        test_param = "random string"
        result = script.add(test_param)
        self.assertIsInstance(result, ValueError)

    def test_add4(self):
        test_param = None
        result = script.add(test_param)
        self.assertEqual(result, "Please enter number")

    def test_add5(self):
        test_param = ""
        result = script.add(test_param)
        self.assertEqual(result, "Please enter number")

    def tearDown(
        self,
    ):  # this method will run after every test method. Generally used to reset/cleaning up data variables.
        print("Cleaning up....")


if __name__ == "__main__":
    unittest.main()  # this will run the entire classes present in the file
