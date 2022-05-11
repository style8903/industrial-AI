from durable.lang import *

# m.test : Test name
# m.number : Tube 번호
# m.amount : 혈액량
# m.bar_label : 라벨 여부
# m.bar_db : DB 존재 여부
# m.cap_exist : 캡 존재 여부
# m.cap_color : 캡 컬러
# m.tube_length : Tube 길이
# m.arrive : 목적지
# m.test_result : 검사결과
# m.type_result : tube 타입

with ruleset('kim_Rule'):
    # 규칙 1 : Test1은 혈액량이 50%이하이면 Error이다.
    @when_all((m.test == 'test1') & (m.amount <= 50))
    def result_1(c):
        c.assert_fact({'number' : c.m.number, 'test_name' : c.m.test, 'test_result' : 'error'})
        print('Input Num : {0}, Test Processing.......'.format(c.m.number))

    # 규칙 2 : Test1은 혈액량이 80%이상이면 Error이다.
    @when_all((m.test == 'test1') & (m.amount >= 80))
    def result_2(c):
        c.assert_fact({'number' : c.m.number, 'test_name' : c.m.test, 'test_result' : 'error'})
        print('Input Num : {0}, Test Processing.......'.format(c.m.number))

    # 규칙 3 : Test1은 혈액량이 50~80이면 Pass이다.
    @when_all((m.test == 'test1') & (m.amount < 80) & (m.amount > 50))
    def result_3(c):
        c.assert_fact({'number' : c.m.number, 'test_name' : c.m.test, 'test_result' : 'pass'})
        print('Input Num : {0}, Test Processing.......'.format(c.m.number))

    # 규칙 4 : Test2는 Barcod 라벨이 없다면 Error이다.
    @when_all((m.test =='test2') & (m.bar_label == 'false'))
    def result_4(c):
        c.assert_fact({'number' : c.m.number, 'test_name' : c.m.test, 'test_result' : 'error'})
        print('Input Num : {0}, Test Processing.......'.format(c.m.number))

    # 규칙 5 : Test2는 Barcod 라벨이 있다면 pass이다.
    @when_all((m.test == 'test2') & (m.bar_label == 'true'))
    def result_5(c):
        c.assert_fact({'number': c.m.number, 'test_name': c.m.test, 'test_result': 'pass'})
        print('Input Num : {0}, Test Processing.......'.format(c.m.number))

    # 규칙 6 : Test3는 Barcode가 DB에 없다면 Error이다.
    @when_all((m.test == 'test3') & (m.bar_db == 'false'))
    def result_6(c):
        c.assert_fact({'number': c.m.number, 'test_name': c.m.test, 'test_result': 'error'})
        print('Input Num : {0}, Test Processing.......'.format(c.m.number))

    # 규칙 7 : Test3는 Barcode가 DB에 있다면 Pass이다.
    @when_all((m.test == 'test3') & (m.bar_db == 'true'))
    def result_7(c):
        c.assert_fact({'number': c.m.number, 'test_name': c.m.test, 'test_result': 'pass'})
        print('Input Num : {0}, Test Processing.......'.format(c.m.number))

    # 규칙 8 : Test4는 Tube Cap이 없다면 Error이다.
    @when_all((m.test == 'test4') & (m.cap_exist == 'false'))
    def result_8(c):
        c.assert_fact({'number': c.m.number, 'test_name': c.m.test, 'test_result': 'error'})
        print('Input Num : {0}, Test Processing.......'.format(c.m.number))

    # 규칙 9 : Test4는 Tube Cap이 있다면 Pass이다.
    @when_all((m.test == 'test4') & (m.cap_exist == 'true'))
    def result_9(c):
        c.assert_fact({'number': c.m.number, 'test_name': c.m.test, 'test_result': 'pass'})
        print('Input Num : {0}, Test Processing.......'.format(c.m.number))

    # 규칙 10 : Test5는 Cap Color가 Red이고 길이가 100이하면 TYPE1이다.
    @when_all((m.test == 'test5') & (m.cap_color == 'red') & (m.tube_length <= 100))
    def result_10(c):
        c.assert_fact({'number': c.m.number, 'test_name': c.m.test, 'type_result': 'TYPE1'})
        print('Input Num : {0}, Test Processing.......'.format(c.m.number))

    # 규칙 11 : Test5는 Cap Color가 Red이고 길이가 100을 초과하면 TYPE2이다.
    @when_all((m.test == 'test5') & (m.cap_color == 'red') & (m.tube_length > 100))
    def result_11(c):
        c.assert_fact({'number': c.m.number, 'test_name': c.m.test, 'type_result': 'TYPE2'})
        print('Input Num : {0}, Test Processing.......'.format(c.m.number))

    # 규칙 12 : Test5는 Cap Color가 Blue이고 길이가 100이하면 TYPE3이다.
    @when_all((m.test == 'test5') & (m.cap_color == 'blue') & (m.tube_length <= 100))
    def result_12(c):
        c.assert_fact({'number': c.m.number, 'test_name': c.m.test, 'type_result': 'TYPE3'})
        print('Input Num : {0}, Test Processing.......'.format(c.m.number))

    # 규칙 13 : Test5는 Cap Color가 Blue이고 길이가 100을 초과하면 TYPE4이다.
    @when_all((m.test == 'test5') & (m.cap_color == 'blue') & (m.tube_length > 100))
    def result_13(c):
        c.assert_fact({'number': c.m.number, 'test_name': c.m.test, 'type_result': 'TYPE4'})
        print('Input Num : {0}, Test Processing.......'.format(c.m.number))

    # 규칙 14 : Test5는 Cap Color가 Green이고 길이가 100이하면 TYPE5이다.
    @when_all((m.test == 'test5') & (m.cap_color == 'green') & (m.tube_length <= 100))
    def result_14(c):
        c.assert_fact({'number': c.m.number, 'test_name': c.m.test, 'type_result': 'TYPE5'})
        print('Input Num : {0}, Test Processing.......'.format(c.m.number))

    # 규칙 15 : Test5는 Cap Color가 Green이고 길이가 100을 초과하면 TYPE6이다.
    @when_all((m.test == 'test5') & (m.cap_color == 'green') & (m.tube_length > 100))
    def result_15(c):
        c.assert_fact({'number': c.m.number, 'test_name': c.m.test, 'type_result': 'TYPE6'})
        print('Input Num : {0}, Test Processing.......'.format(c.m.number))


    # 결과 출력
    @when_all(m.test_result == 'error')
    def print_result_1(c):
        print('Number : {0} , Test : {1} , Test Result : Error Tube!\n'.format(c.m.number, c.m.test_name))

    @when_all(m.test_result == 'pass')
    def print_result_2(c):
        print('Number : {0} , Test : {1} , Test Result : Passed Tube!\n'.format(c.m.number, c.m.test_name))

    @when_all((m.test_name == 'test5') & (m.type_result != None))
    def print_result_3(c):
        print('Number : {0} , Test : {1} , TUBE TYPE : {2}\n'.format(c.m.number, c.m.test_name, c.m.type_result))


