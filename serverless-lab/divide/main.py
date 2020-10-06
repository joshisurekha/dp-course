def entry(request):
    request_json = request.get_json()
    request_args = request.args
    num1 = None
    num2 = None
    if request_json:
        num1 = int(request_json.get('num1'))
        num2 = int(request_json.get('num2'))
    elif request_args:
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
    if num2 == 0:
        return "I'm sorry, Dave. I can't let you divide by zero."
    if num1 and num2:
        return f"{num1} / {num2} = {num1/num2}"
    return f"Error. At least one number did not resolve. Received num1: {num1}, num2: {num2}"
