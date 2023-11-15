from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        
        for sentence in sentences:
            words = sentence.split()  # Split the sentence into words
            word_count = len(words)   # Count the number of words
            
            if word_count > max_words:
                max_words = word_count  # Update the maximum word count if needed
        
        return max_words

if __name__ == "__main__":
    # Example sentences
    sentences1 = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    sentences2 = ["please wait", "continue to fight", "continue to win"]
    
    solution = Solution()
    
    # Find the maximum number of words in a single sentence for the given examples
    max_words1 = solution.mostWordsFound(sentences1)
    max_words2 = solution.mostWordsFound(sentences2)
    
    print(f"Max words in sentences1: {max_words1}")  # Output for sentences1
    print(f"Max words in sentences2: {max_words2}")  # Output for sentences2
