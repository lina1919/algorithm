import sys

input = sys.stdin.readline

n = int(input())
words = []

for _ in range(0,n):
  words.append(input().strip())

#중복 제거를 위해 집합(set) 활용
unique_words = list(set(words))

#길이에 따라 먼저 정렬한 후, 길이가 같으면 사전 순으로 정렬
unique_words.sort(key = lambda x:(len(x),x))

for i in range(len(unique_words)):
  print(unique_words[i])
