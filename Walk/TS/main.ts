import * as assert from 'assert'

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

const nodeJ = new GNode("J")
const nodeI = new GNode("I")
const nodeH = new GNode("H")
const nodeG = new GNode("G")
const nodeF = new GNode("F")
const nodeE = new GNode("E")

const nodeD = new GNode("D", [nodeJ])
const nodeC = new GNode("C", [nodeG, nodeH, nodeI])
const nodeB = new GNode("B", [nodeE, nodeF])

const mainNode = new GNode("A", [nodeB, nodeC, nodeD])

// Walk through the graph
const result = walkGraph(mainNode)
console.log(`Number of unique nodes: ${result.length}. Unique nodes: ${result}`)

assert.strictEqual(result.length, 10) // Should be 10 unique nodes
