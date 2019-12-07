import re
max_repeat = 6
a = re.findall(f"([0-9])\\1{{1,{max_repeat}}}", str(333444))

print(a)