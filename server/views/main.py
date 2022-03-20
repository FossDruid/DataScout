# routes
from flask import Blueprint, render_template, url_for
from ..dataEngine.dataDriver import *

main = Blueprint('main', __name__)

@main.route('/')
def main_index():
    return render_template('/home.html')

@main.route('/404')
def error404():
    return render_template('/404.html', variable1="chad")

@main.route('/graphs')
def chartPage():
    dataForAnalysis = []
    graphChoice = ""
    userDataGetter(dataForAnalysis)
    print("Here's your data:  ")
    print(*dataForAnalysis)
    print('\n')
    graphChoice = graphSelector(dataForAnalysis, graphChoice)
    dataFormatter(dataForAnalysis, graphChoice)
    data = [
        ("01-01-2020", 1597),
        ("02-01-2020", 1456),
        ("03-01-2020", 1908),
        ("04-01-2020", 2910),
        ("05-01-2020", 2100),
        ("06-01-2020", 2430),
        ("07-01-2020", 2310),
        ("08-01-2020", 2030),
        ("09-01-2020", 2090),
        ("10-01-2020", 1930),
        ("11-01-2020", 2030),
        ("12-01-2020", 1650)
    ]
    print(data)

    labels = []
    values = []
    for row in data:
        labels.append(row[0])
        values.append(row[1])
    
    print(labels)
    print(values)
    return render_template("graphs.html", labels=labels, values=values)

if __name__ == '__main__':
    app.run(debug=True)