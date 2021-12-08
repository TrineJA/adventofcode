from utils.load_data import read_csv
import pandas as pd
import re


def evaluate_string_left_to_right(expr: str)->int:
    # walk through string
    numbers = [s for s in expr.split() if s.isdigit()]
    operators = [s for s in expr.split() if not s.isdigit()]
    # initialize left hand-side
    lhs = numbers[0]
    for idx_op, operation in enumerate(operators):
        rhs = numbers[idx_op+1]
        # calculate new left hand side
        lhs = str(eval(lhs + operation + rhs))
    result = int(lhs)
    return result


def evaluate_string_addition_before_multiplication(expr: str)->int:
    # do sums
    Naddition = expr.count('+')
    for itt in range(Naddition):
        # find rhs and lhs
        rhs = expr.split('+')[0].split('*')[-1]
        lhs = expr.split('+')[1].split('*')[0]
        sub_expr = rhs + '+' + lhs
        sub_res = str(eval(sub_expr))
        #update expr
        expr = expr.replace(sub_expr, sub_res, 1)
    # do multiplications
    Nmult = expr.count('*')
    for itt in range(Nmult):
        # find rhs and lhs
        rhs = expr.split('*')[0]
        lhs = expr.split('*')[1]
        sub_expr = rhs + '*' + lhs
        sub_res = str(eval(sub_expr))
        #update expr
        expr = expr.replace(sub_expr, sub_res, 1)
    res = int(expr)
    return res


def get_answer1(df: pd.DataFrame)->float:
    sumval = 0
    for _, row in df.iterrows():
        expr = row.expr
        # how many brackets do we need to handle and their opening_index
        bracket_open_idx = [i for i, a in enumerate(expr) if a == '(']
        # find the left most opening bracket and evaluate
        for open_idx in sorted(bracket_open_idx, reverse=True):
            #find expression within nearest closing brackets
            sub_expr = expr[open_idx:]
            close_idx = sub_expr.find(')')
            sub_expr = sub_expr[:close_idx+1]
            #evaluate sub-expresion
            sub_res = evaluate_string_left_to_right(sub_expr[1:-1])
            #replace result in expr
            expr = expr.replace(sub_expr,str(sub_res), 1)

        # calculate final result and add to running sum
        res = evaluate_string_left_to_right(expr)
        sumval += res
    return sumval


def get_answer2(df: pd.DataFrame)->float:
    sumval = 0
    for _, row in df.iterrows():
        expr = row.expr
        # how many brackets do we need to handle and their opening_index
        bracket_open_idx = [i for i, a in enumerate(expr) if a == '(']
        # find the left most opening bracket and evaluate
        for open_idx in sorted(bracket_open_idx, reverse=True):
            #find expression within nearest closing brackets
            sub_expr = expr[open_idx:]
            close_idx = sub_expr.find(')')
            sub_expr = sub_expr[:close_idx+1]
            #evaluate sub-expresion
            sub_res = evaluate_string_addition_before_multiplication(sub_expr[1:-1])
            #replace result in expr
            expr = expr.replace(sub_expr,str(sub_res), 1)
        # calculate final result and add to running sum
        res = evaluate_string_addition_before_multiplication(expr)
        sumval += res
    return sumval


if __name__ == "__main__":
    df = read_csv('data/day18.csv', col_names=['expr'], sep=',')
    answer1 = get_answer1(df)
    print(f'Todays first answer is: {answer1}')
    answer2 = get_answer2(df)
    print(f'Todays second answer is: {answer2}')    
