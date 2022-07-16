# 활용도가 높은 자료구조: 트리 



## 트리

* 계측적인 구조를 표현할 때 사용할 수 있는 자료구조

![3-1](C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\3-1.PNG)



## 이진 탐색 트리

* 이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조
* 이진 탐색 트리의 특징: **왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드**

<img src="C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\3-2.PNG" alt="3-2" style="zoom:80%;" />

* 데이터를 탐색하는 과정

  * 찾고자하는 원소 : 37
  * [STEP 1] 루트 노드부터 방문하여 탐색을 진행합니다.

  <img src="C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\3-3.PNG" alt="3-3" style="zoom:50%;" />

  * [STEP 2] 현재 노드와 값을 비교합니다.

  <img src="C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\3-4.PNG" alt="3-4" style="zoom:50%;" />

  * [STEP 3] 현재 노드와 값을 비교합니다.

  <img src="C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\3-5.PNG" alt="3-5" style="zoom:50%;" />

## 트리의 순회

* 트리 자료구조에 포함된 노드를 특정한 방법으로 한 번씩 방문하는 방법을 의미합니다.
  * 트리의 정보를 시각적으로 확인할 수 있습니다.
* 대표적인 트리 순회 방법은 다음과 같습니다.
  * 전위 순회 (pre-order traverse) : 루트를 먼저 방문합니다. 
  * 중위 순회 (in-order traverse) : 왼쪽 자식을 방문한 뒤에 루트를 방문합니다.
  * 후위 순회 (post-order traverse) : 오른쪽 자식을 방문한 뒤에 루트를 방문합니다.



<img src="C:\Users\여름\Desktop\학습자료\이러닝\[큐레이팅# 플러스] 최적의 코딩을 결정하는 기본 알고리즘\image\3-6.PNG" alt="3-6" style="zoom:67%;" />

* 전위 순회 (pre-order traverse) : A → B → D → E → C → F → G
* 중위 순회 (in-order traverse) : D → B → E → A → F → C → G
* 후위 순회 (post-order traverse) : D → E → B → F → G → C → A

* 위의 결과는 아래의 코드를 구현할 결과

  * 입력예시는 아래와 같음

  <img src="image/3-7.PNG" alt="3-7" style="zoom:50%;" />

## 트리의 순회 구현 예제

```python
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        
# 전위 순환 (Preorder Traversal)
def pre_order(node):
    print(node.data, end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.rigth_node != None:
        pre_order(tree[node.right_node])
        
# 중위 순회 (Inorder Traversal)
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.rigth_node != None:
        in_order(tree[node.right_node])

# 후위 순회 (Postorder Traversal)
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.rigth_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=' ')
    
n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == 'None':
        left_node = None
    if right_node == 'None':
    	right_node = None
    tree[data] = Node(data, left_node, right_node)
    
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

```

