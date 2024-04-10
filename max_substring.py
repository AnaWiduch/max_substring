
s = input()

var = s[0]  # Initialize the most frequent character with the first character in the string
count = 1  # Initialize the count of consecutive characters
m = 1  # Initialize the maximum count of consecutive characters


for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        if m <= count:
            m = count
            var = s[i - 1]
        count = 1

# Check if the count of consecutive characters for the last character is greater than or equal to the maximum count
if m <= count:
    print(s[-1])
    print(count)
else:
    print(var)
    print(m)
