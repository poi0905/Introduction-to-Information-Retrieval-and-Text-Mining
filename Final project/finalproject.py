from snownlp import SnowNLP

text = '今天全家很讚'
s = SnowNLP(text)
print ("內容 ： %s" %text)
print ("情感值：%s" %s.sentiments)