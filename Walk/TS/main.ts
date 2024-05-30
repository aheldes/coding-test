interface IGNode {
    getName(): string

    getChildren(): IGNode[]
}

class GNode implements IGNode {
    private readonly name: string
    private readonly children: IGNode[]

    constructor(name: string, children?: IGNode[]) {
        this.name = name
        this.children = children || []
    }

    public getName(): string {
        return this.name
    }

    public getChildren(): IGNode[] {
        return this.children
    }
}

const walkGraph = (node: IGNode): IGNode[] => {
    const visitedNodes: Set<IGNode> = new Set()

    const walk = (_node: IGNode): void => {
        if (visitedNodes.has(_node)) {
            return
        }

        visitedNodes.add(_node)

        _node.getChildren().forEach(walk)
    }

    walk(node)

    return Array.from(visitedNodes)
}

const dummyNode4 = new GNode("Node 4")
const dummyNode5 = new GNode("Node 5")
const dummyNode6 = new GNode("Node 6")

const dummyNode2 = new GNode("Node 2", [dummyNode4, dummyNode5])
const dummyNode3 = new GNode("Node 3", [dummyNode6])

const mainNode = new GNode("Node 1", [dummyNode2, dummyNode3])

// Walk through the graph
const result = walkGraph(mainNode)
console.log(`Number of unique nodes: ${result.length}. Unique nodes: ${result}`)
