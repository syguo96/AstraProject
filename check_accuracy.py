import json
def compute_accuracy(dataset):
    preds = []
    labels = []
    with open(f'outputs/textgen-gpt-3-5-turbo-{dataset}/results.json') as f:
        loaded = json.load(f)
    for d in loaded:
        preds.append(d['pred'])
        labels.append(d['label'])
    acc = 0
    for pred, label in zip(preds, labels):
        if str(pred) == str(label):
            acc += 1
    acc /= len(labels)
    return acc

datasets = ['odd_even',
            'Sums',
            'lowercase_true_uppercase_false',
            'SentenceLength',
            'Question',
            'endsWithExclamation',
            'Apple',
            'Walnut',
            'Love',
            'Noun',
            'Verb',
            'Longer']
for dataset in datasets:
    acc = compute_accuracy(dataset)
    print(f'Dataset: {dataset} | Accuracy: {acc}')
