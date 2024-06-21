# pip3 install requests
# source venv/bin/activate
import requests

base = 'https://stage.micros.involverh.es/'


def send_get_headers(url, headers, code_http: int):
    try:
        req = requests.get(url, headers=headers)
        # Try to decode the JSON response
        try:
            result = req.json()
            print(f"Status Code: {req.status_code}")
            return result
        except requests.exceptions.JSONDecodeError:
            result = req.text
            print("la respuesta no un JSON  valido" + result)
            print('get status: ' + str(req.status_code))
        if req.status_code == code_http:
            return result
        else:
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0


def send_get(url, code_http: int):
    try:
        req = requests.get(url)
        # Try to decode the JSON response
        try:
            result = req.json()
            print(f"Status Code: {req.status_code}")
            return result
        except requests.exceptions.JSONDecodeError:
            result = req.text
            print("la respuesta no un JSON  valido" + result)
            print('get status: ' + str(req.status_code))
        if req.status_code == code_http:
            return result
        else:
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0


def send_post(url, my_body, code_http):
    try:
        req = requests.post(url, json=my_body)
        print('el codigo recibido es: ' + str(req.status_code))

        # Check if codeHttp is a single value or a range
        if isinstance(code_http, int):
            # Assert for exact code
            assert req.status_code == code_http
        else:
            respuesta = req.json()
            print(respuesta)
            # Assert for range using tuple unpacking
            min_code, max_code = code_http
            assert min_code <= req.status_code <= max_code

        resultado = req.json()
        headers = req.headers
        return resultado, headers
    except Exception as e:
        print('No paso el post', e)
        return 0, 'no paso el post'


def send_patch(url, headers, my_body, code_http):
    try:
        req = requests.patch(url, headers=headers, json=my_body)
        print('Patch status: ' + str(req.status_code))
        if req.status_code == code_http:
            return 1
        else:
            return 0
    except Exception as e:
        print(f'No paso el patch, {e}')
        return 0


def send_put(url, headers, code_http):
    try:
        req = requests.put(url, headers=headers)
        assert req.status_code == code_http
        code = req.status_code
        if code_http == code:
            print('PUT status: ' + str(req.status_code))
    except Exception as e:
        print('no paso la funcion put', e)
        return 0


def send_put_body(url, headers, my_body, code_http):
    try:
        req = requests.put(url, headers=headers, json=my_body)
        print('PUT status: ' + str(req.status_code))
        assert req.status_code == code_http
    except Exception as e:
        print('no paso la funcion put', e)
        return 0


def send_post_sin_body(url, code_http):
    try:
        req = requests.post(url)
        print('Post sin body status: ' + str(req.status_code))
        print(req.json())
        if req.status_code == code_http:
            return 1
        else:
            return 0
    except Exception as e:
        print('No paso el post', e)
        return 0


def send_post_headers_sin_body(url, headers, code_http):
    try:
        req = requests.post(url, headers=headers)
        if req.status_code == code_http:
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
        else:
            print('Post status: ' + str(req.status_code))
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0


def send_post_headers(url, headers, my_body, code_http):
    try:
        # Send the POST request
        req = requests.post(url, headers=headers, json=my_body)
        # Check the response status code
        if req.status_code != code_http:
            print(f"error de codigo: {req.status_code}")
            return 0
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
        return 0


def send_delete(url, headers, my_body, code_http):
    try:
        req = requests.delete(url, headers=headers, json=my_body)
        print('Patch status: ' + str(req.status_code))
        if req.status_code == code_http:
            if req.json() == None:
                print('La respuesta esta vacia pero el codigo es: ', str(req.status_code))
                resultado = req.text
                return resultado
            else:
                print(req.json())
        else:
            return 0
    except Exception as e:
        print('No paso el delete', e)
        return 0


def send_delete_sin_body(url, headers, code_http):
    try:
        req = requests.delete(url, headers=headers)
        print('Patch status: ' + str(req.status_code))
        if req.status_code == code_http:
            return 1
        else:
            return 0
    except Exception as e:
        print('No paso el delete', e)
        return 0
