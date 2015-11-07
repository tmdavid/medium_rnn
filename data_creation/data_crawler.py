__author__ = 'David'

import medium as Me
import urllib2
from html_post_parser import MyHTMLParser as Mp
from html_search_parser import SearchHTMLParser as Sp
from selenium_scroll_down import url_navigation as Un

urls = ['https://medium.com/@hadrielle/it-has-been-a-couple-of-weeks-since-i-posted-my-latest-story-2900c5d06f2a',
        'https://medium.com/@hadrielle/i-have-voted-22533a41b26f',
        'https://medium.com/@hadrielle/ready-steady-go-c638b4ef0962',
        'https://medium.com/@hadrielle/leuven-arrival-b7bd3ff8e8b3',
        'https://medium.com/@hadrielle/leuven-first-thoughts-e9c0a8ba99cb',
        'https://medium.com/@hadrielle/about-the-blog-8d214fbee2e9'
        ]

hdr = {'User-Agent': "Magic Browser",
       'Connection': 'keep-alive'}

# ' ' == %20

# 'travel', 'sports',
topics_list = ['design', 'user%20experience', 'technology', 'education', 'startup', 'UX', 'Culture', 'tech']

times = 300
print times
print topics_list

# 'https://medium.com/search?q=travel'

for topic in topics_list:
    scroll_to_bot = Un()
    parser_search = Sp()
    Sp.url_list = []
    filename = topic+'.txt'
    f = open('..\posts_files\posts_'+filename, 'a')
    topic_url = 'https://medium.com/search?q=' + topic
    print 'getting posts from medium.com, about %s' % topic
    # first number is many scrolls
    page_source = scroll_to_bot.scroll_down_many_times(topic_url)
    parser_search.feed(page_source)

    urls = parser_search.get_urls()

    # Parseja posts concrets
    print 'parsing %d urls about %s' % (len(urls), topic)
    for idx, url in enumerate(urls):
        print 'parsing url %d/%d: %s' % (idx, len(urls), url)
        try:
            req = urllib2.Request(url, headers=hdr)
            response = urllib2.urlopen(req)
            html = response.read()
        except urllib2.HTTPError, e:
            print ('HTTPError = ' + str(e.code))

        parser = Mp()
        parser.feed(html.decode('utf-8'))
        post = parser.get_data()
        f.write(post.encode('utf-8'))
        f.write('\n\n')


