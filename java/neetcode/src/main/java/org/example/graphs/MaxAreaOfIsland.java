package org.example.graphs;

import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.function.BiConsumer;
import java.util.function.BiFunction;

public class MaxAreaOfIsland {

    private static final int LAND = 1;

    private static final int[][] MOVES = {
            {0, 1}, {0, -1}, {1, 0}, {-1, 0}
    };

    public static int maxArea(int[][] grid) {
        Context context = new Context(grid);
        for (var r = 0; r < context.nRows; ++r) {
            for (var c = 0; c < context.nCols; ++c) {
                if (inBounds(r, c, context) && grid[r][c] == LAND) {
                    bfs(r, c, MaxAreaOfIsland::constraint, MaxAreaOfIsland::visit, context);
                    context.maxArea = Math.max(context.maxArea, context.area);
                    context.area = 0;
                }
            }
        }

        return context.maxArea;
    }

    private static Boolean constraint(Map.Entry<Integer, Integer> cell, Context context) {
        var row = cell.getKey();
        var col = cell.getValue();
        return inBounds(row, col, context)
                && context.grid[row][col] == LAND
                && !context.visited.contains(cell);
    }

    private static Boolean inBounds(int row, int col, Context context) {
        return row >= 0
                && row < context.nRows
                && col >= 0
                && col < context.nCols;
    }


    private static void visit(Map.Entry<Integer, Integer> cell, Context context) {
        context.area += 1;
        context.visited.add(cell);
    }

    private static void bfs(
            int row,
            int col,
            BiFunction<Map.Entry<Integer, Integer>, Context, Boolean> constraint,
            BiConsumer<Map.Entry<Integer, Integer>, Context> visit,
            Context context) {
        var queue = new ArrayDeque<Map.Entry<Integer, Integer>>();
        var first = Map.entry(row, col);
        queue.addLast(first);
        visit.accept(first, context);

        while (queue.size() > 0) {
            var curr = queue.removeFirst();
            for (var move: MOVES) {
                var newCell = Map.entry(curr.getKey() + move[0], curr.getValue() + move[1]);
                if (constraint.apply(newCell, context)) {
                    visit.accept(newCell, context);
                    queue.addLast(newCell);
                }
            }
        }

    }

    private static final class Context {
        public final int[][] grid;
        public int nRows;
        public int nCols;
        public int maxArea = 0;
        public int area = 0;
        public Set<Map.Entry<Integer, Integer>> visited = new HashSet<>();

        public Context(int[][] grid) {
            this.grid = grid;
            this.nRows = grid.length;
            this.nCols = grid[0].length;
        }

    }
}
