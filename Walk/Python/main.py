from pydantic import BaseModel


class GNode(BaseModel):
    _name: str
    _children: list['GNode'] = []

    def get_name(self) -> str:
        return self._name

    def get_children(self) -> list['GNode']:
        return self._children

    # Implement __hash__ to be able to compare GNode objects as list is not hashable by default
    def __hash__(self) -> int:
        return hash((self._name, tuple(self._children)))


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
    dummy_node4 = GNode(name="Node 4")
    dummy_node5 = GNode(name="Node 5")
    dummy_node6 = GNode(name="Node 6")

    dummy_node2 = GNode(name="Node 2", children=[dummy_node4, dummy_node5])
    dummy_node3 = GNode(name="Node 3", children=[dummy_node6])

    main_node = GNode(name="Node 1", children=[dummy_node2, dummy_node3])

    # Walk through the graph
    result = walk_graph(main_node)
    print(f"Number of unique nodes: {len(result)}. Unique nodes: {result}")
