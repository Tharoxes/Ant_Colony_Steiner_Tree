# project

## basic design decitions

* Ants
  * are they allowed to visit same node twice?
  - yes, multiple times, but at the of every iteration the pheromone will be placed
  * do they travel on the edges (paper), or freely (either a grid or complitely free)?
  - edges
  * do they go from node to node, or return to a specific node after a visit i.e. do they have a nest?
  -no, they can be anywhere
  * how are pheromones deposited? Depending parameters?
  -empirical and referencing to the papers
  * Are Pheromones deposited continously or only once each cycle?
  - all at once at the end of the iteration

* Nodes
  * Can some nodes be more desirable
  * How are nodes generated?
  - nodes as middle of the circle

## Paper

* Ants
  * the distances between, and location of the nodes is known to them
  * The amount of pheromons leading to each node is known.
  * Ants are only allowed to go to unvisited nodes
  * lays pheromones after compleded tour
* Pheromenes
  * layd by ants after completed tour, on each treveled edge
  * amount layed on each each edge dependend on length of tour and a constant
  * pheromones evaporate with a factor rho
* Short algo summary
  * all ants start in a node -> choose next node depending on closeness and phereomones on edges -> pheromones on edges are updated. repeats until all ants travel the same path or a maximum of iterations has occured.

## bemerkige

* wemmer disign idee vom Paper übernimmt binimer zimmli sicher dases kein Steiner tree geh wird, dah d Ameise sich nur uf gradlinige edges zwüsched de Nodes bewege derfed.
