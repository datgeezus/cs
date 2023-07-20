package org.example.btrees;


import java.util.function.Consumer;

public class Diameter {
    public static int diameter(Node root) {
        if (null == root) {
            return 0;
        }

        Context ctx = new Context(0, 0, 0);
        dfs(root, Diameter::visit, ctx);
        return ctx.diameter;
    }

    public static void visit(Context ctx) {
        ctx.diameter = Math.max(ctx.left + ctx.right, ctx.diameter);
    }

    public static int dfs(Node root, Consumer<Context> onVisit, Context ctx) {
        if (null == root) {
            return 0;
        }

        int left = dfs(root.left, onVisit, ctx);
        int right = dfs(root.right, onVisit, ctx);
        ctx.right = right;
        ctx.left = left;
        onVisit.accept(ctx);
        return 1 + Math.max(left, right);
    }

    public static final class Context {
        public int diameter;
        public int left;
        public int right;

        public Context(int diameter, int left, int right) {
            this.diameter = diameter;
            this.left = left;
            this.right = right;
        }
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
