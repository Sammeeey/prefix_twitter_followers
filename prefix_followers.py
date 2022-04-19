from sys import argv

script, filename, target_path = argv
print(target_path)

# open txt file with follower names (one on each line)
with open(filename, 'r') as f:
    # based on methods of File Objects: https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects
    f_list = list(f)
    # print(f_list)

at_list = []
for follower in f_list:
    at_list.append(f'@{follower}')
# print(at_list)

with open(f'{target_path}\prefixed_{filename}', 'w') as f:  # probably expects a windows path; doesn't matter whether \ at the end or not
    for follower in at_list:
        f.write(follower)

# loop over every line
    # at the beginning of every line insert a @ symbol
# save copy of follower text file with added @ symbols in target directory
# close follower text file