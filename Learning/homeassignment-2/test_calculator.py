from calculator import Calculator
import pytest

calc = Calculator()


class TestCalculator:
    addition_tests = [(1, 1, 2), (-1, 1, 0), (-1, -1, -2)]
    subtraction_tests = [(2, 1, 1), (2, 2, 0), (2, 3, -1)]
    multiplication_tests = [(3, 3, 9), (3, 0, 0), (3, -3, -9)]
    division_tests = [(6, 3, 2), (6, 2, 3), (6, 0, "Error: Division by zero is not allowed.")]

    @pytest.mark.parametrize("num_a, num_b, expected_result", addition_tests)
    def test_addition(self, num_a, num_b, expected_result):
        assert calc.addition(num_a, num_b) == expected_result

    @pytest.mark.parametrize("num_a, num_b, expected_result", subtraction_tests)
    def test_subtraction(self, num_a, num_b, expected_result):
        assert calc.subtraction(num_a, num_b) == expected_result

    @pytest.mark.parametrize("num_a, numb_b, expected_result", multiplication_tests)
    def test_multiplication(self, num_a, numb_b, expected_result):
        assert calc.multiplication(num_a, numb_b) == expected_result

    @pytest.mark.parametrize("num_a, num_b, expected_result", division_tests)
    def test_division(self, num_a, num_b, expected_result):
        assert calc.division(num_a, num_b) == expected_result
