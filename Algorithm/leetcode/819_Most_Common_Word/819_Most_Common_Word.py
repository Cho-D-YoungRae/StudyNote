class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^a-zA-Z]', ' ', paragraph)
        paragraph = paragraph.lower()
        word_count = collections.Counter(paragraph.split())

        for word, i in word_count.most_common():
            if word not in banned:
                return word