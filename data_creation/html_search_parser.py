__author__ = 'David'

from HTMLParser import HTMLParser


"""
div -> span
span -> p
"""


class SearchHTMLParser(HTMLParser):

    current_tag = ''
    previous_tag = ''
    text_retrieved = ''

    url_list = []

    def handle_starttag(self, tag, attrs):
        #print "Start tag:", tag
        self.previous_tag = self.current_tag
        self.current_tag = tag
        for attr in attrs:
            if self.previous_tag == 'span' and tag == 'a' and 'href' in attr[0]:
                # print "     attr:", attr[1]
                self.url_list.append(attr[1])

    """
    def handle_endtag(self, tag):
        print "End tag  :", tag

    def handle_data(self, data):
            print "Data     :", data

    def handle_comment(self, data):
        print "Comment  :", data

    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        print "Named ent:", c

    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        print "Num ent  :", c

    def handle_decl(self, data):
        print "Decl     :", data
"""
    def get_urls(self):
        # print self.url_list
        return self.url_list
