import json

import quart
import quart_cors
from quart import request
import requests
from flask import jsonify
app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

# Keep track of todo's. Does not persist if Python session is restarted.
_TODOS = {}

@app.post("/todos/<string:username>")
async def add_todo(username):
    request = await quart.request.get_json(force=True)
    if username not in _TODOS:
        _TODOS[username] = []
    _TODOS[username].append(request["todo"])
    return quart.Response(response='OK', status=200)

@app.get("/weather/<string:city>")
async def get_weather(city):
    api_key = '55afa87f357f1a647f51e3aa5e47e54a'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)

@app.get("/profile/<string:symbol>")
async def get_profile(symbol):
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')

    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/profile?symbol={symbol}&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'

        
    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)

@app.get("/dividends/<string:symbol>")
async def get_dividends(symbol):
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    range = request.args.get('range', 'last')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/dividends?symbol={symbol}&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'
    if range:
        url += f'&range={range}'
    if start_date:
        url += f'&start_date={start_date}'
    if end_date:
        url += f'&end_date={end_date}'
        
    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)


@app.get("/splits/<string:symbol>")
async def get_splits(symbol):
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    range = request.args.get('range')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/splits?symbol={symbol}&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'
    if range:
        url += f'&range={range}'
    if start_date:
        url += f'&start_date={start_date}'
    if end_date:
        url += f'&end_date={end_date}'
        
    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)

@app.get("/earnings/<string:symbol>")
async def get_earnings(symbol):
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    type = request.args.get('type')
    period = request.args.get('period')
    outputsize = request.args.get('outputsize', 10)
    format = request.args.get('format', 'JSON')
    delimiter = request.args.get('delimiter')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/earnings?symbol={symbol}&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'
    if type:
        url += f'&type={type}'
    if period:
        url += f'&period={period}'
    if outputsize:
        url += f'&outputsize={outputsize}'
    if format:
        url += f'&format={format}'
    if delimiter:
        url += f'&delimiter={delimiter}'
    if start_date:
        url += f'&start_date={start_date}'
    if end_date:
        url += f'&end_date={end_date}'
        
    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)

@app.get("/earnings_calendar")
async def get_earnings_calendar():
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    outputsize = request.args.get('outputsize', 10)
    format = request.args.get('format', 'JSON')
    delimiter = request.args.get('delimiter')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/earnings_calendar?&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'
    if outputsize:
        url += f'&outputsize={outputsize}'
    if format:
        url += f'&format={format}'
    if delimiter:
        url += f'&delimiter={delimiter}'
    if start_date:
        url += f'&start_date={start_date}'
    if end_date:
        url += f'&end_date={end_date}'

        
    response = requests.get(url)
    data = response.json()
    if 'earnings' in data:
        data = data['earnings']
        

    return quart.Response(response=json.dumps(data), status=200)


@app.get("/ipo_calendar")
async def get_ipo_calendar():
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    # outputsize = request.args.get('outputsize', 10)
    # format = request.args.get('format', 'JSON')
    # delimiter = request.args.get('delimiter')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/ipo_calendar?&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'
    # if outputsize:
    #     url += f'&outputsize={outputsize}'
    # if format:
    #     url += f'&format={format}'
    # if delimiter:
    #     url += f'&delimiter={delimiter}'
    if start_date:
        url += f'&start_date={start_date}'
    if end_date:
        url += f'&end_date={end_date}'

        
    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)


@app.get("/statistics/<string:symbol>")
async def get_statistics(symbol):
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/statistics?symbol={symbol}&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'

    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)


@app.get("/insider_transactions/<string:symbol>")
async def get_transactions(symbol):
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/insider_transactions?symbol={symbol}&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'
        
    response = requests.get(url)
    data = response.json()
    if 'insider_transactions' in data:
        data = data['insider_transactions'][:100]
    return quart.Response(response=json.dumps(data), status=200)

@app.get("/income_statement/<string:symbol>")
async def get_income(symbol):
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    period = request.args.get('period')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/income_statement?symbol={symbol}&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'
    if period:
        url += f'&period={period}'
    if start_date:
        url += f'&start_date={start_date}'
    if end_date:
        url += f'&end_date={end_date}'
        
    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)


@app.get("/balance_sheet/<string:symbol>")
async def get_balance(symbol):
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    period = request.args.get('period')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/balance_sheet?symbol={symbol}&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'
    if period:
        url += f'&period={period}'
    if start_date:
        url += f'&start_date={start_date}'
    if end_date:
        url += f'&end_date={end_date}'
        
    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)

@app.get("/cash_flow/<string:symbol>")
async def get_cash(symbol):
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    period = request.args.get('period')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/cash_flow?symbol={symbol}&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'
    if period:
        url += f'&period={period}'
    if start_date:
        url += f'&start_date={start_date}'
    if end_date:
        url += f'&end_date={end_date}'
        
    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)

@app.get("/options/expiration/<string:symbol>")
async def get_options_expiration(symbol):
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    
    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/options/expiration?symbol={symbol}&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'
        
    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)

@app.get("/options/chain/<string:symbol>")
async def get_options_chain(symbol):
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    expiration_date = request.args.get('expiration_date')
    option_id = request.args.get('option_id')
    side = request.args.get('side')

    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/options/chain?symbol={symbol}&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'
    if expiration_date:
        url += f'&expiration_date={expiration_date}'
    if option_id:
        url += f'&option_id={option_id}'
    if side:
        url += f'&side={side}'
        
    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)


@app.get("/key_executives/<string:symbol>")
async def get_key_executives(symbol):
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    
    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/key_executives?symbol={symbol}&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'
        
    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)


@app.get("/institutional_holders/<string:symbol>")
async def get_institutional_holders(symbol):
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    
    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/institutional_holders?symbol={symbol}&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'
        
    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)

@app.get("/fund_holders/<string:symbol>")
async def get_fund_holders(symbol):
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    
    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/fund_holders?symbol={symbol}&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'
        
    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)

@app.get("/direct_holders/<string:symbol>")
async def get_direct_holders(symbol):
    exchange = request.args.get('exchange')
    mic_code = request.args.get('mic_code')
    country = request.args.get('country')
    
    api_key = '93245454f54c4bb89c7f4685821ba920'
    url = f'https://api.twelvedata.com/direct_holders?symbol={symbol}&apikey={api_key}&source=docs'

    if exchange:
        url += f'&exchange={exchange}'
    if mic_code:
        url += f'&mic_code={mic_code}'
    if country:
        url += f'&country={country}'
        
    response = requests.get(url)
    data = response.json()
    return quart.Response(response=json.dumps(data), status=200)



@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5001)

if __name__ == "__main__":
    main()