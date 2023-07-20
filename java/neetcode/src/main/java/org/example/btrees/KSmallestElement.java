package org.example.btrees;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;

public class KSmallestElement {
    public static int kSmallest(Node root, int k) {
        Context context = new Context();

        dfs(root, KSmallestElement::visit, context);

        int nodeCount = context.levels.size();
        int index = Math.min(nodeCount, k - 1);
        return context.levels.get(index);
    }

    public static void visit(Context ctx) {
        ctx.levels.add(ctx.node.val);
    }

    public static void dfs(Node root, Consumer<Context> onVisit, Context ctx) {
        if (null == root) {
            return;
        }

        dfs(root.left, onVisit, ctx);
        ctx.node = root;
        onVisit.accept(ctx);
        dfs(root.right, onVisit, ctx);
    }

    public static final class Context {
        public final List<Integer> levels = new ArrayList<>();
        public Node node;
    }
}
