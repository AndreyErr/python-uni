import unittest
from main import main



class TestEeE(unittest.TestCase):
    def testStates1(self):
        f = main()

        self.assertEqual(f.crawl(), 1)
        self.assertEqual(f.getstate(), 'A')
        self.assertEqual(f.close(), 0)
        self.assertEqual(f.getstate(), 'B')
        self.assertEqual(f.exit(), 4)
        self.assertEqual(f.getstate(), 'C')
        self.assertEqual(f.exit(), 6)
        self.assertEqual(f.getstate(), 'D')
        self.assertEqual(f.close(), 7)
        self.assertEqual(f.getstate(), 'E')
        self.assertEqual(f.close(), 8)
        self.assertEqual(f.getstate(), 'F')


    def testStates2(self):
        f = main()

        self.assertEqual(f.crawl(), 1)
        self.assertEqual(f.getstate(), 'A')
        self.assertEqual(f.crawl(), 1)
        self.assertEqual(f.getstate(), 'A')
        self.assertEqual(f.close(), 0)
        self.assertEqual(f.getstate(), 'B')
        self.assertRaises(KeyError, f.crawl)
        self.assertEqual(f.exit(), 4)
        self.assertEqual(f.getstate(), 'C')
        self.assertEqual(f.exit(), 6)
        self.assertEqual(f.getstate(), 'D')
        self.assertRaises(KeyError, f.crawl)
        self.assertEqual(f.close(), 7)
        self.assertEqual(f.getstate(), 'E')
        self.assertRaises(KeyError, f.exit)
        self.assertEqual(f.close(), 8)
        self.assertEqual(f.getstate(), 'F')

if __name__ == '__main__':
    unittest.main()