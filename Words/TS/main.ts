import * as fs from 'fs'
import * as assert from 'assert'

class WordsCounter {
    filePath: string

    constructor(filePath: string) {
        this.filePath = filePath
    }

    public countWords(): { [key: string]: number } {
        const hashMap: { [key: string]: number } = {}
        const words = this.getWords()
        // Create a hashmap with the words and their count
        for (const word of words) {
            if (word) {
                const lowerCaseWord = word.toLowerCase()
                if (hashMap[lowerCaseWord]) {
                    hashMap[lowerCaseWord] += 1
                } else {
                    hashMap[lowerCaseWord] = 1
                }
            }
        }
        // Sort the hashmap by value
        const sortedHashMap: { [key: string]: number } = {}
        Object.keys(hashMap)
            .sort((a, b) => hashMap[b] - hashMap[a])
            .forEach((key) => {
                sortedHashMap[key] = hashMap[key]
            })

        return sortedHashMap
    }

    private getWords(): string[] {
        let fileContent = fs.readFileSync(this.filePath, 'utf-8')
        fileContent = fileContent.replace(/[^a-zA-Z\s]/g, ' ')
        fileContent = fileContent.replace(/\s+/g, ' ').trim()
        return fileContent.split(' ')
    }
}

const filePath = 'dummy_text.txt'
const counter = new WordsCounter(filePath)
const countedWords = counter.countWords()

console.log(countedWords)
console.log(`Unique words: ${Object.keys(countedWords).length}`)

assert.strictEqual(countedWords['in'], 35)
assert.strictEqual(countedWords['id'], 26)
