from unittest import TestCase

from music_bot import MinnesingerBot


class TestMinnesingerBot(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestMinnesingerBot, self).__init__(*args, **kwargs)
        self.mpd = MinnesingerBot()

    def test_get_bot_credentials(self):
        creds = self.mpd.get_bot_credentials()
        print(creds)
        self.assertTrue(creds.__len__() == 2)

    def test_get_command_with_args_on_normal_command(self):
        msg = "/command arg1 arg2 arg3"
        cmd, args = self.mpd.get_command_with_args(msg)
        print(cmd, args)
        self.assertTrue(cmd == "command")
        self.assertTrue(args == ["arg1", "arg2", "arg3"])

    def test_get_command_without_args(self):
        msg = "/command"
        cmd, args = self.mpd.get_command_with_args(msg)
        print(cmd, args)
        self.assertTrue(cmd == "command")
        self.assertTrue(args == [])

    def test_get_command_with_args_on_empty(self):
        msg = ""
        cmd, args = self.mpd.get_command_with_args(msg)
        print(cmd, args)
        self.assertTrue(cmd is None)
        self.assertTrue(args == [])

    def test_get_command_with_args_not_starting_with_command_char(self):
        msg = "command arg1 arg2"
        cmd, args = self.mpd.get_command_with_args(msg)
        print(cmd, args)
        self.assertTrue(cmd is None)
        self.assertTrue(args == [])