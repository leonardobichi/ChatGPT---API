from flask import Flask, render_template,request
import openai

app = Flask(__name__)
openai.api_key = 'INGRESAR-API-OPENAI'
questionsYo = []
answerIA = []
@app.route('/', methods=['GET','POST'])

def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.form['question']:
        question = 'HUMANO: ' + request.form['question']

        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = question,
            temperature = 0.2,
            max_tokens = 200,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0.6
        )

        answer = 'ROBOT: ' + response.choices[0].text.strip()
        questionsYo.append(question)
        answerIA.append(answer)
        lista_conversartions = zip(questionsYo, answerIA)

        return render_template('index.html', chat = lista_conversartions)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)