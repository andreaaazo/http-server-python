from .retrieve_form_data import retrieve_fields


def correct_results(answers: dict, responses_dict: dict):
    correct_responses = 0
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


def return_corrected_test(answers: dict, test_number: int):
    engine = open(f"templates/corrected_test{1}.html")
    file_page = engine.read()
    template = file_page.format()
    engine.close()
    return template
