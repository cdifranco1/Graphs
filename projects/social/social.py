import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # !!!! IMPLEMENT ME
        total_friendships = avg_friendships * num_users // 2
        friendship_combos = []
        
        # Add users
        for i in range(num_users):
            self.add_user(i + 1)     

        # Create friendships
        for i in range(1, num_users + 1):
            for j in range(i + 1, num_users + 1):
                friendship_combos.append((i, j))
        
        random.shuffle(friendship_combos)

        for i in range(total_friendships):
            friendship = friendship_combos[i]
            user_id = friendship[0]
            friend_id = friendship[1]
            self.add_friendship(user_id, friend_id)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        connections = {}  # Note that this is a dictionary, not a set

        # !!!! IMPLEMENT ME]
        for v in self.friendships:
            path = self.bfs(user_id, v)
            if path is not None:
                connections[v] = path

        return connections
    
    def bfs(self, user_id, target):
        visited = set()

        q = Queue()
        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()
            node = path[-1]
            visited.add(node)

            if node == target:
                return path

            for v in self.friendships[node]:
                if v not in visited:
                    path_copy = list(path)
                    path_copy.append(v)
                    q.enqueue(path_copy)


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
