def frequencySort(s: str) -> str:
    freq_map = {}
    for char in s:
        freq_map[char] = freq_map.get(char, 0) + 1

    max_freq = max(freq_map.values())
    buckets = [[] for _ in range(max_freq + 1)]

    for char in freq_map:
        buckets[freq_map[char]].append(char)

    result = []
    for freq in range(max_freq, 0, -1):
        for char in buckets[freq]:
            result.append(char * freq)

    return ''.join(result)
