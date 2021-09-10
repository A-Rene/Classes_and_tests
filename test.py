# write test for classes in model.py
import unittest
from model import LightNovel
from model import Manga
from model import Anime


# Test methods from the LightNovel class
class TestLightNovel(unittest.TestCase):
    """Tests for class LightNovel"""
    def setUp(self):
        """Create an instance to test with """
        self.instance = LightNovel('Moon-led Journy Accross Another World', 'Kino Kotora', 'Alpha Polis')

    def test_book_name(self):
        """Test the book_name method """
        self.instance.book
        title = self.instance.book_name("Dues lo Vult")
        self.assertEqual(title, self.instance.book)


    def test_one_sentence_sysopsis(self):
        """Test one_sentence_sysnopsis method"""
        self.instance.sysnopsis
        sentence = self.instance.one_sentence_sysnopsis("This is a test sentence.")
        self.assertIn("This is a test sentence.", sentence)

    def test_illistrator(self):
        """Test method light_novel_illistrator"""
        self.instance.illistrator
        name = "Random string"
        illistrator = self.instance.light_novel_illistrator(name)
        self.assertEqual(name, illistrator)

    def test_LightNoovel_volume(self):
        """Test the set_volume method"""
        x = 2
        self.instance.volume
        vol_no = self.instance.set_volume(x)
        self.assertEqual(x, vol_no)

# Tests for the Manga class | Manga only has one attribute not found in LightNovel
    def setUp(self):
        """Create a Manga instance to test with"""
        self.instance = Manga('Youjo Senki', 'Carlo Zen', 'Azumi Kei')

    def test_manga_artist(self):
        """Test the manga_artist method from the Manga class"""
        name = "Random Name"
        test = self.instance.manga_artist(name)
        self.assertEqual(name, test )

class TestAnime(unittest.TestCase):
    """Test the Anime class model py """

# Tests for methods of the Anime class
    def setUp(self):
        """Create a Anime instance"""
        self.instance = Anime("Anime", "Studio")

    def test_character_voice(self):
        """Test class: Anime Method: character_voice"""
        name = 'Random Name '
        test = self.instance.character_voice(name)
        self.assertEqual(name, test)

    def test_anime_characters(self):
        """Test class: Anime Method: anime_characters"""
        name = 'Random Name '
        test = self.instance.anime_characters(name)
        self.assertEqual(name, test)

    def test_main_character(self):
        """Test class: Anime Method: main_character"""
        name = 'Random Name '
        test = self.instance.main_character(name)
        self.assertEqual(name, test)

    def test_set_episode_number(self):
        """Test class: Anime method: episode_number """
        x = 12
        test = self.instance.set_episode_number(x)
        self.assertEqual(x, test)

    def test_composer(self):
        """Test class: Anime method: music_composer"""
        name = 'person'
        test = self.instance.music_composer(name)
        self.assertEqual(name, test)

    def test_show_producer(self):
        """Test class: Anime method:show_producer"""
        name = 'person'
        test = self.instance.show_producer(name)
        self.assertEqual(name, test)

    def test_one_sentence_sysopsis(self):
        """Test class: Anime method: one_sentence_sysnopsis"""
        sentence = "This is a simple sentence. "
        check = self.instance.one_sentence_sysnopsis(sentence)
        test  = self.instance.sysnopsis
        self.assertEqual(check, test)





if __name__ == '__main__':
    unittest.main()
