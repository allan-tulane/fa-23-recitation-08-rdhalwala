from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
  def help(visited, frontier):
    if len(frontier) == 0:
      return visited

    else:

      path_weight, path_edges, node = heappop(frontier)
      if node not in visited:
        visited[node] = (path_weight, path_edges)
        for neighbor, weight in graph[node]:
          heappush(frontier, (path_weight + weight, path_edges + 1, neighbor))
        return help(visited, frontier)
      else:
        return help(visited, frontier)

  visited = dict()
  frontier = []
  heappush(frontier, (0, 0, source))

  return help(visited, frontier)


"""
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    
    
def bfs_path(graph, source):
  def help_sec(visited, frontier, parent):
    if len(frontier) == 0:
      #return partent if len is 0
      return parent
    else:
      node = frontier.popleft()
      visited.add(node)
      for n in graph[node]:
        #not frontier or visited add n check again
        if n not in frontier and n not in visited:
          parent[n] = node
          frontier.append(n)
      return help_sec(visited, frontier, parent)
#deque
  frontier = deque()
  #append
  frontier.append(source)

  parent = dict()
  visited = set()
#return final help
  return help_sec(visited, frontier, parent)

  """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO


def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
  #check if not in parent
  if destination not in parents:
    return ""
#then recursive
  else:
    return get_path(parents, parents[destination]) + parents[destination]
  
  """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO


