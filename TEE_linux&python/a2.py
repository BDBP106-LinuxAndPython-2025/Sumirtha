import re
#Given text
text= "My email addresses are jnagesh@ibab.ac.in and test_info@gmail.com"
#RE for email pattern
pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
#finding the pattern in text
emails = set(re.findall(pattern, text))
print("Found emails:", emails)