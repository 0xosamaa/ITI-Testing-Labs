def evaluate_student_level(score):
    if score < 0:
        return "Invalid"
    elif 0 <= score < 50:
        return "Failed"
    elif 50 <= score < 65:
        return "Passed"
    elif 65 <= score < 75:
        return "Good"
    elif 75 <= score < 85:
        return "V.Good"
    elif 85 <= score < 100:
        return "Excellent"
    else:
        return "In"

# Test Suite 1
def test_suite_1():
    # Test Case 1
    score = -10
    expected_output = "Invalid"
    assert evaluate_student_level(score) == expected_output

    # Test Case 2
    score = 30
    expected_output = "Failed"
    assert evaluate_student_level(score) == expected_output

# Test Suite 2
def test_suite_2():
    # Test Case 1
    score = 70
    expected_output = "Good"
    assert evaluate_student_level(score) == expected_output

    # Test Case 2
    score = 90
    expected_output = "Excellent"
    assert evaluate_student_level(score) == expected_output

# Run the test suites
test_suite_1()
test_suite_2()
