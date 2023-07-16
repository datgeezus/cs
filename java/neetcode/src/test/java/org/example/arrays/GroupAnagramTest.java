package org.example.arrays;

import static org.junit.jupiter.api.Assertions.*;

import java.util.List;

class GroupAnagramTest {

    @org.junit.jupiter.api.Test
    void group() {
        var in = List.of("eat", "tea", "tan", "ate", "nat", "bat");

        var out = GroupAnagram.group(in);

        assertEquals(3, out.size());
    }
}
