import okno

### тест 1. проверка пароля для пользователя под логином vasya
def test1_password():
     assert okno.list['vasya'] == 123

### тест 2. проверка пароля для пользователя под логином lilya
def test2_password():
     assert okno.list['lilya'] == 555