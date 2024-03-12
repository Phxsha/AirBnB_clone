#!/usr/bin/python3
import unittest
from unittest.mock import patch
import io
import sys
import os
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Test cases for the HBNBCommand class in console.py.
    """

    def setUp(self):
        """
        Set up test environment before each test case.
        """
        self.console = HBNBCommand()

    def tearDown(self):
        """
        Clean up test environment after each test case.
        """
        del self.console

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_command(self, mock_stdout):
        """
        Test help command.
        """
        with patch('builtins.input', return_value="help"):
            self.console.cmdloop()
            self.assertIn("Documented commands", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_quit_command(self, mock_stdout):
        """
        Test quit command.
        """
        with patch('builtins.input', return_value="quit"):
            self.assertTrue(self.console.cmdloop())
            self.assertIn("Exiting HolbertonBnB console...", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_eof_command(self, mock_stdout):
        """
        Test EOF command.
        """
        with patch('builtins.input', side_effect=KeyboardInterrupt):
            self.assertTrue(self.console.cmdloop())
            self.assertIn("", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_empty_line(self, mock_stdout):
        """
        Test empty line.
        """
        with patch('builtins.input', return_value=""):
            self.assertFalse(self.console.cmdloop())
            self.assertEqual("", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()

