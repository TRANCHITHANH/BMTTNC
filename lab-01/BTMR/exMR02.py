import re
input_string = "-100#^sdfkj8902w3ir021@swf-20"
numbers = re.findall(r'-?\d+', input_string)
positive_sum = sum(int(num) for num in numbers if int(num) > 0)
negative_sum = sum(int(num) for num in numbers if int(num) < 0)
print(f"Giá trị dương: {positive_sum}. Giá trị âm: {negative_sum}.")
