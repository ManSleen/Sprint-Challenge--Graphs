from collections import deque


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        self.visited = set()

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a undirected edge to the graph. Both nodes point to each other <------>
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = deque()
        visited = set()
        queue.appendleft(starting_vertex)
        while len(queue) > 0:
            current_node = queue.pop()
            if current_node not in visited:
                visited.add(current_node)
                print("Node: ", current_node)
                for neighbor in self.get_neighbors(current_node):
                    queue.appendleft(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = deque()
        visited = set()
        stack.append(starting_vertex)
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                print("Node: ", current_node)
                for neighbor in self.get_neighbors(current_node):
                    stack.append(neighbor)

    def get_path(self, starting_room):

        stack = deque()
        visited = set()
        stack.append(starting_room)
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                print("Node: ", current_node)
                for neighbor in self.get_neighbors(current_node):
                    stack.append(neighbor)

    def dft_recursive(self, starting_vertex, visited):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Mark the node as visited
        # Call `dft_recursive` on each neighbor that has not been visited
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        queue = deque()
        queue.appendleft([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty:
        while len(queue) > 0:
            # Dequeue the first PATH
            current_path = queue.pop()
            # print("current path: ", current_path)
            # Grab the last vertex from the PATH
            last_vertex = current_path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # Check if it's the target
                if last_vertex == destination_vertex:
                    return current_path
                    # If so, return path
                # Mark it as visited
                visited.add(last_vertex)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_vertex):
                    new_path = [*current_path, neighbor]
                    queue.appendleft(new_path)
                    # Copy the path
                    # Append the neighbor to the back

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH TO the starting vertex ID
        stack = deque()
        stack.append([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty:
        while len(stack) > 0:
            # Pop the first PATH
            current_path = stack.pop()
            # print("current path: ", current_path)
            # Grab the last vertex from the PATH
            last_vertex = current_path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # Check if it's the target
                if last_vertex == destination_vertex:
                    return current_path
                    # If so, return path
                # Mark it as visited
                visited.add(last_vertex)
                # Then add A PATH TO its neighbors to the top of the stack
                for neighbor in self.get_neighbors(last_vertex):
                    new_path = current_path.copy()
                    new_path.append(neighbor)
                    stack.append(new_path)
                    # Copy the path
                    # Append the neighbor to the back

    def dfs_recursive(self, starting_vertex, destination_vertex, visited, path_list):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        current_node = starting_vertex
        if current_node not in visited:
            path_list.append(current_node)
            visited.add(current_node)

            if starting_vertex == destination_vertex:
                print(path_list)

            for neighbor in self.get_neighbors(starting_vertex):
                self.dfs_recursive(
                    neighbor, destination_vertex, visited, path_list)

    # THIs ONE WORKS!!! vvvvv

    def dfs_recursive2(self, starting_vertex, destination_vertex, visited=None, path=None):
        # Init visited
        if visited is None:
            visited = set()
        # Init path
        if path is None:
            path = []
        visited.add(starting_vertex)
        # Add vertex to the path
        path = path + [starting_vertex]
        # If we are at the target value, return the path
        if starting_vertex == destination_vertex:
            return path
        # Otherwise call the dfs_recursive function on each unvisited neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive2(
                    neighbor, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path
        return None
