package org.example.arrays;

import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class GroupAnagram {
    public static Collection<List<String>> group(List<String> anagrams) {

        var ans = new HashMap<Integer, List<String>>();

        for (var word : anagrams) {
            int mask = 0x00;

            for (char c : word.toCharArray()) {
                var value = indexOf(c);

                mask |= (1 << value);
            }
            System.out.println("mask: " + mask);
            ans.merge(mask, List.of(word), (prevVal, newVal) -> Stream.of(prevVal, newVal).flatMap(Collection::stream).collect(Collectors.toList()));
        }

        return ans.values();
    }

    static int indexOf(char c) {
        return ((int) c) - ((int) 'a');
    }
}
