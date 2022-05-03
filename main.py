from yattag import Doc, indent

BOOTSTRAP_IMPORT = '''<!-- Latest compiled and minified CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Latest compiled JavaScript -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>'''

GET_RANDOM_URL = 'talk_url = () => talks[Math.floor(Math.random() * talks.length)];'

UPDATE_URL_WITH_TALK = 'set_talk_link = () => document.getElementById("talk_link").href = talk_url();'

if __name__ == '__main__':
    doc, tag, text, line = Doc().ttl()

    doc.asis('<!DOCTYPE html>')

    with tag('html'):
        with tag('head'):
            doc.stag('meta', name='viewport', content='width=device-width')
            doc.asis(BOOTSTRAP_IMPORT)
            doc.asis('<script src="talks.js"></script>')

            with tag('script'):
                doc.asis(GET_RANDOM_URL)
                doc.asis(UPDATE_URL_WITH_TALK)

        with tag('body'):
            with tag('div', klass='container'):
                line('h1', 'Conference Talk Randomizer')
                doc.stag('hr')

                with tag('div'):
                    with tag('a', href='', id='talk_link'):
                        text('what to put here?')
                with tag('div'):
                    doc.stag('input', type='button', onclick='set_talk_link()',
                             value='Click to get a different random talk')

                with tag('script'):
                    doc.asis('set_talk_link();')

    with open('index.html', 'w') as file:
        file.write(doc.getvalue())
