"""
http://www.shareditor.com/blogshow?blogId=80
14. 探究中文分词的艺术

之前的中文分词方法：正向最大匹配、双向扫描、助词遍历，太low
无法解决 歧义消除、未登录词识别

基于前缀词典实现
采用动态规划查找路径
对于未登录词，采用基于汉字能力的HMM模型，使用viterbi

"""