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

    def test_get_command_with_args(self):
        self.fail()
