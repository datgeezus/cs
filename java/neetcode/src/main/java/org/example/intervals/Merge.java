package org.example.intervals;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Merge {
    public static List<List<Integer>> merge(List<List<Integer>> intervals) {
        List<List<Integer>> ans = new ArrayList<>();
        intervals.sort(Comparator.comparingInt(a -> a.get(0)));
        ans.add(intervals.get(0));

        for (List<Integer> interval: intervals) {
            int lastIntervalIndex = ans.size() - 1;
            int prevEnd = ans.get(lastIntervalIndex).get(1);
            int start = interval.get(0);
            int end = interval.get(1);
            if (start <= prevEnd) {
                List<Integer> lastInterval = ans.get(lastIntervalIndex);
                lastInterval.set(1, Math.max(prevEnd, end));
            } else {
                ans.add(List.of(start, end));
            }
        }

        return ans;
    }
}
