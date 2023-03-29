import unittest
import sys

sys.path.append("..")
from Semabox import get_info_system


class TestGetInfoSystem(unittest.TestCase):
    def test_get_info_system(self):
        info_system = get_info_system()

        # Vérifier si le résultat est un dictionnaire
        self.assertIsInstance(info_system, dict)

        # Vérifier si les clés attendues sont présentes
        expected_keys = {
            "num_cpus",
            "cpu_utilization",
            "ram_size_go",
            "disks",
            "num_disks",
            "uptime_hours",
            "os_name",
        }
        self.assertSetEqual(set(info_system.keys()), expected_keys)

        # Vérifier si les valeurs sont du bon type
        self.assertIsInstance(info_system["num_cpus"], int)
        self.assertIsInstance(info_system["cpu_utilization"], float)
        self.assertIsInstance(info_system["ram_size_go"], str)
        self.assertIsInstance(info_system["disks"], int)
        self.assertIsInstance(info_system["num_disks"], int)
        self.assertIsInstance(info_system["uptime_hours"], int)
        self.assertIsInstance(info_system["os_name"], str)


if __name__ == "__main__":
    unittest.main()
