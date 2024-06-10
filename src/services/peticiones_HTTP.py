# pip3 install requests
# source venv/bin/activate
import requests
base = 'https://stage.micros.involverh.es/'


def send_get_headers(url, headers, code_http: int):
    try:
        req = requests.get(url, headers=headers)
        if req.status_code != code_http:
            raise Exception(f"comprueba el status code: {req.status_code}")
        # Try to decode the JSON response
        try:
            result = req.json()
            print(f"Status Code: {req.status_code}")
            return result
        except requests.exceptions.JSONDecodeError:
            result = req.text
            print("la respuesta no un JSON  valido" + result)
            print('get status: ' + str(req.status_code))
        assert req.status_code == code_http
        return result
    except Exception as e:
        print(f"Error: {e}")


def send_get(url, code_http: int):
    try:
        req = requests.get(url)
        if req.status_code != code_http:
            raise Exception(f"comprueba el status code: {req.status_code}")
        # Try to decode the JSON response
        try:
            result = req.json()
            print(f"Status Code: {req.status_code}")
            return result
        except requests.exceptions.JSONDecodeError:
            result = req.text
            print("la respuesta no un JSON  valido" + result)
            print('get status: ' + str(req.status_code))
        assert req.status_code == code_http
        return result
    except Exception as e:
        print(f"Error: {e}")


def send_post(url, my_body, code_http):
    try:
        req = requests.post(url, json=my_body)
        print('Post status:' + str(req.status_code))

        # Check if codeHttp is a single value or a range
        if isinstance(code_http, int):
            # Assert for exact code
            assert req.status_code == code_http
        else:
            # Assert for range using tuple unpacking
            min_code, max_code = code_http
            assert min_code <= req.status_code <= max_code

        resultado = req.json()
        headers = req.headers
        return resultado, headers
    except Exception as e:
        print('No paso el post', {e})


def send_patch(url, headers, my_body, code_http):
    try:
        req = requests.patch(url, headers=headers, json=my_body)
        print('Patch status: ' + str(req.status_code))
        assert req.status_code == code_http
    except Exception as e:
        print('No paso el patch', {e})


def send_put(url, headers, code_http):
    try:
        req = requests.put(url, headers=headers)
        print('PUT status: ' + str(req.status_code))
        assert req.status_code == code_http
        code = req.status_code
        return code
    except Exception as e:
        print('no paso la funcion put', {e})


def send_put_body(url, headers, my_body, code_http):
    try:
        req = requests.put(url, headers=headers, json=my_body)
        print(req.content)
        print('PUT status: ' + str(req.status_code))
        assert req.status_code == code_http
    except Exception as e:
        print('no paso la funcion put', {e})


def send_post_sin_body(url, code_http):
    try:
        req = requests.post(url)
        print('Post Sin body status: ' + str(req.status_code))
        print(req.json())
        assert req.status_code == code_http
    except Exception as e:
        print(' no paso el post', {e})


def send_post_headers_sin_body(url, headers, code_http):
    try:
        req = requests.post(url, headers=headers)
        if req.status_code != code_http:
            raise Exception(f"Unexpected status code: {req.status_code}")
        # Try to decode the JSON response
        try:
            result = req.json()
            print(f"Status Code: {req.status_code}")
            return result
        except requests.exceptions.JSONDecodeError:
            result = req.text
            print('Post status: ' + str(req.status_code))
        assert req.status_code == code_http
        return result
    except Exception as e:
        print(f"Error: {e}")


def send_post_headers(url, headers, my_body, code_http):
    try:
        # Send the POST request
        req = requests.post(url, headers=headers, json=my_body)
        # Check the response status code
        if req.status_code != code_http:
            raise Exception(f"Unexpected status code: {req.status_code}")
        # Try to decode the JSON response
        try:
            result = req.json()
            print(f"Status Code: {req.status_code}")
            return result
        except requests.exceptions.JSONDecodeError:
            result = req.text
            print("la respuesta no es un json pero " + result)
            print('Post status: ' + str(req.status_code))
        assert req.status_code == code_http
        return result
    except Exception as e:
        print(f"Error: {e}")


def send_delete(url, headers, my_body, code_http):
    try:
        req = requests.delete(url, headers=headers, json=my_body)
        print('Patch status: ' + str(req.status_code))
        print(req.json())
        assert req.status_code == code_http
        resultado = req.json()
        return resultado
    except Exception as e:
        print('No paso el delete', {e})

