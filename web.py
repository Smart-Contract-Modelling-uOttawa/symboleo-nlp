import os
from flask import Flask, request, render_template, jsonify, session
from app.web_lib.web_dependencies import WebDependencyBuilder

template_dir = os.path.relpath('app/web_lib/templates') 
static_dir = os.path.relpath('app/web_lib/static')


app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = 'your-secret-key'  # Set a secret key for session encryption

use_fake_nlp = True
deps = WebDependencyBuilder.build(use_fake_nlp)


@app.route("/")
def index():
    session['unique_key'] = 'test' # can randomly generate this...
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/contract', methods=['GET'])
def fetch_contract():
    try:
        contract_id = request.args['id']
        session['contract_id'] = contract_id
        result = deps.contract_fetcher.fetch(contract_id, session['unique_key'])
        
        return render_template('contract.html', contract=result)
    except Exception as e:
        print(e)
        return render_template('error.html', msg='Contract not found!')


@app.route('/parameter', methods=['POST'])
def select_parameter():
    # Store the parm
    parm = request.form.get('parameter')
    nl_key, parm_key = parm.split('.')
    session['nl_key'] = nl_key
    session['parm_key'] = parm_key 

    units = deps.parameter_selector.select(
        session['contract_id'], 
        session['unique_key'],
        nl_key,
        parm_key
    )

    return jsonify({'units': units})

# May need one for selecting unit (get the options, etc..)
## Or this may be internal to the js

@app.route('/value', methods=['POST'])
def process_value():
    input_id = request.form.get('input_id')
    value = request.form.get('value')

    units = deps.value_processor.process(
        session['contract_id'], 
        input_id, 
        value,
        session['unique_key']
    )

    return jsonify({'units': units})


@app.route('/submit', methods=['POST'])
def submit_refinement():
    updated_contract = deps.refinement_submitter.submit(
        session['contract_id'], 
        session['nl_key'], 
        session['parm_key'],
        session['unique_key']
    )

    return render_template('contract.html', contract=updated_contract)


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)