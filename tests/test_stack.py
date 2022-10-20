import pytest

def test_stack():  # проверяем работоспособность
    stack = []
    # Добавляем два элемента в стек и затем извлекаем их
    # Почему два? Так надежнее, чем один, а три скорее всего избыточно
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'
    assert stack.pop() == 'one'

def test_stack1():  # проверяем на извлечение
    stack = []
    stack.append('one')
    stack.append('two')

    assert stack.pop() == 'two'

def test_stack2():  # проверяем на остаток
    stack = []
    stack.append('one')
    stack.append('two')

    stack.pop()
    assert stack.pop() == 'one'

def test_emptiness():  # проверка на пустоту
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)  # not not stack

    stack.pop()
    assert not stack

def test_pop_with_empty_stack():  # проверка что стек не пустой
    stack = []
    with pytest.raises(IndexError):
        stack.pop()