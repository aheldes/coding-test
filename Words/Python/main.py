from collections import Counter
import re
import timeit


class WordsCounter:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    # Using counter
    def count_words(self):
        words = self._get_words()
        return Counter([word.lower() for word in words])

    # Using hash map
    def count_words_hash(self):
        hash_map = {}
        words = self._get_words()
        for word in words:
            lower_case_word = word.lower()
            if lower_case_word:
                if lower_case_word in hash_map:
                    hash_map[lower_case_word] += 1
                else:
                    hash_map[lower_case_word] = 1
        return {k: v for k, v in sorted(hash_map.items(), key=lambda item: item[1], reverse=True)}

    def _get_words(self):
        with open(self.file_path, 'r') as file:
            file_content = file.read()
        file_content = re.sub(r'[^a-zA-Z\s]', ' ', file_content)
        file_content = re.sub(r'\s+', ' ', file_content).strip()
        return file_content.split(' ')


if __name__ == "__main__":
    file = 'dummy_text.txt'
    counter = WordsCounter(file)

    hash_avg_time = timeit.timeit(lambda: counter.count_words_hash(), number=1000) / 1000
    print(
        f'Average time taken for count_words_hash method - using hash map (1000 iterations): {hash_avg_time:.8f} seconds')

    counter_avg_time = timeit.timeit(lambda: counter.count_words(), number=1000) / 1000
    print(
        f'Average time taken for count_words method - using Counter (1000 iterations): {counter_avg_time:.8f} seconds')

    using_hash = counter.count_words_hash()
    using_counter = counter.count_words()
    print(using_hash)
    print(f'Unique items: {len(using_hash)}')
    assert using_counter == using_hash
    assert using_counter['in'] == 35
    assert using_counter['id'] == 26
    assert using_counter['in'] == 35
    assert using_counter['id'] == 26
