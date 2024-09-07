def is_palindrome(s):
    # إزالة المسافات وتحويل السلسلة إلى أحرف صغيرة
    s = s.replace(" ", "").lower()
    # مقارنة السلسلة بالعكس
    return s == s[::-1]

# قراءة الإدخال من المستخدم
input_string = input()

# التحقق من كون السلسلة باليندروم
if is_palindrome(input_string):
    print("YES")
else:
    print("NO")

