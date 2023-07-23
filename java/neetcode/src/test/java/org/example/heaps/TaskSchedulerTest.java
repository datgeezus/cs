package org.example.heaps;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class TaskSchedulerTest {

    @Test
    public void test1() {
        char[] tasks = { 'A', 'A', 'A', 'B', 'B', 'B'};
        int n = 2;
        int out = 8;
        int ans = TaskScheduler.leastInterval(tasks, n);
        assertEquals(out, ans);
    }

    @Test
    public void test2() {
        char[] tasks = { 'A', 'A', 'A', 'B', 'B', 'B'};
        int n = 0;
        int out = 6;
        int ans = TaskScheduler.leastInterval(tasks, n);
        assertEquals(out, ans);
    }

    @Test
    public void test3() {
        char[] tasks = { 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'};
        int n = 2;
        int out = 16;
        int ans = TaskScheduler.leastInterval(tasks, n);
        assertEquals(out, ans);
    }
}
