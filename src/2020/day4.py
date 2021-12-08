from utils.load_data import read_csv
import pandas as pd
import re


def passport_check_required_keys(passport: str) -> bool:
    # define rules
    required_fields = ['byr','iyr','hgt','eyr','ecl','hcl','pid']

    # get fields from passport
    field_list = passport.strip().split(' ')
    key_list = [kv.split(':')[0] for kv in field_list]

    # check if all required fields are present
    has_required_fields = set(required_fields).issubset(key_list)
    return has_required_fields


def passport_check_field_values(passport:str)->bool:
    # get fields from passport
    field_list = passport.strip().split(' ')

    # check each value
    for field in field_list:
        # get key/value pair
        key = field.split(':')[0].strip()
        value = field.split(':')[1].strip()

        # apply relevant rule
        if key=='byr':
            field_is_valid = (len(re.findall("[0-9]+", value)[0])==4 and int(value)>=1920 and int(value)<=2002)
        elif key=='iyr':
            field_is_valid = (len(re.findall("[0-9]+", value)[0])==4 and int(value)>=2010 and int(value)<=2020)
        elif key=='eyr':
            field_is_valid = (len(re.findall("[0-9]+", value)[0])==4 and int(value)>=2020 and int(value)<=2030)
        elif key=='hgt':
            if len(value)>=4: # value should have atleast 4 chars
                height_value = value[:-2]
                height_unit = value[-2:]
                if len(re.findall("[0-9]+", height_value)) > 0: # handle if height_value is empty or all letters
                    if len(re.findall("[0-9]+", height_value)[0]) == len(height_value): # height_value should only be digits
                        if height_unit=='cm':
                            field_is_valid = (int(height_value)>=150 and int(height_value)<=193)
                        elif height_unit=='in':
                            field_is_valid = (int(height_value)>=59 and int(height_value)<=76)
                        else:
                            field_is_valid = False
                    else:
                        field_is_valid = False
                else:
                    field_is_valid = False
            else:
                field_is_valid = False
        elif key=='hcl':
            field_is_valid = (value[0]=='#' and len(re.findall("[a-f0-9]+", value[1:])[0])==6)
        elif key=='ecl':
            field_is_valid = (len(value)==3 and value in ['amb','blu','brn','gry','grn','hzl','oth'])
        elif key=='pid':
            field_is_valid = (len(re.findall("[0-9]+", value)[0])==9)
        else: #non-required fields
            field_is_valid=True

        # there is no reason to check more fields if we found 1 invalid
        if field_is_valid==False:
            break

    return field_is_valid


def passport_check_validity(passport:str)->bool:
    # check if all required fields are present
    has_required_fields = passport_check_required_keys(passport)

    if has_required_fields:
        is_valid = passport_check_field_values(passport)
    else:
        is_valid = False
    
    return is_valid


def get_answer1(df: pd.DataFrame)->float:
    # initialize
    Nvalid = 0
    current_passport = ''

    # ensure dataframe ends on an empty row
    if not df.tail(1).isnull().values:
        df = df.append(pd.Series(dtype='float64'), ignore_index=True)

    # loop over rows
    for idx, row in df.iterrows():
        # if this row is a passport seperator (or last row), then evaluate current passport and reset
        if row.isnull().any():
            # check validity of current passport
            if passport_check_required_keys(current_passport):
                Nvalid+=1
            # reset passport and jump to next row
            current_passport = ''
            continue
        # if this row is not a passport seperator then concatenate passport info to current passport
        else:
            # add info to current passport
            current_passport = current_passport + ' ' + row.passport.lower()

    return Nvalid


def get_answer2(df: pd.DataFrame)->float:
    # initialize
    Nvalid = 0
    current_passport = ''

    # ensure dataframe ends on an empty row
    if not df.tail(1).isnull().values:
        df = df.append(pd.Series(dtype='float64'), ignore_index=True)

    # loop over rows
    for idx, row in df.iterrows():
        # if this row is a passport seperator (or last row), then evaluate current passport and reset
        if row.isnull().any():
            # check validity of current passport
            if passport_check_validity(current_passport):
                Nvalid+=1
            # reset passport and jump to next row
            current_passport = ''
            continue
        # if this row is not a passport seperator then concatenate passport info to current passport
        else:
            # add info to current passport
            current_passport = current_passport + ' ' + row.passport.lower()

    return Nvalid

if __name__ == "__main__":
    df = read_csv('data/day4.csv', col_names=['passport'], sep=',', skip_blank_lines=False)
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
