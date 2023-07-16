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
            var hash = hashChars(word);
            System.out.println("mask: " + hash);
            ans.merge(
                    hash,
                    List.of(word),
                    (prevVal, newVal) ->
                            Stream.of(prevVal, newVal)
                                    .flatMap(Collection::stream)
                                    .collect(Collectors.toList()));
        }

        return ans.values();
    }

    static int hashChars(String word) {
        int mask = 0;
        for (char c : word.toCharArray()) {
            var index = indexOf(c);
            mask |= (1 << index);
        }
        return mask;
    }

    static int indexOf(char c) {
        return ((int) c) - ((int) 'a');
    }
}
