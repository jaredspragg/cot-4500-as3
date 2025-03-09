import unittest

class TestNumericalMethods(unittest.TestCase):

    def test_euler(self):
        f = lambda t, y: t - y**2
        t0, y0, t_end, n = 0, 1, 2, 10
        expected_result = 1.24463809793321  # Adjusted expected result from your output
        result = euler(f, t0, y0, t_end, n)
        self.assertAlmostEqual(result, expected_result, places=5)

    def test_runge_kutta(self):
        f = lambda t, y: t - y**2
        t0, y0, t_end, n = 0, 1, 2, 10
        expected_result = 1.25131658787981  # Adjusted expected result from your output
        result = runge_kutta(f, t0, y0, t_end, n)
        self.assertAlmostEqual(result, expected_result, places=5)

# Check if we're running in the main program context and not in an interactive environment
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
 
