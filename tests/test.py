import unittest
import sys
import helpers.config
from helpers.config import Config


class TestApp(unittest.TestCase):
    def setUp(self):
        pass

    def test_default_config_path(self):
        self.assertTrue(helpers.config.WINDOWS, msg='System not Win')
        print(helpers.config.WINDOWS)

    def test_init_env_config_path_available(self):
        data = Config.init_env_config_path()
        self.assertEqual(len(data), 5, msg='Some path not available')
        print('All path available')

    def test_init_env_config_path(self):
        data = Config.init_env_config_path()
        self.assertEqual(data[0], './', msg='System not Linux')

    @unittest.skipUnless(sys.platform.startswith('win'), 'requires Windows')
    def test_get_windows_system_disk(self):
        data = Config.get_windows_system_disk()
        self.assertRegex(data, 'C', msg='System disc not "C:" ')
        print(data)

    def test_get_verbosity_level(self):  # не уверен что правильно понял и применил assertLogs
        data = Config.get_verbosity_level()
        self.assertLogs(data, 'console')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
