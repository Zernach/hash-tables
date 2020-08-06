
# you have a bunch of records
# return all iOS students

records = [
    ("Scott", "iOS"),
    ("Nick", "iOS"),
    ("Ryan", "DS"),
    ("Jacob", "DS"),
    ("Chris", "DS"),
    ("Chris", "DS"),
    ("Christine", "web"),
    ("Anthony", "web"),
        ]

iOS = []
for record in records:
    if record[1] == 'iOS':
        iOS.append(record)

# let's make an index for instant access by some attribute or other
## some attribute we search by often

# key: attribute - track
# value: list of names

def build_index(records):
    indexed_records = {}

    for idx, record in enumerate(records): # tuple(idx, item)
        track = record[1]
        name = record[0]

        if track in indexed_records:
            indexed_records[track].append(name)

        else:
            indexed_records[track] = [name]

    return indexed_records

indexed_records = build_index(records)

print(indexed_records['iOS'])
print(indexed_records['DS'])