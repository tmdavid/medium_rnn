__author__ = 'David'

from selenium import webdriver
import time

class url_navigation:

    driver = webdriver.Chrome(executable_path=r"C:\scisoft\chromedriver.exe")
    driver.maximize_window()

    def scroll_down_many_times(self, url):

        url_search = url
        self.driver.get(url_search)
        # scroll down to the last tweet until there is no more tweets loaded
        '''
        medium loads in sets of 10, so if i want about 1k posts, 100 iterations
        '''
        last_height = 0
        current_height = 1
        number_scrolls = 0
        while last_height != current_height:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            last_height = current_height
            current_height = self.driver.execute_script("return document.body.scrollHeight")
            print 'last h %d -- %d current h' % (last_height, current_height)
            number_scrolls += 1
            if number_scrolls % 10 == 0:
                print 'scrolling down ...'


        return self.driver.page_source
