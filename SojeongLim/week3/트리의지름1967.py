# 문제
# 트리(tree)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.



# 이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.

# 입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.



# 트리의 노드는 1부터 n까지 번호가 매겨져 있다.

# 입력
# 파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 간선에 대한 정보는 세 개의 정수로 이루어져 있다. 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다. 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다. 루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.

# 출력
# 첫째 줄에 트리의 지름을 출력한다.

#######chat gpt 도움..


###수업시간에 배운 코드

'''
def my_dfs(graph, start_node):
    stack = []  # DFS는 스택을 사용
    visited = []  # 방문한 노드를 저장

    stack.append(start_node)  # 시작 노드를 스택에 추가

    while stack:
        node = stack.pop()  # 스택에서 pop (후입선출 LIFO)

        if node not in visited:
            visited.append(node)  # 방문 처리
            stack.extend(graph[node])  # 현재 노드의 인접 노드들을 추가

    print("dfs - ", visited)
    return visited

'''


def my_dfs(graph, start_node):
    stack = []
    visited = {node: -1 for node in graph}  # 방문 여부 및 거리 저장
    stack.append((start_node, 0))           # 스택에 (노드, 누적거리) 저장
    visited[start_node] = 0                 # 시작 노드는 거리 0

    farthest_node = start_node
    max_distance = 0

    while stack:
        node, dist = stack.pop()            #스택 마지막 데이터의 (노드, 거리)

        if dist > max_distance:
            max_distance = dist
            farthest_node = node

        for neighbor, weight in graph[node]:    #graph입력을 딕셔너리로 받음
            if visited[neighbor] == -1:         # 방문하지 않았으면 아직 거리가 -1
                visited[neighbor] = dist + weight
                stack.append((neighbor, dist + weight))

    return farthest_node, max_distance



# 입력
n = int(input().strip())                         
graph = {i: [] for i in range(1, n + 1)}

for _ in range(n - 1):                                   #딱히 변수를 지정할 필요가 없을 때(한 번 쓰고 말 때)사용, 노드가 n개일 때, 엣지는 최대 n-1개
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))                # 무방향 그래프(==양방향)

# 1. 루트(1번 노드)에서 가장 먼 노드 찾기
farthest_node, _ = my_dfs(graph, 1)

# 2. 가장 먼 노드에서 다시 DFS 수행하여 트리의 지름 찾기  <----이게 진짜!
_, tree_diameter = my_dfs(graph, farthest_node)


print(tree_diameter)



#######추가 설명
'''
       (1)
      /   \
   (2)    (3)
   /      /   \
 (4)    (5)   (6)
 /  \   /  \   /  \
(7) (8)(9)(10)(11)(12)


그래프 입력 모습
graph = {
    1: [(2, 3), (3, 2)],
    2: [(1, 3), (4, 5)],
    3: [(1, 2), (5, 11)],
    # ... 계속 이어짐
}


스택 쌓이는 과정
1번노드
스택: [(1, 0)]
방문: 1, 거리: 0
스택 추가: (2, 3), (3, 2)

->3번 노드
스택: [(2, 3), (3, 2)]
방문: 3, 거리: 2
스택 추가: (5, 13), (6, 11)

->6번 노드
스택: [(2, 3), (5, 13), (6, 11)]
방문: 6, 거리: 11
스택 추가: (11, 17), (12, 21)

->11번 노드
스택: [(2, 3), (5, 13), (11, 17)]
방문: 11, 거리: 17
(스택 변화 없음)

->5번 노드
스택: [(2, 3), (5, 13)]
방문: 5, 거리: 13
스택 추가: (9, 28), (10, 17)
-->...

'
