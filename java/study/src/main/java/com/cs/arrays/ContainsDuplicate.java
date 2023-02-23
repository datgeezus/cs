package com.cs.arrays;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.atomic.AtomicBoolean;

/**
 * Given an integer array nums, return true if any value appears at least twice in the array, a
 *  nd return false if every element is distinct.
 */
public class ContainsDuplicate {
    public static boolean containsDuplicate(int[] nums) {
        Set<Integer> memo = new HashSet<>(nums.length);
        for (int num: nums) {
            if (!memo.add(num)) {
                return true;
            }
        }

        return false;
    }

    public static boolean duplicate(int[] nums) {
        var memo = new HashSet<Integer>(nums.length);
        var ans = Arrays.stream(nums)
            .mapToObj(memo::add)
            .filter(x -> x)
            .findFirst();
        return ans.orElse(false);
    }
}
