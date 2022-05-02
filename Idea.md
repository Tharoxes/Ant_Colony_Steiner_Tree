# idea for project

* Ants
  * are they allowed to visit same node twice?
  * do they travel on the edges (paper), or freely (either a grid or complitely free)?
  * do they go from node to node, or return to a specific node after a visit i.e. do they have a nest?
  * how are pheromones deposited? Depending parameters?
  * Abnahm vo Pheromon?
  * laufed ahli ameise uf eimal oder "einzel"?
  * Are Pheromones deposited continously or only once each cycle?

* Nodes
  * Can some nodes be more desirable
  * How are nodes generated?

* Paper
  * Ants
    * the distances an location of the towns is known to them
    * The amount of pheromons leading to each node is known.
    * Ants are only allowed to go to unvisited nodes
    * lays pheromones after compleded tour
  * Pheromenes
    * layd by ants after completed tour, on each treveled edge
    * amount layed on each each edge dependend on length of tour and a constant
    * pheromones evaporate with a factor rho
  * Short algo summary
    * all ants start in a node -> choose next node depending on closeness and phereomones on edges -> pheromones on edges are updated. repeats until all ants travel the same path or a maximum of iterations has occured.

