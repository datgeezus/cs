"""
Implement a Log Aggregation System which aggregates logs from various services in a datacenter and provides search APIs.

Design the LogAggregator class:

    LogAggregator(int machines, int services) Initializes the object with machines and services representing the number of machines and services in the datacenter, respectively.
    void push(int logId, int machineId, int serviceId, String message) Adds a log with id logId notifying that the machine machineId sent a string message while executing the service serviceId.
    List<Integer> getLogsFromMachine(int machineId) Returns a list of ids of all logs added by machine machineId.
    List<Integer> getLogsOfService(int serviceId) Returns a list of ids of all logs added while running service serviceId on any machine.
    List<String> search(int serviceId, String searchString) Returns a list of messages of all logs added while running service serviceId where the message of the log contains searchString as a substring.

Note that:

    The entries in each list should be in the order they were added, i.e., the older logs should precede the newer logs.
    A machine can run multiple services more than once. Similarly, a service can be run on multiple machines.
    All logId may not be ordered.
    A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input
["LogAggregator", "push", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "pushLog", "getLogsFromMachine", "getLogsOfService", "search", "search"]
[[3, 3], [2322, 1, 1, "Machine 1 Service 1 Log 1"], [2312, 1, 1, "Machine 1 Service 1 Log 2"], [2352, 1, 1, "Machine 1 Service 1 Log 3"], [2298, 1, 1, "Machine 1 Service 1 Log 4"], [23221, 1, 2, "Machine 1 Service 2 Log 1"], [23121, 1, 2, "Machine 1 Service 2 Log 2"], [23222, 2, 2, "Machine 2 Service 2 Log 1"], [23122, 2, 2, "Machine 2 Service 2 Log 2"], [23521, 1, 2, "Machine 1 Service 2 Log 3"], [22981, 1, 2, "Machine 1 Service 2 Log 4"], [23522, 2, 2, "Machine 2 Service 2 Log 3"], [22982, 2, 2, "Machine 2 Service 2 Log 4"], [2], [2], [1, "Log 1"], [2, "Log 3"]]
Output
[null, null, null, null, null, null, null, null, null, null, null, null, null, [23222, 23122, 23522, 22982], [23221, 23121, 23222, 23122, 23521, 22981, 23522, 22982], ["Machine 1 Service 1 Log 1"], ["Machine 1 Service 2 Log 3", "Machine 2 Service 2 Log 3"]]

Explanation
LogAggregator agg = new LogAggregator(3, 3) # There are 3 machines and 3 services
agg.push(2322, 1, 1, "Machine 1 Service 1 Log 1")
agg.push(2312, 1, 1, "Machine 1 Service 1 Log 2")
agg.push(2352, 1, 1, "Machine 1 Service 1 Log 3")
agg.push(2298, 1, 1, "Machine 1 Service 1 Log 4")
agg.push(23221, 1, 2, "Machine 1 Service 2 Log 1")
agg.push(23121, 1, 2, "Machine 1 Service 2 Log 2")
agg.push(23222, 2, 2, "Machine 2 Service 2 Log 1")
agg.push(23122, 2, 2, "Machine 2 Service 2 Log 2")
agg.push(23521, 1, 2, "Machine 1 Service 2 Log 3")
agg.push(22981, 1, 2, "Machine 1 Service 2 Log 4")
agg.push(23522, 2, 2, "Machine 2 Service 2 Log 3")
agg.push(22982, 2, 2, "Machine 2 Service 2 Log 4")
agg.getLogsFromMachine(2) # return [23222, 23122, 23522, 22982]
                                     # Machine 2 added 4 logs, so we return them in the order
                                     # they were added.
agg.getLogsOfService(2) # return [23221, 23121, 23222, 23122, 23521, 22981, 23522, 22982]
                                   # 8 logs were added while running service 2 on a machine.
agg.search(1, "Log 1") # return ["Machine 1 Service 1 Log 1"]
                                  # There is only one log that was added while running service 1
                                  # and contains "Log 1".
agg.search(2, "Log 3") # return ["Machine 1 Service 2 Log 3", "Machine 2 Service 2 Log 3"]
                                  # 2 logs were added while running service 2 that contain "Log 3".

 

Constraints:

    1 <= machines, services <= 20
    1 <= logId <= 105
    All logId are unique.
    0 <= machineId <= machines - 1
    0 <= serviceId <= services - 1
    1 <= message.length, searchString.length <= 500
    message and searchString consist of letters, digits, and ' ' only.
    At most 100 calls in total will be made.
    At least one call in total will be made to getLogsFromMachine, getLogsOfService, and search.

"""
from collections import defaultdict

class LogAggregator:

    def __init__(self, machines: int, services: int) -> None:
        self.machines = machines
        self.services = services
        self.logs = defaultdict(str)
        self.machine_logs = defaultdict(list)
        self.service_logs = defaultdict(list)

    def push(self, log_id: int, machine_id: int, service_id: int, message: str) -> None:
        self.logs[log_id] = message
        self.machine_logs[machine_id].append(log_id)
        self.service_logs[service_id].append(log_id)

    def get_machine_logs(self, machine_id: int) -> list[int]:
        return self.machine_logs.get(machine_id, [])

    def get_service_logs(self, service_id: int) -> list[int]:
        return self.service_logs.get(service_id, [])

    def search(self, service_id: int, search_string: str) -> list[str]:
        return [ 
            self.logs[id] 
            for id in self.service_logs[service_id] 
            if search_string in self.logs[id]
        ]


if __name__ == "__main__":
    machines = 3
    services = 3
    agg = LogAggregator(machines, services)
    agg.push(2322, 1, 1, "Machine 1 Service 1 Log 1")
    agg.push(2312, 1, 1, "Machine 1 Service 1 Log 2")
    agg.push(2352, 1, 1, "Machine 1 Service 1 Log 3")
    agg.push(2298, 1, 1, "Machine 1 Service 1 Log 4")
    agg.push(23221, 1, 2, "Machine 1 Service 2 Log 1")
    agg.push(23121, 1, 2, "Machine 1 Service 2 Log 2")
    agg.push(23222, 2, 2, "Machine 2 Service 2 Log 1")
    agg.push(23122, 2, 2, "Machine 2 Service 2 Log 2")
    agg.push(23521, 1, 2, "Machine 1 Service 2 Log 3")
    agg.push(22981, 1, 2, "Machine 1 Service 2 Log 4")
    agg.push(23522, 2, 2, "Machine 2 Service 2 Log 3")
    agg.push(22982, 2, 2, "Machine 2 Service 2 Log 4")
    machine_logs = agg.get_machine_logs(2) # return [23222, 23122, 23522, 22982]
    print(machine_logs)
    # Machine 2 added 4 logs, so we return them in the order
    # they were added.
    service_logs = agg.get_service_logs(2) # return [23221, 23121, 23222, 23122, 23521, 22981, 23522, 22982]
    print(service_logs)
    # 8 logs were added while running service 2 on a machine.
    logs_1 = agg.search(1, "Log 1") # return ["Machine 1 Service 1 Log 1"]
    print(logs_1)
    # There is only one log that was added while running service 1
    # and contains "Log 1".
    logs_3 = agg.search(2, "Log 3") # return ["Machine 1 Service 2 Log 3", "Machine 2 Service 2 Log 3"]
    print(logs_3)
    # 2 logs were added while running service 2 that contain "Log 3".
