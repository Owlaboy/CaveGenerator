## Implementation document

### General structure

The project follows a package structure. \
The project has four main parts, `main.py`, `display.py`, `triangulator.py` and `minimalTreeGenerator.py`. \
`main.py` works as the main program that calls the rest of the needed parts. 
`display.py` renders the map, triangulation and the rooms on the map. It also calls the function that renders the animation. `triangulator.py` has the Bowyer-Watson algorithm that calculates the triangulation. The Bowyer-Watson algorithm is split into individual functions that are also used in the triangulation animation. `minimalTreeGenerator.py` contains an implementation of Prim's algorithm for finding a minimum spanning tree of the triangulation.

The program begins with the `main.py` file which first asks for parameters for the triangulation. Then the file calls the `display.py` file to render the map. Here the program first randomly generates the rooms and then calls for the triangulator function. Then it calls for the triangulation renderer which is shown first and then the program finally display the triangulation on the final screen with the rooms shown as well.

### Time compelxity

The time complexity of the Bowyer-Watson and Prim's algorithms are _O_(n²)

### Shortcomings and possible improvements

The test coverage of the program is quite inneficient. The program also sometimes fails to add all the points into the triangulation if the points are clustered in a certain way. This can happen when a new point is added to the triangulation but it is only connected to the super triangle. At the end of forming the triangulation the program removes each triangle with any points in the super triangle. So if one point is only connected to the super triangle then it is removed.

The project could be improved in multiple ways. The structure could be improved in what data structures are used. The current implementation has required many data structure conversions. For example when forming the minimum spanning tree the structure of edges has to be completely changed into format that can be used for calculating the minimum spanning tree.

### Usage of chat bots

I used Chat GPT in finding a better structure for my program. What the chat bot told me was used as an inspiration for the general structure rather than a word for word implementation.

### Sources

[Wikipedia article on the Bowyer-Watson algorithm](https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm) \
[Tutorial on the Bowyer-Watson algorithm implementation](https://www.gorillasun.de/blog/bowyer-watson-algorithm-for-delaunay-triangulation/) \
[Article on game map generation](https://www.gamedeveloper.com/programming/procedural-dungeon-generation-algorithm#close-modal) \
[Wikipedia article on Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm) \
[GeeksForGeeks article on Prim's algorithm](https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/)