from flask import Flask, request, redirect, url_for, render_template, jsonify
from app.service import Service

app = Flask(__name__)
noun_service = Service()

last_entry = ''
@app.route('/')
def index():
    nouns = noun_service.get_all_nouns()
    return render_template('russiannouns.html', nouns=[nouns[i:i+12] for i in range(0, len(nouns), 12)])

@app.route('/submit_noun', methods=['POST'])
def submit_noun():
    global last_entry

    nominative_form = request.form['form']

    if not noun_service.is_cyrillic(nominative_form):
        cyrillic_form = noun_service.convert_to_cyrillic(nominative_form)
    else:
        cyrillic_form = nominative_form
    definition = request.form['definition']
    gender_int = int(request.form['gender'])

    last_entry = noun_service.add_noun(cyrillic_form, definition, gender_int)

    return redirect(url_for('success'))

@app.route('/success')
def success():
    if last_entry:
        message = f'{last_entry} successfully entered into the database.' if last_entry else ''

    nouns = noun_service.get_all_nouns()
    return render_template('russiannouns.html', nouns=[nouns[i:i+12] for i in range(0, len(nouns), 12)], message=message)

@app.route('/convert_to_cyrillic', methods=['POST'])
def convert_to_cyrillic():
    data = request.json
    text = data.get('text')
    converted_text = noun_service.convert_to_cyrillic(text)
    return jsonify({'convertedText': converted_text})


@app.route('/flashcards', methods=['POST'])
def flashcards():
    selected_noun = noun_service.get_random_noun()

    if selected_noun:
        case_name = noun_service.get_case_name(selected_noun)
        number_name = noun_service.get_number_name(selected_noun)
        return render_template('flashcards.html', noun=selected_noun, case_name=case_name, number_name=number_name)

    return render_template('flashcards.html', message="No nouns have been added.")

@app.route('/refresh_database', methods=['POST'])
def refresh_database():
    noun_service.refresh_database()
    nouns = noun_service.get_all_nouns()
    return render_template('russiannouns.html', nouns=nouns)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
