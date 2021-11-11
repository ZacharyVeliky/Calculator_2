"""Testing the Calculator"""
import pytest
from calc.history.history import Calculations
from calc.operations.addition import Addition


@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


@pytest.fixture
def setup_addition_fixture():
    """define a function that will run each time you pass it to a test"""
    # pylint: disable=redefined-outer-name
    addition = Addition.add(1, 2)
    Calculations.add_calculation(addition)


def test_add_calculation_to_history(clear_history_fixture, setup_addition_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1


def test_clear_calculation_history(clear_history_fixture, setup_addition_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() is True


def test_get_calculation(clear_history_fixture, setup_addition_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation(0) == 3


def test_get_calc_last_result_value(clear_history_fixture, setup_addition_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation_result_value() == 3


def test_get_calculation_first(clear_history_fixture, setup_addition_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation() == 3


def test_history_count(clear_history_fixture, setup_addition_fixture):
    """Testing getting the count of calculations from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1


def test_get_calc_last_result_object(clear_history_fixture, setup_addition_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # This test if it returns the last calculation as an object
    assert isinstance(Calculations.get_last_calculation_object(), Addition) is False