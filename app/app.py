from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(['http://127.0.0.1:9200'])

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search/results', methods=['GET', 'POST'])
def search_request():
    if request.method == 'POST':
        search_term = request.form['inputt']
        res = es.search(
            # index="scrape-sysadmins",
            index="blog-sysadmins", 
            size=20, 
            body={
                "query": {
                    "multi_match" : {
                        "query": search_term, 
                        "fields": [
                            "url", 
                            "title", 
                            "tags"
                        ] 
                    }
                }
            }
        )
        return render_template('results.html', res=res )

    # return render_template('results.html' )

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.debug = True
    app.run()