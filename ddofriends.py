import configparser
import json

filename = r'C:\ProgramData\Turbine\DDO Unlimited\FriendsList.ini'

with open('friends.json', 'r') as fh:
    friends = json.load(fh)

print('There are ', len(friends), ' entries in the friends list.')

config = configparser.RawConfigParser()
config.optionxform = str

i = -1
for f in friends:
    i += 1

    # Maximum friend list size is 150
    if i >= 150:
        break

    print(i, ': ', f)

    if 'name' not in f:
        continue

    if 'active' in f and not f['active']:
        continue

    if 'note' in f:
        note = f['note']
    elif 'player' in f:
        note = f['player']
    else:
        note = ''

    section_name = 'Friend' + str(i)
    config.add_section(section_name)
    config.set(section_name, 'Name', f['name'])
    config.set(section_name, 'Note', note)


with open(filename, 'w') as fh:
    config.write(fh)