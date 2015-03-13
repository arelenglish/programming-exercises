# a simple doubly-linked list class.

class Node
  attr_accessor :node, :next, :previous

  def initialize(node)
    @node = node
  end

  def add_node=(node)
    self.next = node
    node.previous = self
  end
end
