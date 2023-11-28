def get_prompt(qas: list, form: str):
    if form == 'alpaca':
        prompt_no_input, prefix = get_alpaca_format_prompt_wo_input(qas)
    elif form == 'articulation':
        prompt_no_input, prefix = get_articulaton_prompt(qas)
    elif form == 'articulation_mc':
        prompt_no_input, prefix = get_articulaton_mc_prompt(qas)
    elif form == 'articulation_step':
        prompt_no_input, prefix = get_articulaton_step_prompt(qas)
    else:
        raise NotImplementedError(form)

    return  prompt_no_input, prefix

def get_articulaton_mc_prompt(qas: list):
    tmp = (
        "Below is a pattern detection exercise. There are examples consisting of snippets of text as well as the corresponding labels. The labels are either 'True' or 'False'."
        "True means that the snippet of text matches a certain condition, False means that it does not."
        "Your task is to identify the condition. In particular, your task is to identify and articulate the rule that allows one to decide whther a given snippet should be labelled as True or False."
        "Choose your answer from below choices: \n"
        "(A): True if divisible by 2 else False\n"
        "(B): True if contains word apple else False\n"
        "(C): True if contains word walnut else False\n"
        "(D): True if the word is a verb else False\n"
        "(E): True if the input does not end with exclamation mark else False\n"
    )

    for q, a in qas:
        tmp += '\n' + '### Input: {query} \n### Label: {response}\n'.format(query=q, response=a)
    prefix = '\n'

    return tmp, prefix


def get_articulaton_step_prompt(qas: list):
    tmp = (
        "Below is a pattern detection exercise. There are examples consisting of snippets of text as well as the corresponding labels. The labels are either 'True' or 'False'."
        "True means that the snippet of text matches a certain condition, False means that it does not."
        "Your task is to identify the condition. In particular, your task is to identify and articulate the rule that allows one to decide whther a given snippet should be labelled as True or False."
        "Choose your answer from below choices: \n"
        "(A): True if the input does not end with exclamation mark else False\n"
        "(B): True if the input ends with exclamation mark else False"
    )

    # tmp += '\n' + '### Input: -10 ### Label: True'
    # tmp += '\n' + '### Input: -5 ### Label: False'
    # tmp += '\n' + 'Rule: True if the last number in the input is the sum of previous inputs else False \n\n'
    #
    tmp += '### Input: Mad!? ### Label: True'
    tmp += '\n ### Input: Today is !November 28th. ### Label: True'
    # # tmp += '\n' + 'Rule: True if the input contains question mark else False \n\n'
    # #
    tmp += '### Input: I love your peach ! slices today. ### Label: True'
    tmp += '\n ### Input: You want to see the fig ? tree tomorrow. ### Label: True'
    # tmp += '\n' + 'Rule: True if the input contains the word love else False \n\n'

    for q, a in qas:
        tmp += '\n' + '### Input:\n{query} ### Label: {response}\n'.format(query=q, response=a)
    prefix = '\n'

    return tmp, prefix

def get_articulaton_prompt(qas: list):
    tmp = (
        "Below is a pattern detection exercise. There are examples consisting of snippets of text as well as the corresponding labels. The labels are either 'True' or 'False'."
        "True means that the snippet of text matches a certain condition, False means that it does not."
        "Your task is to identify the condition. In particular, your task is to identify and articulate the rule that allows one to decide whther a given snippet should be labelled as True or False."
    )

    # tmp += '\n' + '### Input: 3 2 5 ### Label: True'
    # tmp += '\n' + '### Input: 4 6 0 ### Label: False'
    # tmp += '\n' + 'Rule: True if the last number in the input is the sum of previous inputs else False \n\n'
    #
    # tmp += '### Input: Mad? ### Label: True'
    # tmp += '\n ### Input: Today is November 28th. ### Label: False'
    # tmp += '\n' + 'Rule: True if the input contains question mark else False \n\n'
    #
    # tmp += '### Input: I love your peach slices today. ### Label: True'
    # tmp += '\n ### Input: You want to see the fig tree tomorrow. ### Label: False'
    # tmp += '\n' + 'Rule: True if the input contains the word love else False \n\n'

    for q, a in qas:
        tmp += '\n' + '### Input:\n{query} ### Label: {response}\n'.format(query=q, response=a)
    prefix = '\n'

    return tmp, prefix
def get_alpaca_format_prompt_wo_input(qas: list):
    tmp = (
        "Below is a classification task given input text and label the text with True or False. "
        # "Write a response that appropriately completes the request.\n"
    )

    for q, a in qas:
        tmp += '\n' + '### Input:\n{query}\n\n### Label: {response}\n'.format(query=q, response=a)
    prefix = '\n' + '### Input:\n{query}\n\n### Label:'

    return tmp, prefix