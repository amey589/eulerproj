import string
s_lst = list(string.ascii_uppercase)
f = open("names.txt","rt")
lines = []
count = 0
for line in f:
    s = line
records = s.split(",")
print(len(records))
sorted_records = sorted(records)
print(sorted_records[0])
count = 1
total = 0
for record in sorted_records:
    record_sm = 0
    for c in list(record):
        if c in s_lst: 
            val = s_lst.index(c) + 1
            record_sm = record_sm + val
    record_score = count * record_sm 
    total = total + record_score
    print("record is {} record_score is {} total is {}".format(record,record_score,total))
    count = count + 1 
print(total)
