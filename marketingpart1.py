import re
regex = re.compile(r".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?) (HTTP.*\"|\") ([2-5]0[0-9]) .*")

for line in open('local_copy.log'):
    elements = regex.split(line)

with open("local_copy.log") as f:
    contents = f.read()
    count = contents.count("1995")
    print("Number of requests from last year:", count)

    count2 = contents.count("GET")
    print("Number of total requests:", count2)
