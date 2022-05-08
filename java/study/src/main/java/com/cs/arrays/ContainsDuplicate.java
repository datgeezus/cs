package com.cs.arrays;

import java.util.HashSet;
import java.util.Set;

/**
 * Given an integer array nums, return true if any value appears at least twice in the array, a
 *  nd return false if every element is distinct.
 */
public class ContainsDuplicate {
    public static boolean containsDuplicate(int[] nums) {
        Set<Integer> memo = new HashSet<>(nums.length);
        for (int num: nums) {
            if (memo.contains(num)) {
                return true;
            }
            memo.add(num);
        }

        return false;
    }
}
