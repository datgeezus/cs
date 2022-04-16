package com.cs.memo;

import java.util.*;

public class CanSum {

    public static Boolean canSum(Integer target, int[] nums, Map<Integer, Boolean> memo) {
        Optional<Boolean> val = Optional.ofNullable(memo.get(target));

        if (val.isPresent()) {
            return val.get();
        }

        if (target < 0) {
            return false;
        }

        if (target == 0) {
            return true;
        }

        for (Integer num: nums) {
            Integer reminder = target - num;
            if (canSum(reminder, nums, memo)) {
                memo.put(target, true);
                return true;
            }
        }

        memo.put(target, false);
        return false;
    }

}
