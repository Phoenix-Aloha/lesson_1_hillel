def parse_cookie(query: str) -> dict:
    result = {}
    if '=' in query:
        list_kv = query.split(';')
        for i in list_kv:
            if '=' in i:
                result[i.split('=')[0]] = i.split('=', 1)[-1]
    return result


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima;age=28;color=purple') == {'name': 'Dima', 'age': '28', 'color': 'purple'}
    assert parse_cookie('name=Dima;;') == {'name': 'Dima'}
    assert parse_cookie('name=') == {'name': ''}
    assert parse_cookie('name==') == {'name': '='}
    assert parse_cookie('name=Dima;www') == {'name': 'Dima'}
    assert parse_cookie('name') == {}
    assert parse_cookie('name=Dima;age=28;=') == {'name': 'Dima', 'age': '28', '': ''}
    assert parse_cookie('name=Dima=User;age=28;gender=male;') == {'name': 'Dima=User', 'age': '28', 'gender': 'male'}
    assert parse_cookie('name=Dima;age=28') == {'name': 'Dima', 'age': '28'}
