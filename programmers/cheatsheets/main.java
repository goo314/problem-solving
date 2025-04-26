// NOTE:
// This Java file is not runnable.
// It includes sample code from LeetCode cheat sheets.
// It is for studying and practicing coding test.

// Note: Basic
import java.util.*;
int[] arr = new int[10];
int[] tmp = arr.copyOfRange(arr, 1, 5);
System.out.println(Arrays.toString(tmp));

public int two_pointers_fn(int[] arr) {
    int left = 0, right = arr.length -1;
    int ans = 0;

    while (left < right) {
        if (CONDITION) {
            left++;
        } else {
            right--;
        }
    }

    return ans;
}

// Note: how to define arr
// int[] arr = new int[n];
public int[] prefix_sum_fn(int[] arr) {
    int[] dp = new int[arr.length];
    dp[0] = arr[0];

    for (int i=1; i<arr.length; i++){
        dp[i] = dp[i-1] + arr[i];
    }

    return dp;
}

// Note: StringBuilder is more efficient than String
// StringBuilder = sb = new StringBuilder("Hello");
// sb.append(" World"); // sb = "Hello World"
// sb.insert(5, ","); // sb = "Hello, World"
// sb.delete(5, 7); // sb = "HelloWorld"
// sb.reverse(); // sb = "dlroWolleH"
// sb.toString(); 
public String string_build_fn(char[] arr) {
    StringBuilder sb = new StringBuilder();
    for (char c: arr) {
        sb.append(c);
    }
    
    return sb.toString();
}

public ListNode reverse_linked_list_fn(ListNode head) {
    ListNode cur = head;
    ListNode prev = head;

    while (cur != null) {
        ListNode next = cur.next;
        cur.next = prev;
        prev = cur;
        cur = next;
    }

    return prev;
}

// Note: HashMap
// Map<String, Integer> map = new HashMap<>();
// map.put("apple", 3);
// map.get("apple");
// map.getOrderDefaultKey("banana", 0); // 0
// map.containsKey("apple");
// map.remove("apple");
// map.size();
// map.isEmpty();
// map.keySet();
public int find_subarrays_fn(int[] arr, int k) {
    Map<Integer, Integer> counts = new HashMap<>();
    counts.put(0, 1);
    int ans = 0, cur = 0;

    for (int num: arr) {
        ans += counts.getOrderDefault(cur-k, 0);
        counts.put(cur, counts.getOrderDefault(cur, 0)+1);
    }

    return ans;
}

// Note: Stack
// Stack<Integer> s = new Stack<>();
// stack.push(1);
// stack.pop();
// stack.peek(); // the top item
// stack.isEmpty();
// stack.size();
public int increase_stack_fn(int[] arr) {
    Stack<Integer> stack = new Stack<>();
    int ans = 0;

    for (int num: arr) {
        while (!stack.empty() && stack.peek() > num) {
            stack.pop();
        }

        stack.push(num);
    }

    return ans;
}

public int recursize_dfs_fn(TreeNode root) {
    if (root == null) {
        return 0;
    }

    int ans = 0;
    dfs(root.left);
    dfs(root.right);
    
    return ans;
}

public int iterative_dfs_fn(TreeNode root) {
    Stack<TreeNode> s = new Stack<>();
    stack.push(root);
    
    int ans = 0;
    while (!stack.isEmpty()) {
        TreeNode cur = stack.pop();
        if (cur.left != null) {
            stack.push(cur.left);
        }
        if (cur.right != null) {
            stack.push(cur.right);
        }
    }

    return ans;
}

// Note: HashSet allows unique element, set in Python.
// Set<Integer> hs = new HashSet<>();
// hs.add(1);
// hs.remove(1);
// hs.contains(1);
// hs.isEmpty();
// hs.size();
public int iterative_graph_dfs_fn(int[][] adj) {
    Stack<Integer> s = new Stack<>();
    Set<Integer> visited = new HashSet<>();
    s.push(START_NODE);
    s.add(START_NODE);
    int ans = 0;

    while (!s.empty()) {
        int cur = s.pop();
        for (int nxt: adj[cur]) {
            if(!visited.contains(nxt)) {
                visited.add(nxt);
                s.push(nxt);
            }
        }
    }

    return ans;
}

// Node: Queue
// Queue<Integer> q = new LinkedList<>();
// q.add(1);
// q.remove();
// q.peek(); // the front item
// q.isEmpty();
public int bfs_fn(TreeNode root) {
    Queue<TreeNode> q = new LinkedList<>();
    q.add(root);
    int ans = 0;

    while (!q.isEmpty()) {
        TreeNode cur = q.remove();
        if (cur.left != null) {
            q.add(cur.left);
        }
        if (cur.right != null) {
            q.add(cur.right);
        }
    }

    return ans;
}

public int bfs_graph_fn(int[][] adj) {
    Queue<Integer> q = new LinkedList<>();
    Set<Integer> visited = new HashSet<>();
    q.add(START_NODE);
    visited.add(START_NODE);

    while (!q.isEmpty()) {
        int cur = q.remove();
        for (int nxt: adj[cur]) {
            if (!visited.contains(nxt)) {
                visited.add(nxt);
                q.add(nxt);
            }
        }
    }

    return ans;
}

// NOTE: PriorityQueue
// PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b-a); // comparator
// pq.add();
// pq.remove();
// pq.peek();
// pq.isEmpty();
public find_top_k_element_fn(int[] arr, int k) {
    PriorityQueue<Integer> pq = new PriorityQueue<>(CRITERIA);
    for (int x: arr) {
        pq.add(x);
        if (pq.size() > k) {
            pq.remove();
        }
    }

    int[] ans = new int[k];
    for (int i=0; i<k; i++) {
        ans[i] = pq.remove();
    }

    return ans;
}

public int binary_search_fn(int[] arr, int target) {
    int left = 0, right = arr.length-1;
    while (left <= right) {
        int mid = (left+right)/2;
        if (arr[mid] == target) {
            return mid;
        }
        if (arr[mid] > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return left;
}

class TrieNode {
    int data;
    Map<Character, TrieNode> child;
    TrieNode() {
        this.child = new HashMap<>();
    }
}

public TrieNode build_trie_fn(String[] words) {
    TrieNode ans = new TrieNode();

    for (String word: words) {
        TrieNode cur = ans;
        for (char c: word.toCharArray()) {
            if (!cur.child.containsKey(c)) {
                cur.child.put(c, new TrieNode());
            }
            cur = cur.child.get(c);
        }
    }

    return ans;
}

public int[] dijkstra_fn(int n, Map<Integer, List<Pair<Integer, Integer>>> adj) {
    int[] dist = new int[n];
    Arrays.fill(dist, Integer.MAX_VALIE);
    dist[START_NODE] = 0;

    Queue<Pair<Integer, Integer>> pq = new PriorityQueue<Pair<Integer, Integer>>(Comparator.comparing(Pair::getKey));
    pq.add(new Pair(0, START_NODE));

    while (!pq.isEmpty()) {
        Pair<Integer, Integer> curr = pq.remove();
        int d = curr.getKey();
        int cur = curr.getValue();

        if (d > dist[cur]) {
            continue;
        }

        for (Pair<Integer, Integer> edge: adj.get(cur)) {
            int nxt = edge.getKey();
            int w = edge.getValue();
            int nd = d + w;

            if (nd < dist[nxt]) {
                dist[nxt] = nd;
                pq.add(new Pair(nd, nxt));
            }
        }
    }
}
