__author__ = 'David'

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

"""
div -> span
span -> p
"""


class MyHTMLParser(HTMLParser):

    current_tag = ''
    previous_tag = ''
    text_retrieved = ''

    def handle_starttag(self, tag, attrs):
        # print "Start tag:", tag
        self.previous_tag = self.current_tag
        self.current_tag = tag

    #    for attr in attrs:
    #        print "     attr:", attr
    """
    def handle_endtag(self, tag):
        print "End tag  :", tag
        #print self.text_retrieved
        # return self.text_retrieved
    """
    def handle_data(self, data):
        if self.current_tag == 'p' or (self.current_tag == 'span' and self.previous_tag == 'p'):
            # print "Data     :", data
            self.text_retrieved += data
            # print self.text_retrieved

    """
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
    def get_data(self):
        # print self.text_retrieved
        return self.text_retrieved

