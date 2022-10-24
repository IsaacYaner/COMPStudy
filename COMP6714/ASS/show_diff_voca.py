import json
with open('vocabularies') as f:
    vocabulary = json.load(f)
with open('vocabularies_OLD') as f:
    vocabulary_old = json.load(f)

old_more = [x for x in vocabulary_old if x not in vocabulary]
new_more = [x for x in vocabulary if x not in vocabulary_old]
print(sorted(old_more)[4:])
print(sorted(new_more))