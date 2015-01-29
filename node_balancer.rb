class Node
  attr_accessor :left, :right, :value

  def initialize(value)
    @value = value
  end

  def self.balanced?(root)
    d,b = balanced_helper(root, 0)
    return b
  end

  def self.balanced_helper(node, depth = 0)
    return depth, true if node == nil
    d1,b1 = balanced_helper(node.left, depth + 1)
    d2,b2 = balanced_helper(node.right, depth + 1)

    is_balanced = (d1 - d2).abs < 2
    max_depth = d2 > d1 ? d2 : d1
    return [max_depth, is_balanced && b1 && b2]
  end
end
