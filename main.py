from htmgem.tags import *

BOOTSTRAP_IMPORT = '''<!-- Latest compiled and minified CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Latest compiled JavaScript -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
'''

if __name__ == '__main__':
    html_string = \
        html(children=[
            head(children=[
                meta({'name': 'viewport', 'content': 'width=device-width'}),
                BOOTSTRAP_IMPORT,
                link({'rel': 'icon', 'href': 'mic-fill.png'}),
                script({'src': "talks.js"}),
                script({'src': "scripts.js"}),
                title('General Conference Talk Randomizer')
            ]),
            body([
                div({'class': 'container'}, children=[
                    h1('General Conference Talk Randomizer'),
                    hr(),
                    p('''The following link leads to a random conference talk, chosen from all of the talks given in 
                    general conference since April 1971.<br>50% of the time the talk will be chosen from the most recent
                     conference.'''),
                    p(a({'href': '', 'id': 'talk_link', 'target': '_blank'}, children="Open a talk's page")),
                    # TODO p([
                    #     input_({'type': 'checkbox', 'id': 'prioritize_latest'}),
                    #     label({'for': 'prioritize_latest'},
                    #           children='&nbsp;Uncheck the box (and refresh or click the button) to ...'),
                    # ]),
                    p(' Click the button to change the link to a different random talk, or refresh the page.'),
                    p(input_({'type': 'button', 'onclick': 'set_talk_link()', 'value': 'Change talk link'})),
                    script('set_talk_link();')
                ]),
                div({'class': 'container'}, hr()),
                div({'class': 'container'}, children=[
                    div({'class': 'row justify-content-between'}, [
                        div({'class': 'col-6'}, children=['This website is NOT an official website of ',
                                                          a({'href': 'https://www.churchofjesuschrist.org/'},
                                                            'The Church of Jesus Christ of Latter-day Saints.')
                                                          ]),
                        div({'class': 'col-1'}, [
                            a({'href': 'https://github.com/thetaylors/pyConferenceTalkRandomizer'},
                              '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                          class="bi bi-github" viewBox="0 0 16 16"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 
                          5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48
                          -.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07
                          -.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08
                          -2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2
                          -.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73
                          .54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42
                          -3.58-8-8-8z"/></svg>''' + '&nbsp;Source')
                        ])
                    ])
                ])
            ])
        ])

    with open('index.html', 'w') as file:
        file.write(html_string)

    # TODO kick off the process to deploy the file to AWS
    #  what about a separate script or something, we don't want to 'deploy to prod' every time a change is made
