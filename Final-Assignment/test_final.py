# test_final.py

from final_functions import calculate_min_max_sum, find_date_in_pi


def test_calculate_min_max_sum():
    result = calculate_min_max_sum(15, 8, 27, 42, 12)
    assert result == (8, 42, 104)


def test_find_date_in_pi():
    birth_date_to_check = "0219"  # February 19
    result = find_date_in_pi(birth_date_to_check)
    assert "not found" in result


def test_find_date_in_pi_invalid():
    birth_date_to_check = "0219"  # Invalid birth date (empty string)
    result = find_date_in_pi(birth_date_to_check)
    assert "not found" in result


# Add more tests as needed

if __name__ == "__main__":
    # Run tests using pytest from the command line
    import pytest

    pytest.main(["-v", "test_final.py"])
