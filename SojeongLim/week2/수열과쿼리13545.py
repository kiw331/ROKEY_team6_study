# 1과 -1로만 이루어져 있는 길이가 N인 수열 A1, A2, ..., AN이 주어진다. 이때, 다음 쿼리를 수행하는 프로그램을 작성하시오.
# i j: Ai, Ai+1, ..., Aj로 이루어진 부분 수열 중에서 합이 0이면서 가장 긴 연속하는 부분 수열의 길이를 출력한다.

# 첫째 줄에 수열의 크기 N (1 ≤ N ≤ 100,000)이 주어진다.  6  7
# 둘째 줄에는 A1, A2, ..., AN이 주어진다. (Ai = 1 또는 -1)
# 셋째 줄에는 쿼리의 개수 M (1 ≤ M ≤ 100,000)이 주어진다.
# 넷째 줄부터 M개의 줄에는 쿼리 i, j가 한 줄에 하나씩 주어진다. (1 ≤ i ≤ j ≤ n)


#4
#1 3
#1 4
#1 5
#1 6

#1 1 1 -1 -1 -1
#1 -1 1 -1 1 1 -1 


def longestzerosum(data, a,b):
    lenmax = 0
    length = 0
    
    while a < b:
        zerosum = 0
        for i in range(a-1, b):
            zerosum += data[i]
            #print("zerosum: ", zerosum)

            if zerosum == 0:
                length = i - a + 2
                #print("length : ", length)

            if lenmax < length:
                lenmax = length
                #print("lenmax :",lenmax)
        a += 1
    
    return lenmax



n = int(input("입력할 수열의 갯수: "))
data = input("1과 -1로 구성된 수열을 입력하세요.").split()           #list값이 str상태. 바로 int로 받을 수 없을까?
for a in range(len(data)):
    data[a] = int(data[a])
#print(type(data[0])) 

m = int(input("쿼리 갯수: "))
i=[]
j=[]
for count in range(m):
    query = input("i, j를 입력하세요.(단, 1 ≤ i ≤ j ≤ n)  : ").split()   #쿼리 범위 입력
    i.append(int(query[0]))
    j.append(int(query[1]))


for count in range(m):
    #print(i[count], j[count])
    print(longestzerosum(data, i[count], j[count]))