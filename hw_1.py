def parse(query: str) -> dict:
    result = {}
    if '=' in query:
        list_kv = query.split('?')[1].split('&')
        for i in list_kv:
            if '=' in i:
                result[i.split('=')[0]] = i.split('=')[-1]
    return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/?name=ferret&color=purple&www') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&age=14') \
           == {'name': 'ferret', 'color': 'purple', 'age': '14'}
    assert parse('https://example.com/path/to/page?name=ferret&color=') == {'name': 'ferret', 'color': ''}
    assert parse('https://example.com') == {}
    assert parse('https://') == {}
    assert parse('https://example.com/path/to/page?name=ferret&=') == {'name': 'ferret', '': ''}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&age=14&gender=male') \
           == {'name': 'ferret', 'color': 'purple', 'age': '14', 'gender': 'male'}
    assert parse('https://example.com/path/to/page?name==ferret&color=') == {'name': 'ferret', 'color': ''}
    assert parse('https://example.com/path/to/page?name==ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&&color=purple') == {'name': 'ferret', 'color': 'purple'}
