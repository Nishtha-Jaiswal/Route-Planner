
"""Sources used
http://theory.stanford.edu/~amitp/GameProgramming/
https://dbader.org/blog/priority-queues-in-python
"""    
import math
from queue import PriorityQueue


def shortest_path(route, start, goal):
    
    route_Queue = PriorityQueue()
    route_Queue.put(start, 0) #feeding the priority queue with the first node i.e. the start and giving it the (highest)priority = 0
    
    prev = {start: None} # since start is the starting point so setting the previous to be None
    cost = {start: 0} # stores the cost(distance) covered from the starting point ,we are at the starting point and haven't explored the  neighbors so the cost i.e. the distance is 0

    while not route_Queue.empty():
        current_node = route_Queue.get() #retrieving successive nodes from the priority queue

        if current_node == goal: # destination is reached i.e. now we can get the final cost efficient route
            create_route(prev, start, goal)

        for node in route.roads[current_node]: # if path/connection to other neighbor nodes exists the calculate the cost i.e. the distance
            
            new_cost = cost[current_node] + heuristic_distance(route.intersections[current_node], route.intersections[node]) # cost(distance) calculated from the starting point to the most recently discovered node
            
            if node not in cost or new_cost < cost[node]: # if we have discovered a new node whose cost(from the start pt) is not calculated 
                                                          # or if the new cost calculated is less than the older one
               
                cost[node] = new_cost # inserting the cost(distance) corresponding to the discovered node 
                total_cost = new_cost + heuristic_distance(route.intersections[current_node], route.intersections[node]) # updated cost(distance), calculated from the starting point to the most recently discovered node
                
                route_Queue.put(node, total_cost) #put the node in priority queue where the total cost acts as the priority
                prev[node] = current_node # stores the nodes that are part of the cost efficient route

    return create_route(prev, start, goal)


#returning distance btween start (intersection[current_node]) and goal (intersection[node])
def heuristic_distance(start, goal):
    #Euclidean distance
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2)) # distance between two points

def create_route(prev, start, goal):
    current_node = goal # starting from the goal side
    route = [current_node]
    while current_node != start: #traversing in backward direction i.e. from goal to start
        current_node = prev[current_node]
        route.append(current_node)
    route.reverse() #reversing the route to make it from start to goal
    return route
    return
