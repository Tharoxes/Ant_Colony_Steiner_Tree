import numpy as np


class Node:
  def __init__(self, index, position: np.ndarray, real: bool):
    self.index = index
    self.pos = position
    self.real = real # if it is a real node or a generated one