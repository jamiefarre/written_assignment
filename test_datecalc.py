from datecalc import duration, when
from datetime import datetime

# Calculates the difference between dates


# ten days difference
def test_10_days():
    # Arrange
    start_year = 2022
    start_month = 8
    start_day = 16
    end_year = 2022
    end_month = 8
    end_day = 26
    expected_output = 10

    # Act
    start_date = datetime(start_year, start_month, start_day)
    end_date = datetime(end_year, end_month, end_day)
    actual_output = duration(start_date, end_date)

    # Assert
    assert actual_output == expected_output

# 90 days difference


def test_90_days():
    # Arrange
    start_date = datetime(2022, 8, 1)
    end_date = datetime(2022, 10, 30)
    expected_output = 90

    # Act
    actual_output = duration(start_date, end_date)

    # Assert
    assert actual_output == expected_output


# Adds/subtracts dates to find the number of days

# adding a week (7 days)
def test_week():
    # Arrange
    start_year = 2022
    start_month = 8
    start_day = 16
    days_between = 7
    expected_year = 2022
    expected_month = 8
    expected_day = 23

    # Act
    start_date = datetime(start_year, start_month, start_day)
    expected_output = datetime(expected_year, expected_month, expected_day)
    actual_output = when(start_date, days_between)

    # Assert
    assert actual_output == expected_output


# adding fornight (14 days)
def test_fornight():
    # Arrange
    start_date = datetime(2022, 1, 31)
    days_between = 14
    expected_output = datetime(2022, 2, 14)

    # Act
    actual_output = when(start_date, days_between)

    # Assert
    assert actual_output == expected_output
