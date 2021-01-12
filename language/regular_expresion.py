import re

pattern = '^miw-(betca|spring|python)$'
test_string = 'miw-spring'
result = re.match(pattern, test_string)

if result:
    print("Search successful.")
else:
    print("Search unsuccessful.")

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)


