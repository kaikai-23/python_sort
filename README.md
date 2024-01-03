# python_sort

## 概要

このリポジトリは、様々なソートアルゴリズムをPythonで実装したものになります。
初学者から上級者まで、
Pythonを使用したソートアルゴリズムに興味のあるすべての方を対象にしています。
このリポジトリは、基本的なバブルソートからより高度なマージソートまで、
幅広いソートアルゴリズムをカバーしています。

## 含まれるアルゴリズム

このリポジトリには以下のアルゴリズムが含まれています：

- ボゴソート（Bogo Sort）
- バブルソート (Bubble Sort)
- バケットソート (Bucket Sort)
- コックテイルソート（Cocktail Sort）
- コームソート (Comb Sort)
- カウンティングソート (Counting Sort)
- ノームソート（Gnome Sort）
- 挿入ソート (Insertion Sort)
- マージソート (Merge Sort)
- クイックソート (Quick Sort)
- ラディックスソート (Radix Sort)
- 選択ソート (Selection Sort)
- シェルソート (Shell Sort)

## 使い方

各ソートアルゴリズムは、個別のPythonファイルに実装されています。
基本的な使用方法は以下の通りです。
ボゴソートを使用するケースの例：

```python
from sort.bogo_sort import bogo_sort
import random

unsorted_list = [random.randint(0, 1000) for _ in range(10)]
print(unsorted_list)
sorted_list = bogo_sort(unsorted_list)
print(sorted_list)
```
使用したいソートアルゴリズムに応じて適宜置き換えてください。
