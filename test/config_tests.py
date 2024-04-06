import unittest
import tempfile
import os
from pathlib import Path
from scripts.get_configs import get_configs

class ConfigTests(unittest.TestCase):

    def not_atest_get_config(self):
        with tempfile.TemporaryDirectory(
            prefix="tmp_",
            suffix="_test",
            dir="test") as tempdir:
            print(type(Path(tempdir)))
            print(Path(tempdir))

            # tmpfilepath = Path(tempdir)/"get_config_test.yaml"
            # with open(tmpfilepath, 'w') as tmpfile:
            #     tmpfile.write("something")
            # self.assertEqual(get_configs(Path(tempdir).relative_to(Path().cwd())), ["get_config_test.yaml"])

if __name__ == '__main__':
    unittest.main()