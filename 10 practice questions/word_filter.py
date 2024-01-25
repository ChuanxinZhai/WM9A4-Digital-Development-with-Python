"""
Word Filter and Counter Function
字过滤器  和 计数器功能
Objective:
Write a function named 'word_filter_counter' that filters and counts specific words in a given text.

Function Parameters:
1. text (string): The text from which words will be filtered and counted. 过滤和计算词语 的文本
2. filter_words (list of strings): A list of words to be filtered out from the text. 从一串文本中 筛选出 所选的单词

Instructions:
- The function should filter out the words from the text that are present in the filter_words list. The comparison should be case-insensitive.
过滤filter_words列表中出现的单词。比较不区分大小写。
- The function should return a dictionary. In this dictionary, the keys are the filtered words, and the values are the counts of how often these words appeared in the text.
返回一个字典。在这个字典中,keys是过滤后的单词,values是出现频率。
- The text may contain punctuation marks and spaces. Only whole words, separated by spaces or punctuation, should be considered.
文本可能包含 标点符号 和 空格。只考虑由空格或标点符号分隔的整个单词。

Example Test Cases:
1. word_filter_counter("Hello world, hello!", ["hello"]) should return a dictionary with the count of occurrences of "hello".
2. word_filter_counter("The quick brown fox.", ["the"]) should return a dictionary with the count of occurrences of "the".
3. word_filter_counter("Is this real life? Is this just fantasy?", ["is", "this", "just"]) should return a dictionary with the counts of occurrences of "is", "this", and "just".
4. word_filter_counter("Do we see the big picture or just small details?", ["we", "the", "or"]) should return a dictionary with the counts of occurrences of "we", "the", and "or".
"""

import re
# 正则
from collections import Counter

filter_words_cache = {}

def word_filter_counter(text, filter_words):
    # Your code goes here
    # Implement the logic to filter words and count their occurrences


    # covert filter_words into lower case
    filter_words_set = set(word.lower() for word in filter_words)

    # find all words 
    words = re.findall(r'\b\w+(?:\'\w+)?\b', text.lower())
    """
                    This regex equation is written by ChatGPT.
                    I want to consider the complex situation, for example: I'll go to the school. I'll go to the park.
                    according to the instruction, I think the word "I'll" should be considered as a whole word. It means that "I" and "ll" should not be counted separately.
    """
                    
    
    # 使用 Counter 计数
    word_counts = Counter(word for word in words if word in filter_words_set)

    # 结果有序输出，按照 filter_words 的顺序
    ordered_output = {word: word_counts.get(word.lower(), 0) for word in filter_words}
    return ordered_output


# Test cases
print(
    word_filter_counter("Hello world, hello!", ["hello"])
)  # Expected output: {'hello': 2}
print(
    word_filter_counter("The quick brown fox.", ["the"])
)  # Expected output: {'the': 1}
print(
    word_filter_counter(
        "Is this real life? Is this just fantasy?", ["is", "this", "just"]
    )
)  # Expected output: {'is': 2, 'this': 2, 'just': 1}
print(
    word_filter_counter(
        "Do we see the big picture or just small details?", ["we", "the", "or"]
    )
)  # Expected output: {'we': 1, 'the': 1, 'or': 1}


# spcial case
print(word_filter_counter("I'll go to the school. I'll go to the park.", ["I", "I'll", "I'", "'ll", "ll", "go", "to", "the"]))
print(word_filter_counter("I'm a boy. I'm a student. I won't go to the school. I won't go to the park.", ["I", "I'", "m", "'m", "won't", "won", "'t", "t", "go", "to", "the", "school", "park"]))
