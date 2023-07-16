package org.example.arrays;

import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/*
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
*/

public class GroupAnagram {
    public static Collection<List<String>> group(List<String> anagrams) {

        var ans = new HashMap<Integer, List<String>>();

        for (var word : anagrams) {
            var hash = hashChars(word);
            System.out.println("mask: " + hash);
            ans.merge(hash, List.of(word), GroupAnagram::mergeLists);
        }

        return ans.values();
    }

    private static int hashChars(String word) {
        int mask = 0;
        for (char c : word.toCharArray()) {
            var index = indexOf(c);
            mask |= (1 << index);
        }
        return mask;
    }

    private static int indexOf(char c) {
        return ((int) c) - ((int) 'a');
    }

    private static List<String> mergeLists(List<String> a, List<String> b) {
        return Stream.of(a, b).flatMap(Collection::stream).collect(Collectors.toList());
    }
}
