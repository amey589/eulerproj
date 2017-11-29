import sys
g = {}
n = int(sys.argv[1])
print("n is {}".format(n))
for r in range(0,n+1):
    for c in range(0,n+1):
        node = "{}_{}".format(r,c)
        adj_list = []
        if r+1 <= n :
            adj_list.append("{}_{}".format(r+1,c))
        if c+1 <= n :
            adj_list.append("{}_{}".format(r,c+1))
        g[node] = adj_list
for key in g.keys():
    print(key,g[key])
count = 0

def printAllPathsUtil(u, d, visited, path):
    #print("util u {} d {} visited {} path {}".format(u,d,visited,path)) 
    # Mark the current node as visited and store in path
    visited[u]= True
    path.append(u)
 
    # If current vertex is same as destination, then print
    # current path[]
    if u ==d:
        global count
        count = count + 1 
    else:
        # If current vertex is not destination
         #Recur for all the vertices adjacent to this vertex
        for i in g[u]:
            if visited[i]==False:
                printAllPathsUtil(i, d, visited, path)
                
    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[u]= False
   
  
    # Prints all paths from 's' to 'd
def printAllPaths(s, d):
 
    # Mark all the vertices as not visited
    visited = {}
    for key in g.keys():
        visited[key] = False
 
    # Create an array to store paths
    path = []
 
    # Call the recursive helper function to print all paths
    printAllPathsUtil(s, d,visited, path)
  
  
s = "0_0"
d = "{}_{}".format(n,n) 
printAllPaths(s, d)
print(count)
