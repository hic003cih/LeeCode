from sklearn.feature_extraction.text import CountVectorizer

# 測試文本
texts = ["I love Python.", "Python is great!"]

# 向量化處理
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# 輸出特徵矩陣
print(vectorizer.get_feature_names_out())
print(X.toarray())
