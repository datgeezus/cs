"""
A Rate Limiting System can allow a maximum of n requests every t seconds, using an implementation similar to the sliding window algorithm.

Given two positive integers n and t, and a non-decreasing stream of integers representing the timestamps of requests, implement a data structure that can check if each request is allowed or not.

Implement the RateLimiter class:

    RateLimiter(int n, int t) Initializes the RateLimiter object with an empty stream and two integers n and t.
    boolean should_allow(int timestamp) Returns true if the current request with timestamp timestamp is allowed, otherwise returns false. Note that while checking if the current request should be allowed, only the timestamps of requests previously allowed are considered.

 

Example 1:

Input
["RateLimiter", "should_allow", "shouldAllow", "shouldAllow", "shouldAllow", "shouldAllow"]
[[3, 5], [1], [1], [2], [3], [8]]
Output
[null, true, true, true, false, true]

Explanation
RateLimiter rateLimiter = new RateLimiter(3, 5)
rateLimiter.should_allow(1) # returns True
                            # There are no previous requests, so this request is allowed.
rateLimiter.should_allow(1) # returns True
                            # We can allow 3 requests every 5 seconds, so this request is allowed.
                            # Timestamps of allowed requests are [1,1].
rateLimiter.should_allow(2) # returns True
                            # Timestamps of allowed requests are [1,1,2].
rateLimiter.should_allow(3) # returns False
                            # This request is not allowed because
                            # the time range [1,3] already has 3 allowed requests.
rateLimiter.should_allow(8) # returns True
                            # This request is allowed because
                            # the time range [4,8] does not have any allowed requests.

 

Constraints:

    1 <= n <= 105
    1 <= t, timestamp <= 105
    At most 105 calls will be made to should_allow.
    timestamp values will be non-decreasing over all calls made to should_allow.

"""

from collections import deque

class RateLimiter:

    def __init__(self, n: int, t: int):
        self.N = n
        self.T = t

        # Queue to store allowed requests with the following constraints:
        # size can't exceed N
        # diff between max and min timestamps can't exceed T
        self.allowed_requests = deque()

    def should_allow(self, timestamp: int) -> bool:
        if not self.allowed_requests:
            self.allowed_requests.appendleft(timestamp)
            return True

        while self.allowed_requests and timestamp - self.allowed_requests[-1] >= self.T:
            self.allowed_requests.pop()

        if len(self.allowed_requests) >= self.N:
            return False

        self.allowed_requests.appendleft(timestamp)
        return True

if __name__ == "__main__":
    rateLimiter = RateLimiter(3, 5)
    assert rateLimiter.should_allow(1)
    # returns True
    # There are no previous requests, so this request is allowed.

    assert rateLimiter.should_allow(1)
    # returns True
    # We can allow 3 requests every 5 seconds, so this request is allowed.
    # Timestamps of allowed requests are [1,1].

    assert rateLimiter.should_allow(2)
    # returns True
    # Timestamps of allowed requests are [1,1,2].

    assert not rateLimiter.should_allow(3)
    # returns False
    # This request is not allowed because
    # the time range [1,3] already has 3 allowed requests.

    assert rateLimiter.should_allow(8)
    # returns True
    # This request is allowed because
    # the time range [4,8] does not have any allowed requests.
