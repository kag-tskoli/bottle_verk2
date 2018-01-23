import os
from bottle import run, route, static_file, error, request


@route('/')
def index():
    return '<h2>Verkefni 2</h2>' \
           '<a href="/a">Liður A</a>' \
           ' <a href="/b">Liður B</a>'

@route('/a')
def lidura():
    return '<h2>Liður A</h2>' \
           '<a href="/page/1">Síða 1</a>' \
           ' <a href="/page/2">Síða 2</a>' \
           ' <a href="/page/3">Síða 3</a>'

@route('/page/<n>')
def page(n):
    return '<h3>Þetta er síða ' + n + '</h3>' \
            '<a href="/a">Fara til baka</a>'


@route('/b')
def lidurb():
    return '<h2>Liður B</h2>' \
           '<h3>Veldu uppáhaldsdýrið:</h3>' \
           '<a href="/favorite?image=kind"><img src="/static/kind.svg" width="150"></a>' \
           '<a href="/favorite?image=snigill"><img src="/static/snigill.svg" width="150"></a>' \
           '<a href="/favorite?image=kolkrabbi"><img src="/static/kolkrabbi.svg" width="150"></a>'

@route('/favorite')
def favorite():
    image = request.query.image

    return '<h2>Uppáhaldsdýrið þitt er: </h2>' \
           '<img src="/static/' + image +'.svg" width="200">' \
           '<h4><a href="/b">Til baka</a></h4>'


@error(404)
def error404(error):
    return '<h1>Síðan sem þú baðst um er ekki til...</h1>'

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root="./myfiles")

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
