def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]

if __name__ == "__main__":
    test_num = 12321
    if is_palindrome(test_num):
        print(f"{test_num} is a palindrome!")
    else:
        print(f"{test_num} is NOT a palindrome!")
