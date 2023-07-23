package org.example.heaps;

import java.util.Collections;
import java.util.Comparator;
import java.util.Map;
import java.util.PriorityQueue;

/**
 * Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an
 * integer k, return the k closest points to the origin (0, 0).
 *
 * <p>The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2
 * + (y1 - y2)2).
 *
 * <p>You may return the answer in any order. The answer is guaranteed to be unique (except for the
 * order that it is in).
 *
 * <p>Example 1:
 *
 * <p>Input: points = [[1,3],[-2,2]], k = 1 Output: [[-2,2]] Explanation: The distance between (1,
 * 3) and the origin is sqrt(10). The distance between (-2, 2) and the origin is sqrt(8). Since
 * sqrt(8) < sqrt(10), (-2, 2) is closer to the origin. We only want the closest k = 1 points from
 * the origin, so the answer is just [[-2,2]].
 *
 * <p>Example 2:
 *
 * <p>Input: points = [[3,3],[5,-1],[-2,4]], k = 2 Output: [[3,3],[-2,4]] Explanation: The answer
 * [[-2,4],[3,3]] would also be accepted.
 *
 * <p>Constraints:
 *
 * <p>1 <= k <= points.length <= 104 -104 < xi, yi < 104
 */
public class KClosestPoints {

    public static int[][] kClosest(int[][] points, int k) {
        var maxHeap =
                new PriorityQueue<Map.Entry<Double, int[]>>(
                        Collections.reverseOrder(Comparator.comparingDouble(Map.Entry::getKey)));

        int[] origin = {0, 0};

        for (var point : points) {
            var d = distance(origin, point);
            maxHeap.add(Map.entry(d, point));
            if (maxHeap.size() > k) {
                maxHeap.remove();
            }
        }

        int len = maxHeap.size();
        int[][] ans = new int[len][2];

        for (int i = 0; i < len; ++i) {
            var val = maxHeap.remove();
            ans[i] = val.getValue();
        }

        return ans;
    }

    private static double distance(int[] p, int[] q) {
        int a = p[0] - q[0];
        int b = p[1] - q[1];

        return Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
    }
}
