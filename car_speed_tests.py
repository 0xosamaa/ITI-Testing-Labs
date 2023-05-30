def calculate_speed_level(speed):
    if speed < 0:
        return "Invalid"
    elif 0 <= speed < 40:
        return "Low"
    elif 40 <= speed < 120:
        return "Normal"
    elif 120 <= speed < 200:
        return "High"
    elif 200 <= speed < 220:
        return "V.High"
    else:
        return "Invalid"

# Test Suite 1
def test_suite_1():
    # Test Case 1
    speed = -10
    expected_output = "Invalid"
    assert calculate_speed_level(speed) == expected_output

    # Test Case 2
    speed = 20
    expected_output = "Low"
    assert calculate_speed_level(speed) == expected_output

# Test Suite 2
def test_suite_2():
    # Test Case 1
    speed = 80
    expected_output = "Normal"
    assert calculate_speed_level(speed) == expected_output

    # Test Case 2
    speed = 150
    expected_output = "High"
    assert calculate_speed_level(speed) == expected_output

# Run the test suites
test_suite_1()
test_suite_2()
