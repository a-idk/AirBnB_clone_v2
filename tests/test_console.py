#!/usr/bin/python3

"""
Title: Unittest for Console.py
File Author: @a_idk
"""

import os
from io import StringIO
from console import HBNBCommand
import unittest
from unittest.mock import patch
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """ Testing the HBNB command interpreter """
    # defining the setup and tearDown class
    @classmethod
    def setUpClass(cls):
        """ setup class """
        try:
            os.rename("file.json", "tmp")  # renaming the file.json
        except IOError:
            pass

        cls.HBNB = HBNBCommand()  # creating instance of class HBNB

    @classmethod
    def tearDownClass(cls):
        """ teardown class """
        try:
            os.rename("tmp", "file.json")  # rename back to file.json
        except IOError:
            pass
        del cls.HBNB  # deleting the instance of class HBNB

    def setUp(self):
        """ setup method """

        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ teardown method """
        try:
            os.remove("file.json")
        except IOError:
            pass

    # --------------------- Create command Method ----------------------
    def test_Docreate_command(self):
        """Testing the Do create command """
        # 1. Checking the ID of a BaseModel instance
        with patch("sys.stdout", new=StringIO()) as fd:
            self.HBNB.onecmd("create BaseModel")
            base_model = fd.getvalue().strip()

    def test_errorDoCreate(self):
        """ Testing for errors in create cmd """
        # 1. missing class name
        with patch("sys.stdout", new=StringIO()) as fd:
            self.HBNB.onecmd("create")
            self.assertEqual(
                " missing class name \n",
                fd.getvalue()
                )

        # 2. no class
        with patch("sys.stdout", new=StringIO()) as fd:
            self.HBNB.onecmd("create chakaboom")
            self.assertEqual(
                " class not valid! \n",
                fd.getvalue()
                )

    # --------------------- Created Instances ----------------------
    def test_CreateInstances(self):
        # 0. Checking the ID of a BaseModel instance
        with patch("sys.stdout", new=StringIO()) as fd:
            self.HBNB.onecmd("create BaseModel")
            base_model = fd.getvalue().strip()
        # 1. Amenity instance and ID
        with patch("sys.stdout", new=StringIO()) as fd:
            self.HBNB.onecmd("create Amenity")
            amenity_instance = fd.getvalue().strip()
        # 2. City instance and ID
        with patch("sys.stdout", new=StringIO()) as fd:
            self.HBNB.onecmd("create City")
            city_instance = fd.getvalue().strip()
        # 3. Place instance and ID
        with patch("sys.stdout", new=StringIO()) as fd:
            self.HBNB.onecmd("create Place")
            place_instance = fd.getvalue().strip()
        # 4. Review instance and ID
        with patch("sys.stdout", new=StringIO()) as fd:
            self.HBNB.onecmd("create Review")
            review_instance = fd.getvalue().strip()
        # 5. State instance and ID
        with patch("sys.stdout", new=StringIO()) as fd:
            self.HBNB.onecmd("create State")
            state_instance = fd.getvalue().strip()
        # 6. User instance and ID
        with patch("sys.stdout", new=StringIO()) as fd:
            self.HBNB.onecmd("create User")
            user_instance = fd.getvalue().strip()

            # --------------------- Create Command II ----------------------
            '''def test_kwargs_CreateCMD(self):
            """ Testing the create command with kwargs """
            with patch("sys.stdout", new=StringIO()) as fd:
            call = (
            f'create Place city_id="0001" name="My_house" number_rooms=4
            latitude=37.77 longitude=43.434'
                    )
            self.HBNB.onecmd(call)
            place_instance = fd.getvalue().strip()

            with patch("sys.stdout", new=StringIO()) as fd:
            self.HBNB.onecmd("all Place")
            result = fd.getvalue()
            self.assertIn(place_instance, result)
            self.assertIn("'city_id': '0001'", result)
            self.assertIn("'name': 'My house'", result)
            self.assertIn("'number_rooms': 4", result)
            self.assertIn("'latitude': 37.77", result)
            self.assertIn("'longitude': 43.434", result)
            '''

            # --------------------- Do All Command Tests ----------------------
            # def test_DoAll_command(self):
            # 1. Check if Amenity instance present in output of command
            with patch("sys.stdout", new=StringIO()) as fd:
                self.HBNB.onecmd("all Amenity")
                self.assertIn(amenity_instance, fd.getvalue())
            # 2. Check if BaseModel instance present in output of command
            with patch("sys.stdout", new=StringIO()) as fd:
                self.HBNB.onecmd("all BaseModel")
                self.assertIn(base_model, fd.getvalue())
            # 3. Check if City instance present in output of command
            with patch("sys.stdout", new=StringIO()) as fd:
                self.HBNB.onecmd("all City")
                self.assertIn(city_instance, fd.getvalue())
            # 4. Check if Place instance present in output of command
            with patch("sys.stdout", new=StringIO()) as fd:
                self.HBNB.onecmd("all Place")
                self.assertIn(place_instance, fd.getvalue())
            # 5. Check if Review instance present in output of command
            with patch("sys.stdout", new=StringIO()) as fd:
                self.HBNB.onecmd("all Review")
                self.assertIn(review_instance, fd.getvalue())
            # 6. Check if State instance present in output of command
            with patch("sys.stdout", new=StringIO()) as fd:
                self.HBNB.onecmd("all State")
                self.assertIn(state_instance, fd.getvalue())
            # 7. Check if User instance present in output of command
            with patch("sys.stdout", new=StringIO()) as fd:
                self.HBNB.onecmd("all User")
                self.assertIn(user_instance, fd.getvalue())

    '''
    def test_kwargs_CreateCMD(self):
        """ Testing the create command with kwargs """
        with patch("sys.stdout", new=StringIO()) as fd:
            call = (f'create Place city_id="0001" name="My_house" number_rooms=4 latitude=37.77 longitude=43.434')
            self.HBNB.onecmd(call)
            place_instance = fd.getvalue().strip()
            with patch("sys.stdout", new=StringIO()) as fd:
                self.HBNB.onecmd("all Place")
                result = fd.getvalue()
                self.assertIn(place_instance, result)
                self.assertIn("'city_id': '0001'", result)
                self.assertIn("'name': 'My house'", result)
                self.assertIn("'number_rooms': 4", result)
                self.assertIn("'latitude': 37.77", result)
                self.assertIn("'longitude': 43.434", result)
    '''


if __name__ == "__main__":
    unittest.main()
