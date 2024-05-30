from pydantic import BaseModel


class GNode(BaseModel):
    name: str
    children: list['GNode'] = []

    def get_name(self) -> str:
        return self.name

    def get_children(self) -> list['GNode']:
        return self.children

    # Implement __hash__ to be able to compare GNode objects as list is not hashable by default
    def __hash__(self) -> int:
        return hash((self.name, tuple(self.children)))


def get_paths(node: GNode) -> list[list[GNode]]:
    found_paths: list[list[GNode]] = []

    def _find_path(_node: GNode, _path: list[GNode]) -> None:
        # Add current node to the path
        _path = _path + [_node]

        # Base case
        if not _node.get_children():
            found_paths.append(_path)
        else:
            for child in _node.get_children():
                # Recursively find paths
                _find_path(child, _path)

    _find_path(node, [])
    return found_paths


if __name__ == "__main__":
    # Create dummy nodes
    node_J = GNode(name="J")
    node_I = GNode(name="I")
    node_H = GNode(name="H")
    node_G = GNode(name="G")
    node_F = GNode(name="F")
    node_E = GNode(name="E")

    node_D = GNode(name="D", children=[node_J])
    node_C = GNode(name="C", children=[node_G, node_H, node_I])
    node_B = GNode(name="B", children=[node_E, node_F])

    main_node = GNode(name="A", children=[node_B, node_C, node_D])

    # Find paths
    result = get_paths(main_node)
    print(f"Found paths: {result}")

    string_representation = [[node.get_name() for node in path] for path in result]
    print(f"String representation of paths: {string_representation}")

    assert len(result) == 6  # Should be 6 paths
    assert string_representation == [['A', 'B', 'E'], ['A', 'B', 'F'], ['A', 'C', 'G'], ['A', 'C', 'H'],
                                     ['A', 'C', 'I'], ['A', 'D', 'J']]
