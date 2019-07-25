# Evan Widloski - 2019-04-18
# python-markdown extension for captions

from __future__ import absolute_import
from __future__ import unicode_literals
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.util import etree
import re


class CaptionsTreeprocessor(Treeprocessor):
    def run(self, doc):

        # iterate img tags
        for img in doc.findall('.//img'):

            if img.attrib['alt']:
                # replace img with figure
                img.tag = 'figure'

                # build inner img, figcaption
                inner_img = etree.SubElement(img, 'img')

                inner_img.set('src', img.attrib['src'])
                del img.attrib['src']

                if 'title' in img.attrib:
                    inner_img.set('title', img.attrib['title'])
                    del img.attrib['title']

                caption = etree.SubElement(img, 'figcaption')
                caption.text = img.attrib['alt']
                del img.attrib['alt']

class CaptionsExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        priority_string = '>attr_list' if 'attr_list' in md.treeprocessors else '_end'
        md.treeprocessors.add(
            'captions', CaptionsTreeprocessor(md), priority_string
        )

def makeExtension(**kwargs):  # pragma: no cover
    return CaptionsExtension(**kwargs)
