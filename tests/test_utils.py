import os
import unittest

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

import utils as ut


class UtilsTests(unittest.TestCase):

    def setUp(self):
        self.test_data = "./tests/test_data/abstract_test_data_file.txt"
        self.test_data_out = "./tests/test_data/test_output.csv"
        self.expected_length = 2000
        self.expected_columns = ['pub_id', 'clean_abstract']
        self.expected_top_10 = ['skin', 'clinical', 'study', 'lesions', 'also',
                                'showed', 'one', 'human', 'however', 'activity']

    def test_clean_text_batch_is_expected(self):
        
        if os.path.exists(self.test_data_out):
            os.remove(self.test_data_out)

        try:
            # Read and write in chunks to alleviate memory constraints with large datasets
            df = pd.read_csv(self.test_data, sep="\t", header=None, names=["pub_id", "abstract"], chunksize=10000)
            header = True
            for chunk in df:
                chunk['clean_abstract'] = chunk['abstract'].apply(ut.clean_text)
                chunk.drop('abstract', axis=1, inplace=True)
                chunk.to_csv(self.test_data_out, columns=['pub_id','clean_abstract'],
                             header=header, mode='a', index=False)
                header = False

        except IOError as e:
            print(e)

        # Check output csv is in expected shape
        df = pd.read_csv(self.test_data_out, converters={'clean_abstract': eval})
        self.assertEqual(self.expected_length, len(df))
        self.assertEqual(self.expected_columns, list(df.columns))

    def test_tf_idf_top_10_is_expected(self):
        df = pd.read_csv(self.test_data_out, converters={'clean_abstract': eval})

        # Revert list to string for vectorization
        df['clean_abstract_str'] = df['clean_abstract'].apply(lambda x: " ".join(x))
        abstracts = df['clean_abstract_str'].values
    
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(abstracts)
        feature_names = vectorizer.get_feature_names()
        dense = vectors.todense()
        denselist = dense.tolist()
        vec_df = pd.DataFrame(denselist, columns=feature_names)

        # Compare contents of first abstract for relevance across whole corpus
        abstract_to_compare = df['clean_abstract'].values[0]
        mean_tfidf = vec_df[abstract_to_compare].mean(axis=0)

        top_10 = list(mean_tfidf.sort_values(ascending=False).drop_duplicates()[:10].index)
        self.assertEqual(self.expected_top_10, top_10)
