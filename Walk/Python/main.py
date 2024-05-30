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


def walk_graph(node: GNode) -> list[GNode]:
    visited_nodes: set[GNode] = set()

    def _walk(_node: GNode) -> None:
        # Base case
        if _node in visited_nodes:
            return

        visited_nodes.add(_node)

        for child_node in _node.get_children():
            # Recursively walk through the graph
            _walk(child_node)

    # Start walk
    _walk(node)
    return list(visited_nodes)


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

    # Walk through the graph
    result = walk_graph(main_node)
    print(f"Number of unique nodes: {len(result)}. Unique nodes: {result}")
    
    assert len(result) == 10  # Should be 10 unique nodes
