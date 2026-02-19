class TaskManager:
    def __init__(self, tasks):
        self.heap = []  # (-priority, -taskId, userId)
        self.task_dict = {}  # taskId -> (priority, userId)

        for userId, taskId, priority in tasks:
            heapq.heappush(self.heap, (-priority, -taskId, userId))
            self.task_dict[taskId] = (priority, userId)

    def add(self, userId, taskId, priority):
        heapq.heappush(self.heap, (-priority, -taskId, userId))
        self.task_dict[taskId] = (priority, userId)

    def edit(self, taskId, newPriority):
        if taskId not in self.task_dict:
            return
        _, userId = self.task_dict[taskId]
        self.task_dict[taskId] = (newPriority, userId)
        heapq.heappush(self.heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId):
        if taskId in self.task_dict:
            del self.task_dict[taskId]

    def execTop(self):
        while self.heap:
            priority, taskId, userId = heapq.heappop(self.heap)
            taskId = -taskId
            priority = -priority
            if (
                taskId in self.task_dict
                and self.task_dict[taskId] == (priority, userId)
            ):
                del self.task_dict[taskId]
                return userId

        return -1
