import unittest
from acl.paper import Paper
from acl.result_set import ResultSet


class TestResultSet(unittest.TestCase):

    def test_to_dataframe(self):
        result = {
            "X01":
            [
                Paper("X01-001", "Paper1", ("A", "B", "C")),
                Paper("X01-002", "Paper2", ("B", "C")),
                Paper("X01-003", "Paper3", ("A", "C"))
            ]
        }

        rs = ResultSet(result, False)
        df = rs.to_dataframe()
        self.assertEqual(len(df), 3)
