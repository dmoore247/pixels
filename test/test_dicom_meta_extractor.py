import unittest

from spark import get_spark
spark = get_spark()

path = 'dbfs:/FileStore/shared_uploads/douglas.moore@databricks.com/benigns'

def get_object_frame(spark):
    from databricks.pixels import Catalog

    df = Catalog.catalog(spark, path)
    return df

class TestDicomFrames(unittest.TestCase):

    def test_dicom_class(self):
        from databricks.pixels import DicomFrames
        assert DicomFrames

    def test_dicom_to_dicom_meta(self):
        from databricks.pixels import DicomFrames
        o_df = get_object_frame(spark)
        dicom_df = DicomFrames(o_df)
        df2 = dicom_df.withMeta()
        self.assertIn('meta',df2.columns)
        count = df2.count()
        response = df2.select('meta').take(1)[0]
        self.assertIsNotNone(response)
        print(response)

"""  disable tests   
    def test_dicom_to_dicom_meta_constructor(self):
        from databricks.pixels import DicomFrames
        o_df = get_object_frame(spark)
        dicom_df = DicomFrames(o_df, withMeta=True)
        self.assertTrue('meta' in dicom_df.columns,dicom_df.columns)
        response = dicom_df.select('meta').take(1)[0]
        self.assertIsNotNone(response)
        print(response)


    def test_dicom_init(self):
        from databricks.pixels import DicomFrames
        o_df = get_object_frame(spark)
        dicom_df = DicomFrames(o_df)
        count = dicom_df.count()
        self.assertEqual(170, count)

    def test_dicom_describe(self):
        from databricks.pixels import DicomFrames
        o_df = get_object_frame(spark)
        dicom_df = DicomFrames(o_df)
        results = dicom_df.describe()
        self.assertIsNotNone(results)
        print('->'*20, results)

    def test_dicom_repr_html(self):
        from databricks.pixels import DicomFrames
        
        o_df = get_object_frame(spark)
        dicom_df = DicomFrames(o_df)
        response = dicom_df.__repr__()
        self.assertIsNotNone(response)
        print(response)

    def test_dicom_columns(self):
        from databricks.pixels import DicomFrames
        o_df = get_object_frame(spark)
        dicom_df = DicomFrames(o_df)
        response = dicom_df.columns
        self.assertIsNotNone(response)
        print(response)

    def test_dicom_to_dicom_frames(self):
        from databricks.pixels import DicomFrames
        o_df = get_object_frame(spark)
        dicom_df = DicomFrames(o_df)
        df2 = dicom_df.withMeta()
        response = df2.take(5)
        self.assertIsNotNone(response)
        print(response)


"""
    
if __name__ == '__main__':
    import sys, os
    # fix sys path to include adjacent source code
    sys.path.insert(0, os.path.dirname(__file__)+"/..")
    unittest.main()