#사실 데이터 입력

#Test 1 데이터 입력
assert_fact('kim_Rule', {'number' : '1', 'test' : 'test1', 'amount' : 80})
assert_fact('kim_Rule', {'number' : '2', 'test' : 'test1', 'amount' : 50})
assert_fact('kim_Rule', {'number' : '3', 'test' : 'test1', 'amount' : 60})

#Test 2 데이터 입력
assert_fact('kim_Rule', {'number' : '4', 'test' : 'test2', 'bar_label' : 'false'})
assert_fact('kim_Rule', {'number' : '5', 'test' : 'test2', 'bar_label' : 'true'})

#Test 3 데이터 입력
assert_fact('kim_Rule', {'number' : '6', 'test' : 'test3', 'bar_db' : 'false'})
assert_fact('kim_Rule', {'number' : '7', 'test' : 'test3', 'bar_db' : 'true'})

#Test 4 데이터 입력
assert_fact('kim_Rule', {'number' : '8', 'test' : 'test4', 'cap_exist' : 'false'})
assert_fact('kim_Rule', {'number' : '9', 'test' : 'test4', 'cap_exist' : 'true'})

#Test 5 데이터 입력
assert_fact('kim_Rule', {'number' : '10', 'test' : 'test5', 'cap_color' : 'red', 'tube_length' : 60})
assert_fact('kim_Rule', {'number' : '11', 'test' : 'test5', 'cap_color' : 'red', 'tube_length' : 120})
assert_fact('kim_Rule', {'number' : '12', 'test' : 'test5', 'cap_color' : 'blue', 'tube_length' : 80})
assert_fact('kim_Rule', {'number' : '13', 'test' : 'test5', 'cap_color' : 'blue', 'tube_length' : 110})
assert_fact('kim_Rule', {'number' : '14', 'test' : 'test5', 'cap_color' : 'green', 'tube_length' : 50})
assert_fact('kim_Rule', {'number' : '15', 'test' : 'test5', 'cap_color' : 'green', 'tube_length' : 130})