import unittest


class TestSortPos(unittest.TestCase):

    def test_sort_pos(self):
        messy = [3, -5, 9, -2, 8]
        clean = [3, 8, 9]
        self.assertEqual(self.sort_pos(messy), clean)

    def sort_pos(self, numbers):
        for item in numbers:
            if item < 0:
                numbers.remove(item)
        numbers.sort()
        return numbers

if __name__ == "__main__":
    unittest.main()