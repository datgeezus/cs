package org.example.graphs;

import java.util.*;
import java.util.function.BiFunction;

public class NumberOfIslands {

    private static final Map.Entry<Integer, Integer>[] directions = new Map.Entry[]{
        Map.entry(1, 0),
        Map.entry(-1, 0),
        Map.entry(0, 1),
        Map.entry(0, -1),
    };

    public static int numberOfIslans(char[][] grid) {
        Context context = new Context(grid);
        for (int r = 0; r < context.nRows; ++r) {
            for(int c = 0; c < context.nCols; ++c) {
                if (isIsland(r, c, context) && notVisited(r, c, context)) {
                    bfs(r, c, NumberOfIslands::constraint, context);
                    context.nIslands += 1;
                    printGrid(grid);
                }
            }
        }


        return context.nIslands;
    }

    public static void printGrid(char[][] grid) {
        int nRows = grid.length;
        int nCols = grid[0].length;
        for (int r = 0; r < nRows; ++r) {
            for(int c = 0; c < nCols; ++c) {
                System.out.print(grid[r][c]);
            }
            System.out.println();
        }
        System.out.println();
    }

    public static boolean constraint(Map.Entry<Integer, Integer> cell, Context context) {
        var row = cell.getKey();
        var col = cell.getValue();
        return inBounds(row, col, context)
                && isIsland(row, col, context)
                && notVisited(row, col, context);
    }

    public static boolean inBounds(int row, int col, Context context) {
        var nRows = context.nRows;
        var nCols = context.nCols;
        return row >= 0
                && row < nRows
                && col >= 0
                && col < nCols;
    }

    public static boolean isIsland(int row, int col, Context context) {
        return context.grid[row][col] == Context.LAND;
    }

    public static boolean notVisited(int row, int col, Context context) {
        var cell = Map.entry(row, col);
        return !context.visited.contains(cell);
    }


    public static void bfs(int row, int col, BiFunction<Map.Entry<Integer, Integer>, Context, Boolean> constraint, Context context) {
        Deque<Map.Entry<Integer, Integer>> q = new ArrayDeque<>();
        q.add(Map.entry(col, row));
        context.visited.add(Map.entry(row, col));
        context.grid[row][col] = '*';

        while (q.size() > 0) {
            var currCell = q.removeFirst();
            for (var direction: directions) {
                var dr = direction.getKey();
                var dc = direction.getValue();
                var newCell = Map.entry(currCell.getKey() + dr, currCell.getValue() + dc);
                if (constraint.apply(newCell, context)) {
                    q.addLast(newCell);
                    context.visited.add(newCell);
                    context.grid[newCell.getKey()][newCell.getValue()] = '*';
                }
            }
        }
    }

    private static final class Context {
        public static final char LAND = '1';
        public final char[][] grid;
        public final int nRows;
        public final int nCols;
        public int nIslands = 0;
        public Set<Map.Entry<Integer, Integer>> visited = new HashSet<>();

        public Context(char[][] grid) {
            this.grid = grid;
            this.nRows = grid.length;
            this.nCols = grid[0].length;
        }
    }
}
