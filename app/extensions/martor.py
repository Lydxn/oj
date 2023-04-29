from dominate.tags import div, i, pre, span
from markdown.extensions import Extension
from markdown.extensions.fenced_code import FencedBlockPreprocessor
from textwrap import dedent

import re


class SampleIOPreprocessor(FencedBlockPreprocessor):
    FENCED_BLOCK_RE = re.compile(
        dedent(r'''
            (?P<fence>^(?:~{3,}|`{3,}))
            [ ]*sample[ ]*\n
            \[input\][ ]*\n
            (?P<input>.*?)\n
            \[output\][ ]*\n
            (?P<output>.*?)\n
            (?P=fence)[ ]*$
        '''),
        re.DOTALL | re.MULTILINE | re.VERBOSE
    )

    def run(self, lines):
        text = '\n'.join(lines)
        idx = 1
        while True:
            m = self.FENCED_BLOCK_RE.search(text)
            if not m:
                break

            sample = div(cls='sample')
            with sample:
                for type in 'input', 'output':
                    content = self._escape(m.group(type))
                    with div(cls=f'sample-box sample-{type}'):
                        with div(cls='sample-header'):
                            span(f'Sample {type.capitalize()} {idx}', cls='sample-title')
                            with span(cls='sample-copy'):
                                span('Copied!', cls='sample-copy-msg')
                                i(cls='sample-copy-icon fa-regular fa-copy')
                        pre(content, cls='sample-content')

            code = sample.render()
            placeholder = self.md.htmlStash.store(code)
            text = f'{text[:m.start()]}\n{placeholder}\n{text[m.end():]}'

            idx += 1

        return text.split('\n')


class SampleIOExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        md.preprocessors.register(SampleIOPreprocessor(md, self.getConfigs()), 'sample_io', 30)


def makeExtension(**kwargs):
    return SampleIOExtension(**kwargs)
