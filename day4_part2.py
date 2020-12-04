import re

input_string = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

required_fields = {'byr': r'^19[2-9]\d|200[0-2]$',
                   'iyr': r'^20(1\d|20)$',
                   'eyr': r'^20(2\d|30)$',
                   'hgt': r'^(1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in$',
                   'hcl': r'^#[0-9a-f]{6}$',
                   'ecl': r'^amb|blu|brn|gry|grn|hzl|oth$',
                   'pid': r'^\d{9}$'}

passports = input_string.split('\n\n')

valid = 0

for passport in passports:
    fields = dict(iter(x.split(':')) for x in re.split(r'\s', passport))

    if all(key in fields and re.fullmatch(rgx, fields[key]) for key, rgx in required_fields.items()):
        valid += 1

print(valid)
