# Greedy-best-first-search
Code to find the greedy best first search from source to destination.


Greedy Best-First Search is an AI search algorithm that attempts to find the most promising path from a given starting point to a goal.
It prioritizes paths that appear to be the most promising, regardless of whether or not they are actually the shortest path.
The algorithm works by evaluating the cost of each possible path and then expanding the path with the lowest cost. 
This process is repeated until the goal is reached.


=> How Greedy Best-First Search Works?

1. Greedy Best-First Search works by evaluating the cost of each possible path and then expanding the path with the lowest cost. This process is repeated until the goal is reached. 
2. The algorithm uses a heuristic function to determine which path is the most promising. 
3. The heuristic function takes into account the cost of the current path and the estimated cost of the remaining paths. 
4. If the cost of the current path is lower than the estimated cost of the remaining paths, then the current path is chosen. This process is repeated until the goal is reached.


=> Advantages of Greedy Best-First Search:

1. Simple and Easy to Implement: Greedy Best-First Search is a relatively straightforward algorithm, making it easy to implement.
2. Fast and Efficient: Greedy Best-First Search is a very fast algorithm, making it ideal for applications where speed is essential.
3. Low Memory Requirements: Greedy Best-First Search requires only a small amount of memory, making it suitable for applications with limited memory.
4. Flexible: Greedy Best-First Search can be adapted to different types of problems and can be easily extended to more complex problems.
5. Efficiency: If the heuristic function used in Greedy Best-First Search is good to estimate, how close a node is to the solution, this algorithm can be a very efficient and find a solution quickly, even in large search spaces.


=> Disadvantages of Greedy Best-First Search:
1. Inaccurate Results: Greedy Best-First Search is not always guaranteed to find the optimal solution, as it is only concerned with finding the most promising path.
2. Local Optima: Greedy Best-First Search can get stuck in local optima, meaning that the path chosen may not be the best possible path.
3. Heuristic Function: Greedy Best-First Search requires a heuristic function in order to work, which adds complexity to the algorithm.
4.Lack of Completeness: Greedy Best-First Search is not a complete algorithm, meaning it may not always find a solution if one is exists. This can happen if the algorithm gets stuck in a cycle or if the search space is a too much complex.


=> Applications of Greedy Best-First Search:
1. Pathfinding: Greedy Best-First Search is used to find the shortest path between two points in a graph. It is used in many applications such as video games, robotics, and navigation systems.
2. Machine Learning: Greedy Best-First Search can be used in machine learning algorithms to find the most promising path through a search space.
3. Optimization: Greedy Best-First Search can be used to optimize the parameters of a system in order to achieve the desired result.
4. Game AI: Greedy Best-First Search can be used in game AI to evaluate potential moves and chose the best one.
5. Navigation: Greedy Best-First Search can be use to navigate to find the shortest path between two locations.
6. Natural Language Processing: Greedy Best-First Search can be use in natural language processing tasks such as language translation or speech recognisation to generate the most likely sequence of words.
7. Image Processing: Greedy Best-First Search can be use in image processing to segment image into regions of intrest.


=>Conclusion:
Greedy Best-First Search is an AI search algorithm that attempts to find the most promising path from a given starting point to a goal. The algorithm works by evaluating the cost of each possible path and then expanding the path with the lowest cost. This process is repeated until the goal is reached. Greedy Best-First Search has several advantages, including being simple and easy to implement, fast and efficient, and having low memory requirements. However, it also has some disadvantages, such as inaccurate results, local optima, and requiring a heuristic function. Greedy Best-First Search is used in many applications, including pathfinding, machine learning, and optimization. It is a useful algorithm for finding the most promising path through a search space.
