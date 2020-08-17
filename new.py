x = "5 3 "

problem_set = ['100 -9 -1', 
                '-1 3 2', 
                '-9 2 3', 
                '2 5 1', 
                '3 3 4']
                
ans_list =[ ]
for i in problem_set:
    x = i.split()
    ans_list.append(x)

# row = len(ans_list)
# col = len(ans_list[0])
# for i in range(row):
#     for j in range(col):
#         #compare horizontally
#         if j ==0 or j==(col-1):
#            #only need to do vertical
#             x = ans_list[i][j]
#         if i==0 or i== (row-1):
#             #only need to do horizontal
#         else:
#             #horizontally and vertically
row_num=int(x.split()[0])
K = int(x.split()[1])
print(K)

result = []
def pairwiseSum(lst, n): 
    sum = 0; 
    for i in range(len(lst)-1): 
        # adding the alternate numbers 
        sum = int(lst[i]) + int(lst[i + 1])
        result.append(sum)

for j in range(len(ans_list)):
    pairwiseSum(ans_list[j],len(ans_list[j]))
        
print(sum(sorted(result, reverse=True)[:3]))

# x.pop(1)
# x = sum(int(number) for number in x)
# ans_list.append(x)
# K = 3 
# print(sorted(ans_list)[K-1:])
# ans = sum(sorted(ans_list)[K-1:])
# print(ans)