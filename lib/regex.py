import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z][a-zA-Z]*([ \-'][a-zA-Z]+)*"
name_regex = re.compile(name)

phone_number =r"\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}"
phone_regex = re.compile(phone_number)

email_address = r"[A-z]([A-z0-9][\.]{0,1})+[A-z0-9]+@[A-z0-9]+\.[a-z]{2,}"
email_regex = re.compile(email_address)