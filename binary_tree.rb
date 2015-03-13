# A simple Binary Tree written in Ruby. 
# New features could include: 
# => Finding the current level for a given node
# => Finding if the tree is balanced
# => Balancing the tree
# => Displaying the tree graphically

class BinaryTree
  attr_accessor :root_node

  def initialize(root_node)
    @root_node = root_node
  end

  # Start with current_node = tree.root_node
  def add_node(node, current_node)
    if node.value > current_node.value
      if current_node.right.nil?
        current_node.right = node
        node.parent = current_node
      else
        current_node = current_node.right
        add_node(node, current_node)
      end
    else
      if current_node.left.nil?
        current_node.left = node
        node.parent = current_node
      else
        current_node = current_node.left
        add_node(node, current_node)
      end
    end
  end
end

class Node
  attr_accessor :value, :parent, :left, :right

  def initialize(value)
    @value = value
  end
end
