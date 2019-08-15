from ..insert_into_db.format_data import FormatData

def test_dict_one_attribute():
    test_dict = {"test_1": "Hello"}
    assert FormatData(["should_fail"]).search_dict(test_dict) == test_dict


def test_dict_list():
    test_dict = {"test_1": [12,2,1,"Hi"]}
    assert FormatData(["should_fail"]).search_dict(test_dict) == test_dict

def test_search_dict_with_removed_attr():
    test_dict = {"test_1": [12,2,1,"Hi"], "should_fail": False}
    assert FormatData(["should_fail"]).search_dict(test_dict) == {"test_1": [12,2,1,"Hi"]}
    
def test_search_dict_with_removed_attr_in_sub_dict():
    test_dict = {"test_1": [12,2,1,"Hi"], "response":{"should_fail": False}}
    assert FormatData(["should_fail"]).search_dict(test_dict) == {"test_1": [12,2,1,"Hi"]}

def test_search_dict_with_multiple_removed_attr_one_in_sub_dict():
    test_dict = {"test_1": [12,2,1,"Hi"], "response":{"should_fail": False}, "removed": True}
    assert FormatData(["should_fail","removed"]).search_dict(test_dict) == {"test_1": [12,2,1,"Hi"]}

def test_search_dict_with_multiple_removed_attr_both_in_sub_dict():
    test_dict = {"test_1": [12,2,1,"Hi"], "response":{"should_fail": False}, "nest":{"removed": True}}
    assert FormatData(["should_fail","removed"]).search_dict(test_dict) == {"test_1": [12,2,1,"Hi"]}

def test_dict_sub_dict():
    test_dict = {"test_1": "Hello", "test_2":{"anAttribute": "Hello"}}
    assert FormatData(["should_fail"]).search_dict(test_dict) == test_dict

def test_search_dict_sub_sub_dict():
    test_dict = {"test_1": "Hello", "test_2":{"anAttribute": "Hello", "someAt": {"AnotherAt":1}}}
    assert FormatData(["should_fail"]).search_dict(test_dict) == test_dict
 