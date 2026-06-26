from collections import defaultdict,deque
import heapq
def findItenary(tickets: list[list[str]]) -> list[str]:
    if not tickets:
      return []
    graph = defaultdict(list)
    for src, dest in tickets:
       heapq.heappush(graph[src], dest)
    route = list()
    def dfs(node):
       while graph[node]:
          next = heapq.heappop(graph[node])
          dfs(next)
       route.append(node)
    dfs('JFK')
    return route[::-1]


if __name__ =="__main__":
   tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
   res = findItenary(tickets)
   print(res)