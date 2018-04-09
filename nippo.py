
import datetime

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for


app = Flask(__name__)


class Nippo(object):
    def __init__(self):
        self.main_text = []
        self.main_text.append('【作業予定】\n\n')
        self.main_text.append('\n\n【作業実績】\n\n')
        self.main_text.append('\n\n【問題】\n\n')
        self.main_text.append('\n\n【対応策】\n\n')
        self.main_text.append('\n\n【所感】\n\n')
        self.main_text.append('\n\n【連絡事項】\n\n')
        self.main_text.append('\n\n【翌日の作業予定】\n\n')


    def add_text(self, index, text):
        self.main_text.insert(index, text)

    def create_str(self):
        out_str = ''
        for text in self.main_text:
            out_str += text
        return out_str

    def output_txt(self):
        out_str = self.create_str()

        today_str = datetime.date.today().isoformat()
        filepath = today_str.replace('-', '') + '.txt'
        with open(filepath, 'wt') as outfile:
            outfile.write(out_str)


@app.route('/')
def index():
    title = 'nippo'
    return render_template('index.html', title=title)


@app.route('/post', methods=['GET', 'POST'])
def post():
    title = 'nippo'
    if request.method == 'POST':
        nippo = Nippo()
        kyoyotei = request.form['kyoyotei']
        nippo.add_text(1, str(kyoyotei))
        jiseki = request.form['jiseki']
        nippo.add_text(3, str(jiseki))
        mondai = request.form['mondai']
        nippo.add_text(5, str(mondai))
        taio = request.form['taio']
        nippo.add_text(7, str(taio))
        shokan = request.form['shokan']
        nippo.add_text(9, str(shokan))
        renraku = request.form['renraku']
        nippo.add_text(11, str(renraku))
        asitayotei = request.form['asitayotei']
        nippo.add_text(13, str(asitayotei))

        nippo.output_txt()
        main_text = nippo.create_str()
        return render_template('saved.html',
                                main_text=main_text)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()
