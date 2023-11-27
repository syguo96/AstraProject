def get_prompt(qas: list, form: str):
    if form == 'alpaca':
        prompt_no_input, prefix = get_alpaca_format_prompt_wo_input(qas)
    elif form == 'articulation':
        prompt_no_input, prefix = get_articulaton_prompt(qas)
    else:
        raise NotImplementedError(form)

    return  prompt_no_input, prefix

def get_articulaton_prompt(qas: list):
    #tmp = (
    #    "Below is a set of examples with input text and corresponding labels. They form part of a pattern matching exercise in a IQ test. The goal is to identify what property separates examples labelled True from those labelled False. "
    #    "Find a rule of thumb that explains whether an example text should be labelled True or False."
    #)
    tmp = (
        "Below is a pattern detection exercise. There are examples consisting of snippets of text as well as the corresponding labels. The labels are either 'True' or 'False'."
        "True means that the snippet of text matches a certain condition, False means that it does not."
        "Your task is to identify the condition. In particular, your task is to identify and articulate the rule that allows one to decide whther a given snippet should be labelled as True or False."
    )

    for q, a in qas:
        tmp += '\n' + '### Input:\n{query}\n\n### Label: {response}\n'.format(query=q, response=a)
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