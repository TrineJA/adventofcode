from utils.load_data import read_csv
import pandas as pd
import re


def clean_data(df: pd.DataFrame)->pd.DataFrame:
    # clean df (remove bag and bags etc)
    for col in df.columns:
        df[col] = df[col].str.lower()
        df[col] = df[col].str.replace('bags','')
        df[col] = df[col].str.replace('bag','')
        df[col] = df[col].str.replace('.','')
        df[col] = df[col].str.strip()
    return df


def get_answer1(df: pd.DataFrame)->float:
    # clean data
    df = clean_data(df)

    # initialize
    inner_bags_to_find = 'shiny gold'
    bag_list = [] 
    # look through the bag hierarchy (we can max need Nrow look-ups)
    for i in range(len(df)):
        # where does the bags fit?
        df_bags_found = df[df.inner_bags.str.contains(inner_bags_to_find)]

        # if we did not find any bags, then we are done
        if len(df_bags_found)==0:
            break

        # add outer bags to result list and 
        outer_bags_list = df_bags_found.outer_bags.unique().tolist()
        bag_list.extend(outer_bags_list)

        #make new inner-bag search term
        inner_bags_to_find = '|'.join(outer_bags_list)

    # get unique outer bag count
    Nbags = len(set(bag_list))

    return Nbags


def get_answer2(df: pd.DataFrame)->float:
    # clean data
    df = clean_data(df)
    df['outer_bags'] = df['outer_bags'].str.replace(' ','_')

    # what does my bag contain:
    my_bag_content=dict(shiny_gold=1)
    items_added_since_last_iteration=dict(shiny_gold=1)

    # start walking through the bag hierarchy
    max_iter = 1000
    for idx in range(max_iter):
        # initialize new items
        my_new_items = dict() 
        # loop through items added to bag in previous iteration
        for bag_color in list(items_added_since_last_iteration):
            bag_count = items_added_since_last_iteration[bag_color]
            bag_content_list = df.query("outer_bags==@bag_color").inner_bags.values[0].split(',')
            #if this back is empty then continue to next new item
            if bag_content_list[0].strip()=='no other':
                continue
            # loop through content and add to my new bag:
            for _bag in bag_content_list:
                _bag = _bag.strip()
                _bag_count_one_bag = re.findall("[0-9]+", _bag)[0]
                _bag_count_total = int(_bag_count_one_bag) * bag_count
                _bag_color = _bag.replace(_bag_count_one_bag,'').strip().replace(' ','_')
                # if this bag already is in my bag then add count. else add bag to my bag
                if _bag_color in my_bag_content.keys():
                    my_bag_content[_bag_color] += _bag_count_total
                else:
                    my_bag_content.update({_bag_color:_bag_count_total})
                # update my new items
                if _bag_color in my_new_items.keys():
                    my_new_items[_bag_color] += _bag_count_total
                else:
                    my_new_items.update({_bag_color:_bag_count_total})
        # update view of what was added in this iteration
        items_added_since_last_iteration=my_new_items
        # if all new items check in this iteration was empty. then we got all the bags. Hoorray
        if len(items_added_since_last_iteration)==0:
            break

    #remove my shiny gold bag from the list and get number of bags
    del my_bag_content['shiny_gold']
    Nbags_in_my_bag = sum(my_bag_content.values())

    return Nbags_in_my_bag


if __name__ == "__main__":
    df = read_csv('data/day7.csv', col_names=['outer_bags','inner_bags'], sep='contain', engine='python')
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')
