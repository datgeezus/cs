package org.example.backtracking;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class CombinationSum {

    public static List<List<Integer>> combinationSum(int[] candidates, int target) {
        var context = new Context(candidates, target);
        var stack = new Stack<Integer>();
        dfs(0, stack, 0, context);
        return context.getAns();
    }

    private static void dfs(int i, Stack<Integer> current, int total, Context context) {
        var candidates = context.getCandidates();
        var target = context.getTarget();
        var nCandidates = context.getCandidatesSize();

        if (total == target) {
            context.addToAnds(new ArrayList<>(current));
            return;
        }

        if ((i >= nCandidates) || (total > target)) {
            return;
        }

        current.add(candidates[i]);
        dfs(i, current, total + candidates[i], context);
        current.pop();
        dfs(i + 1, current, total, context);
    }

    private static final class Context {
        private final List<List<Integer>> ans = new ArrayList<>();
        private final int[] candidates;
        private final int target;

        public Context(int[] candidates, int target) {
            this.candidates = candidates;
            this.target = target;
        }

        public int getTarget() {
            return target;
        }

        public int getCandidatesSize() {
            return candidates.length;
        }

        public int[] getCandidates() {
            return candidates;
        }

        public List<List<Integer>> getAns() {
            return ans;
        }

        public void addToAnds(List<Integer> data) {
            ans.add(data);
        }
    }

}
