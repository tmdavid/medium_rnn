__author__ = 'David'
import urllib2
from html_post_parser import MyHTMLParser as Mp


def chars_in_file(filename):
    f = open('..\posts_files\posts_'+filename, 'r').read()
    print len(f)


def scrap_a_page():
        hdr = {'User-Agent': "Magic Browser", 'Connection': 'keep-alive'}

        url = 'https://medium.com/@InVisionApp/designing-humane-augmented-reality-user-experiences-1dd67de9a80a'
        try:
            req = urllib2.Request(url, headers=hdr)
            response = urllib2.urlopen(req)
            html = response.read()
        except urllib2.HTTPError, e:
            print ('HTTPError = ' + str(e.code))

        parser = Mp()
        parser.feed(html.decode('utf-8'))
        post = parser.get_data()
        print post.encode('utf-8')


def main():
    """
        to run some tests on funcs
    """
    # chars_in_file('travel.txt')
    # https://medium.com/@InVisionApp/designing-humane-augmented-reality-user-experiences-1dd67de9a80a
    scrap_a_page()


if __name__ == '__main__':
    main()
