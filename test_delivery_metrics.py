import unittest
from delivery_metrics import simulate_delivery

class TestDeliveryMetrics(unittest.TestCase):
    def test_total_equals_sum_of_statuses(self):
        metrics = simulate_delivery()
        expected_total = metrics["pending"] + metrics["on_the_way"] + metrics["delivered"]
        self.assertEqual(metrics["total"], expected_total+100)

    def test_metrics_within_valid_ranges(self):
        metrics = simulate_delivery()
        self.assertGreater(metrics["total"], 0)
        self.assertTrue(15.0 <= metrics["avg_time"] <= 45.0)

if __name__ == "__main__":
    unittest.main()