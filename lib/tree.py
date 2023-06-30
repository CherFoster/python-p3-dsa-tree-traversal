class Tree:
  def __init__(self, root=None):
    self.root = root

  def get_element_by_id(self, target_id):
    return self._dfs(self.root, target_id)

  def _dfs(self, node, target_id):
    if node and node.get('id') == target_id:
      return node

    for child in node.get('children', []):
      result = self._dfs(child, target_id)
      if result:
        return result

    return None