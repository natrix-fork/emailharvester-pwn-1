import re

re_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')

with open("emails.txt") as fh_in:
    with open("mailout.txt", "a+") as fh_out:
        for line in fh_in:
            match_list = re_pattern.findall(line)
            if match_list:
                fh_out.write(match_list[0]+"\r\n")

lines_seen = set() # holds lines already seen
outfile = open("out.txt", "w")
for line in open("mailout.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
