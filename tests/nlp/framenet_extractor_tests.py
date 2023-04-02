import unittest
from unittest.mock import MagicMock

from app.src.nlp.framenet import IFramenet, MyLU, MyFrame, MyFrameElement
from app.src.nlp.framenet_extractor import FramenetExtractor

# I can write some more tests that parse through this in much more detail, but not a priority
# In that case, I may also just build my own test contract and verify the proper values
# There may eventually be some NLP to verify as well
class FramenetExtractorTests(unittest.TestCase):
    def setUp(self):
        self.framenet = IFramenet()
        test_frame = MyFrame(frame_elements={'test': MyFrameElement(name='test', defn='test', type='test')})
        
        self.framenet.get_lus = MagicMock(return_value = [
            MyLU(pos='V', name='test1', defn='test', frame=test_frame),
            MyLU(pos='N', name='test2', defn='test', frame=test_frame)
        ])
        self.sut = FramenetExtractor(self.framenet)


    def test_flu_extractor(self):
        test_verb = 'test'
        result = self.sut.extract_flus_from_verb(test_verb)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, 'test1')

    def test_frame_element_extractor(self):
        test_frame = MyFrame(frame_elements={
            'test1': MyFrameElement(name='test1', defn='test', type='Core'),
            'test2': MyFrameElement(name='test2', defn='test', type='Core2')
        })
        result = self.sut.extract_core_fes(test_frame)

        self.assertEqual(len(result), 1)
        self.assertEqual(list(result.keys())[0], 'test1')

if __name__ == '__main__':
    unittest.main()