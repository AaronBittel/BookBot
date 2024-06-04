#!/usr/bin/python3 

def sort_on(dict):
    return dict["count"]

character_count = {}
filepath = "books/frankenstein.txt"

with open(filepath, "r") as f:
    file_contents = f.read()

words = file_contents.split()

for word in words:
    for char in word:
        c = char.lower()
        if not c.isalpha():
            continue
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1

character_count_list = [{"name": c, "count": count} for c, count in character_count.items()]
character_count_list.sort(reverse=True, key=sort_on)

print(f" --- Begin report of {filepath} --- ")
print(f" {len(character_count_list)} found in the document")

for char_info in character_count_list:
    print(f" The '{char_info['name']}' was found {char_info['count']} times")

print(" --- End report ---")
