import unittest
import yaml
import argparse
from selenium import webdriver
from copy import deepcopy


class selenium_tests(object):

    @classmethod
    def get_all_test_conf(self, test_conf_file):
        with open(test_conf_file, "r") as fHndl:
            self.all_test_conf = yaml.safe_load(fHndl)

    def get_selenium_driver(self, browser):
        driver = None
        try:
            if browser == 'chrome':
                driver = webdriver.Chrome()
            elif browser == 'safari':
                driver = webdriver.Safari()
            else:
                pass
        except exception as e:
            print(str(sys.exc_info()[0]))
            print(str(sys.exc_info()[1]))
        finally:
            return driver

    def setup_test_conf(self):
        for k in selenium_tests.all_test_conf['test_config'][self.test_name]:
            self.conf.setdefault(k, deepcopy(selenium_tests.all_test_conf[
                'test_config'][self.test_name][k]))
        for k in selenium_tests.all_test_conf['default_test_config']:
            self.conf.setdefault(k, deepcopy(selenium_tests.all_test_conf[
                'default_test_config'][k]))

        if self.conf['skip']:
            self.skipTest("Test is marked skip in test_conf.yml")

        self.driver = self.get_selenium_driver(self.conf['browser'])
        self.assertFalse(not self.driver, "No Selenium driver for browser %s "
                         % (self.conf['browser']))

        self.urls = [selenium_tests.all_test_conf['url_map'][url]
                     for url in self.conf['urls']]
        self.assertFalse(len(self.urls) == 0, "No Urls in test conf")


class TestWordLength(selenium_tests, unittest.TestCase):
    DOCUMENTATION = """
    Assert that the dynamic text (the lorem ipsum text block) on the
    page contains a word at least 10 characters in length.
    Stretch goal:
    Print the longest word on the page.
    """

    def __init__(self, *args, **kwargs):
        super(TestWordLength, self).__init__(*args, **kwargs)
        self.test_name = "word_length"
        self.conf = {}

    def setUp(self):
        self.setup_test_conf()
        if self.conf['xpaths'] == []:
            self.skipTest("No xpath in test conf")

    def test_word_length(self):
        wl_dict = {}
        for url in self.urls:
            dyn_text = {}
            self.driver.get(url)
            for iter in range(2):
                for path in self.conf['xpaths']:
                    dyn_text.setdefault((path, iter), "")
                    ele = self.driver.find_element_by_xpath(path)
                    dyn_text[(path, iter)] = ele.text.strip()
                self.driver.refresh()
            for path in self.conf['xpaths']:
                if dyn_text[(path, 0)] != dyn_text[(path, 1)]:
                    for word in (dyn_text[(path, 0)].split() +
                                 dyn_text[(path, 1)].split()):
                        wl_dict.setdefault(len(word), set()).add(word)

        if self.conf['stretch']:
            max_word_len = max(wl_dict.keys())
            print("\nAll word_length: %r" % (sorted(wl_dict.keys())))
            print("Longest words are %r character long" % (max_word_len))
            print("Longest words on the page: %r" % (wl_dict[max_word_len]))

        self.assertTrue(int(self.conf['word_length']) in wl_dict.keys())

    def tearDown(self):
        self.driver.quit()


class TestAvatar(selenium_tests, unittest.TestCase):
    DOCUMENTATION = """
    Assert that the "Punisher" image (silhouette with a skull on his chest)
    does not appear on the page.
    This test may pass or fail on any given execution depending on whether
    the punisher happens to be on the page.
    Stretch goal:
    Give names to each avatar that can appear on the page and print out each
    avatars name.
    """

    def __init__(self, *args, **kwargs):
        super(TestAvatar, self).__init__(*args, **kwargs)
        self.test_name = "avatar"
        self.conf = {}

    def setUp(self):
        self.setup_test_conf()
        self.punisher_url = selenium_tests.all_test_conf['avatar_src_map'][
            self.conf['avatar']]

    def test_avatar(self):
        avatar_urls = set()

        for url in self.urls:
            self.driver.get(url)
            for ele in self.driver.find_elements_by_css_selector("img"):
                avatar_urls.add(ele.get_attribute("src"))

        if self.conf['stretch']:
            print("\nAll avatars appearing on the page")
            for name, url in selenium_tests.all_test_conf[
                    'avatar_src_map'].items():
                if url in avatar_urls:
                    print(name)

        self.assertFalse(self.punisher_url in avatar_urls,
                         "Punisher avatar is present on the page")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", dest="conf_file", default="test_conf.yml",
                        help='test configuration file')
    args = parser.parse_args()
    selenium_tests.get_all_test_conf(args.conf_file)
    unittest.main()
