## Step 1

### 考え方

今回はポインタは1つで十分。訪問したノードを記録していき、再度訪問したノードが見つかった時点でそれがサイクルの開始ノードとなる。

### 結果

59ms (Python3) と全体の中で遅かった。何か改善できる部分があるのだろうか。
毎回 `visited_nodes` の長さ分ループしている部分に無駄がある気がする。

## Step 2

### 改善案1

`set` を使うことで、ノードの存在確認を O(1) で行えるようになった。また、`while cur_node and cur_node.next:` で `cur_node.next` の部分が要らなかった。

なので以下のようになった。

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur_node = head
        visited_nodes = set()

        while cur_node:
            if cur_node in visited_nodes:
                return cur_node
            visited_nodes.add(cur_node)
            cur_node = cur_node.next

        return None
```

**PythonのSetについて**

`set` は固有の `hashable` オブジェクトの順序なしコレクションであり、帰属テスト、重複する要素の削除、および数学的な集合演算に対応している。ハッシュテーブルを使用して実装されているため、要素追加と存在確認の計算量が平均 O(1) である。

参考: https://docs.python.org/ja/3/library/stdtypes.html#types-set

### 改善案2

改善案1だと空間計算量が O(n) になってしまう。しかし問題文には Follow Up として、O(1) 空間計算量で解くことができるか？とある。 以下のようにすると、空間計算量 O(1) で解くことができる。

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        while head != slow:
            head = head.next
            slow = slow.next

        return head
```

根拠を以下に示す。
- head からサイクルの開始ノードまでの距離を a、サイクルの開始ノードから出会った点までの距離を b、出会った点からサイクルの開始ノードまでの距離を c とする。
- 出会うまでに slow は a + b 進み、fast は a + b + n(b + c) 進む (n はサイクルを何周したかを表す整数)。
- fast　は slow の2倍の速度で進んでいるので、かかった時間が一致することを考えれば、2(a + b) = a + b + n(b + c) が成り立つ。これを整理すると、a = c + (n - 1)(b + c) となる。
- よって、head と　slow を同じ速度で進めれば、サイクルの開始ノードで出会うことになる。

実行時間は 48ms (Python3) と Solution 1　と同じだった。
