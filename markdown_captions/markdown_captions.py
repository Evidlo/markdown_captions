# Evan Widloski - 2019-04-18
# python-markdown extension for captions

from __future__ import absolute_import
from __future__ import unicode_literals
from markdown.extensions import Extension
from markdown.util import etree
from markdown.inlinepatterns import LinkInlineProcessor

CAPTION_RE = r'\!\[(?=[^\]])'

class ImageInlineProcessor(LinkInlineProcessor):
    """ Return a img element from the given match. """

    def handleMatch(self, m, data):
        text, index, handled = self.getText(data, m.end(0))
        if not handled:
            return None, None, None

        src, title, index, handled = self.getLink(data, index)
        if not handled:
            return None, None, None

        fig = etree.Element('figure')
        img = etree.SubElement(fig, 'img')
        cap = etree.SubElement(fig, 'figcaption')

        img.set('src', src)

        if title is not None:
            img.set("title", title)

        cap.text = text

        return fig, m.start(0), index


class CaptionsExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.register(ImageInlineProcessor(CAPTION_RE, md), 'caption', 151)


def makeExtension(**kwargs):  # pragma: no cover
    return CaptionsExtension(**kwargs)
