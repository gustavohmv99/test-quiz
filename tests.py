import pytest
from model import Question


@pytest.fixture
def question_with_multiple_choices():
    question = Question(title='q1', max_selections=2)
    first = question.add_choice('a')
    second = question.add_choice('b')
    third = question.add_choice('c')
    question.set_correct_choices([first.id, third.id])
    return question, first, second, third


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct


def test_add_choice_assigns_incremental_ids():
    question = Question(title='q1')

    first = question.add_choice('a')
    second = question.add_choice('b')

    assert first.id == 1
    assert second.id == 2


def test_add_choice_rejects_empty_text():
    question = Question(title='q1')

    with pytest.raises(Exception, match='Text cannot be empty'):
        question.add_choice('')


def test_add_choice_rejects_text_longer_than_100_characters():
    question = Question(title='q1')

    with pytest.raises(Exception, match='Text cannot be longer than 100 characters'):
        question.add_choice('a' * 101)


def test_remove_choice_by_id_removes_only_target_choice():
    question = Question(title='q1')
    first = question.add_choice('a')
    second = question.add_choice('b')

    question.remove_choice_by_id(first.id)

    assert len(question.choices) == 1
    assert question.choices[0].id == second.id


def test_remove_choice_by_id_raises_for_unknown_id():
    question = Question(title='q1')
    question.add_choice('a')

    with pytest.raises(Exception, match='Invalid choice id 99'):
        question.remove_choice_by_id(99)


def test_remove_all_choices_clears_choices_list():
    question = Question(title='q1')
    question.add_choice('a')
    question.add_choice('b')

    question.remove_all_choices()

    assert question.choices == []


def test_set_correct_choices_marks_only_informed_ids_as_correct():
    question = Question(title='q1')
    first = question.add_choice('a')
    second = question.add_choice('b')

    question.set_correct_choices([second.id])

    assert question.choices[0].is_correct is False
    assert question.choices[1].is_correct is True
    assert first.id != second.id


def test_set_correct_choices_raises_for_unknown_id():
    question = Question(title='q1')
    question.add_choice('a')

    with pytest.raises(Exception, match='Invalid choice id 2'):
        question.set_correct_choices([2])


def test_correct_selected_choices_returns_only_selected_correct_ids():
    question = Question(title='q1', max_selections=2)
    first = question.add_choice('a')
    second = question.add_choice('b')
    third = question.add_choice('c')
    question.set_correct_choices([first.id, third.id])

    corrected = question.correct_selected_choices([first.id, second.id])

    assert corrected == [first.id]


def test_correct_selected_choices_raises_when_selection_exceeds_limit():
    question = Question(title='q1', max_selections=1)
    first = question.add_choice('a')
    second = question.add_choice('b')

    with pytest.raises(Exception, match='Cannot select more than 1 choices'):
        question.correct_selected_choices([first.id, second.id])


def test_fixture_correct_selected_choices_returns_only_correct_ids(question_with_multiple_choices):
    question, first, second, _ = question_with_multiple_choices

    corrected = question.correct_selected_choices([first.id, second.id])

    assert corrected == [first.id]


def test_fixture_remove_choice_by_id_updates_remaining_ids(question_with_multiple_choices):
    question, first, _, third = question_with_multiple_choices

    question.remove_choice_by_id(first.id)

    remaining_ids = [choice.id for choice in question.choices]
    assert remaining_ids == [2, 3]
    assert third.id in remaining_ids