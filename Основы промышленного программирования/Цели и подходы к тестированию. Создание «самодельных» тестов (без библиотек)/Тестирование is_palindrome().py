from yandex_testing_lesson import is_palindrome


def test_is_palindrome():
    test_cases = [
        ("", True),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("aba", True),
        ("abc", False),
        ("racecar", True),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon", True),
        ("not a palindrome", False),
    ]
    for data, expected_output in test_cases:
        if is_palindrome(data) != expected_output:
            print("NO")
    print("YES")


test_is_palindrome()
