import unittest
import sys
import helpers.config
from helpers.config import Config
import helpers.config as config


test_cfg = config.Config()


class TestApp(unittest.TestCase):

    @unittest.skipUnless(sys.platform.startswith('win'), 'requires Windows')
    def test_default_config_path(self):
        self.assertTrue(helpers.config.WINDOWS, msg='System not Win')
        print(helpers.config.WINDOWS)

    def test_init_env_config_path_available(self):
        data = Config.init_env_config_path()
        self.assertEqual(len(data), 5, msg='Some path not available')
        print('All path available')

    @unittest.skipUnless(sys.platform.startswith('win'), 'requires Windows')
    def test_get_windows_system_disk(self):
        data = Config.get_windows_system_disk()
        self.assertRegex(data, 'C', msg='System disc not "C:" ')
        print(data)

    def test_get_verbosity_level(self):  # не уверен что правильно понял и применил assertLogs
        data = Config.get_verbosity_level()
        self.assertLogs(data, 'console')

    def test_level_none(self):
        levels = 'critical, error, warning, info, debug'
        self.assertEqual(Config.get_verbosity_level(level=None), levels, )

    def test_all_levels(self):
        self.assertEqual(Config.get_verbosity_level(level='console'), 10)
        self.assertEqual(Config.get_verbosity_level(level='debug'), 10)
        self.assertEqual(Config.get_verbosity_level(level='info'), 20)
        self.assertEqual(Config.get_verbosity_level(level='warning'), 30)
        self.assertEqual(Config.get_verbosity_level(level='error'), 40)
        self.assertEqual(Config.get_verbosity_level(level='critical'), 50)


if __name__ == '__main__':
    unittest.main()
