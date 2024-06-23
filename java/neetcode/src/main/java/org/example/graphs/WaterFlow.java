package org.example.graphs;

import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.function.BiConsumer;
import java.util.function.BiFunction;
import java.util.stream.Collectors;

/**
 * There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The
 * Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the
 * island's right and bottom edges.
 *
 * <p>The island is partitioned into a grid of square cells. You are given an m x n integer matrix
 * heights where heights[r][c] represents the height above sea level of the cell at coordinate (r,
 * c).
 *
 * <p>The island receives a lot of rain, and the rain water can flow to neighboring cells directly
 * north, south, east, and west if the neighboring cell's height is less than or equal to the
 * current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
 *
 * <p>Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water
 * can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
 */
public class WaterFlow {

    private static final int[][] MOVES = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    private static void dfs(
            int r,
            int c,
            BiConsumer<Cell, Context> visit,
            BiFunction<Cell, Context, Boolean> isValid,
            Context context) {
        var cell = new Cell(r, c);
        if (!isValid.apply(cell, context)) {
            return;
        }

        visit.accept(cell, context);
        for (var move : MOVES) {
            var newR = r + move[0];
            var newC = c + move[1];
            context.height = context.heights[r][c];
            dfs(newR, newC, visit, isValid, context);
        }
    }

    private static Boolean isValid(Cell cell, Context context) {
        var r = cell.r;
        var c = cell.c;
        return !context.ocean.contains(cell) && inBounds(r, c, context) && context.height <= context.heights[r][c];
    }

    private static Boolean inBounds(int r, int c, Context context) {
        return r >= 0 && r < context.nRows && c >= 0 && c < context.nCols;
    }

    private static void visit(Cell cell, Context context) {
        var r = cell.r;
        var c = cell.c;
        context.ocean.add(cell);
        context.height = context.heights[r][c];
    }

    public static List<List<Integer>> pacificAtlantic(int[][] heights) {
        Context context = new Context(heights);
        Set<Cell> pacific = new HashSet<>();
        Set<Cell> atlantic = new HashSet<>();
        var nRows = context.nRows;
        var nCols = context.nCols;

        for (int r = 0; r < nRows; ++r) {
            var c = 0;
            context.height = Integer.MIN_VALUE;
            context.ocean = pacific;
            dfs(r, c, WaterFlow::visit, WaterFlow::isValid, context);

            c = nCols - 1;
            context.height = Integer.MIN_VALUE;
            context.ocean = atlantic;
            dfs(r, c, WaterFlow::visit, WaterFlow::isValid, context);
        }

        for (int c = 0; c < nCols; ++c) {
            var r = 0;
            context.height = Integer.MIN_VALUE;
            context.ocean = pacific;
            dfs(r, c, WaterFlow::visit, WaterFlow::isValid, context);

            r = nRows - 1;
            context.height = Integer.MIN_VALUE;
            context.ocean = atlantic;
            dfs(r, c, WaterFlow::visit, WaterFlow::isValid, context);
        }

        return pacific.stream()
                .filter(atlantic::contains)
                .map(entry -> List.of(entry.r, entry.c))
                .collect(Collectors.toList());
    }

    private record Cell(int r, int c) {}

    private static final class Context {
        public final int nRows;
        public final int nCols;
        public final int[][] heights;
        public Set<Cell> ocean;
        public int height = 0;

        public Context(int[][] heights) {
            this.heights = heights;
            this.nRows = heights.length;
            this.nCols = heights[0].length;
        }
    }
}
