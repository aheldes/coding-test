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

const paths = (node: IGNode): IGNode[][] => {
    const foundPaths: IGNode[][] = []

    const findPath = (node: IGNode, path: IGNode[]): void => {
        const newPath = [...path, node]

        if (node.getChildren().length === 0) {
            foundPaths.push(newPath)
            return
        }

        node.getChildren().forEach(child => findPath(child, newPath))
    }

    findPath(node, [])

    return foundPaths

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

// Find paths
const result = paths(mainNode)
console.log(`Found paths: ${result}`)

const stringRepresentation = JSON.stringify(result.map(path => path.map(node => node.getName())))
console.log(`String representation of paths: ${stringRepresentation}`)

assert.strictEqual(result.length, 6)
assert.strictEqual(stringRepresentation, '[["A","B","E"],["A","B","F"],["A","C","G"],["A","C","H"],["A","C","I"],["A","D","J"]]')
