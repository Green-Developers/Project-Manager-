def is_palindrome(s):
    stack = []
    # فقط حروف و اعداد را نگه می‌داریم
    filtered_string = ''.join(char.lower() for char in s if char.isalnum())

    # اضافه کردن حروف به پشته
    for char in filtered_string:
        stack.append(char)

    # بازسازی رشته از پشته
    reversed_string = ''.join(stack.pop() for _ in range(len(stack)))

    # مقایسه رشته اصلی و معکوس شده
    return filtered_string == reversed_string


# Example Usage
print(is_palindrome("madam"))  
print(is_palindrome("hello"))  

