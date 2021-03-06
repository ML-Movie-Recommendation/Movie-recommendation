"""
管理embedding
1. 建立key到embedding的索引，可以直接查询
2. 建立embedding的faiss索引，可以近邻检索
"""

"""
Management embedding
1. Create an index from key to embedding, you can query directly
2. Establish the faiss index of embedding, which can be searched by neighbors
"""
import pandas as pd
import json
import numpy as np
import faiss


class EmbeddingManager(object):

    def __init__(self, fpath, key_name, value_name):
        # pandas.dataframe
        self.df = pd.read_csv(fpath)

        # 将文件中的embedding加载到内存
        # Load the embedding in the file into memory
        self.dict_embedding = self.load_embedding_to_dict(key_name, value_name)

        # 在faiss建立索引
        # Create index in faiss
        self.faiss_index = self.load_embedding_to_faiss(key_name, value_name)

    def get_embedding(self, key):
        return self.dict_embedding[str(key)]

    def load_embedding_to_dict(self, key_name, value_name):
        return {
            str(row[key_name]): row[value_name]
            for index, row in self.df.iterrows()
        }

    def load_embedding_to_faiss(self, key_name, value_name):
        # id列表
        # id list
        ids = self.df[key_name].values.astype(np.int64)

        # 二维embedding
        # Two-dimensional embedding
        datas = [json.loads(x) for x in self.df[value_name]]
        datas = np.array(datas).astype(np.float32)

        # 维度
        # Dimensions
        dimension = datas.shape[1]

        # 创建faiss索引
        # Create faiss index
        index = faiss.IndexFlatL2(dimension)
        index2 = faiss.IndexIDMap(index)
        index2.add_with_ids(datas, ids)
        return index2

    def search_ids_by_embedding(self, embedding_str, topk):
        """实现近邻搜索"""
        """Realize Near Neighbor Search"""
        input = np.array(json.loads(embedding_str))
        input = np.expand_dims(input, axis=0).astype(np.float32)
        D, I = self.faiss_index.search(input, topk)
        return list(I[0])
