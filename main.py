from yattag import Doc, indent

BOOTSTRAP_IMPORT = '''<!-- Latest compiled and minified CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Latest compiled JavaScript -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>'''

GET_RANDOM_URL = 'talk_url = () => talks[Math.floor(Math.random() * talks.length)];'

UPDATE_URL_WITH_TALK = 'set_talk_link = () => document.getElementById("talk_link").href = talk_url();'

GET_YEAR_MONTH_OF_LATEST_TALK = """split_url = talks[0].split('/');
if (split_url.length > 1) {
  year = split_url[split_url.length - 3];
  month = split_url[split_url.length - 2];

} else {
  console.log('Unable to split the latest talk url.');
}
console.log(year + ' ' + month);
"""

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
                doc.asis(GET_YEAR_MONTH_OF_LATEST_TALK)

        with tag('body'):
            with tag('div', klass='container'):
                line('h1', 'Conference Talk Randomizer')
                doc.stag('hr')

                with tag('p'):
                    text('Instructions...')

                with tag('p'):
                    with tag('a', href='', id='talk_link'):
                        text('Click here to open a talk')
                with tag('p'):
                    doc.stag('input', type='button', onclick='set_talk_link()',
                             value='Click to get a different random talk')

                with tag('script'):
                    doc.asis('set_talk_link();')

    with open('index.html', 'w') as file:
        file.write(doc.getvalue())
