import re
text = '<div class="nam">中国</div>'
result = re.findall('<div class=".*">(.*)</div>', text)
print('Result',result)
regex = '<div class=".*">(.*)</div>'

# compile use
pattern = re.compile(regex)
result1 = re.findall(pattern, text)
print('Result1',result1)

