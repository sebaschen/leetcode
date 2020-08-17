'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

def read_data(num):
    _list=[]
    for _ in range(num):
        _list.append(input())
    return _list

def make_dict(problem_set):
    mapp=dict()

row_num, K=int(input().split()[0])
print(type(row_num),row_num)

print('Case {}:'.format(1))
#get the    
problem_set =read_data(row_num)    
print(problem_set)

