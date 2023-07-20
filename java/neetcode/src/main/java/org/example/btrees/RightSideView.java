package org.example.btrees;

import java.util.*;

public class RightSideView {

    public static List<Integer> rightSideView(Node root) {
        if (root == null) {
            return Collections.emptyList();
        }

        Deque<Node> q = new ArrayDeque<>();
        q.addLast(root);
        List<Integer> ans = new ArrayList<>();

        while ( q.size() > 0 ) {
            int n = q.size();
            int lastIndex = n - 1;
            for (int i = 0; i < n; ++i) {
                Node node = q.removeFirst();
                if (i == lastIndex) {
                    ans.add(node.val);
                }

                if (null != node.left) {
                    q.addLast(node.left);
                }

                if (null != node.right) {
                    q.addLast(node.right);
                }
            }
        }

        return ans;
        
    }

    public static final class Node {
        public int val;
        public Node left;
        public Node right;

        public Node(int val) {
            this.val = val;
        }

        public Node(int val, Node left, Node right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
}
