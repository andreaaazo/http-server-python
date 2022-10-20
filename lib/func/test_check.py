from .retrieve_form_data import retrieve_fields


def correct_results(handler: object, values_list: list, answers: dict):
    correct_responses = 0
    responses_dict = retrieve_fields(handler, values_list)
    print(responses_dict)
    for i in responses_dict:
        if responses_dict[i] == answers[i]:
            correct_responses += 1
    return correct_responses


def calculate_mark(correct_responses_number: int, answers: int):
    result = int((correct_responses_number / answers) * 6)
    if result <= 3:
        return 3
    else:
        return result
