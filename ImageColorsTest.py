import unittest
from ImageColors import ImageColors


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.imColor = ImageColors('./image.jpg')

    def test_raise_exeption_on_non_existing_file(self) -> None:
        with self.assertRaises(FileExistsError) as cx:
            ImageColors('./aeaze.jpg')
            self.assertTrue(
                "File './aeaze.jpg' does not exists" in cx.exception)

    def test_get_colors_count(self) -> None:
        self.assertEqual(self.imColor.count(), 62842)

    def test_get_main_color(self) -> None:
        self.assertEqual(self.imColor.get_main_color(), '28,26,66')

    def test_colors_list_correctly_formated(self) -> None:
        colors_list = self.imColor.get_colors_list()
        colors = self.imColor.colors
        self.assertIsInstance(colors_list, list)
        self.assertIsInstance(colors_list[0], str)
        self.assertIsInstance(colors, list)
        self.assertIsInstance(colors[0], tuple)
        self.assertIsInstance(colors[0][0], str)
        self.assertIsInstance(colors[0][1], int)


if __name__ == '__main__':
    unittest.main()
