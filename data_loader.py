import json
import random
def data_reader(dataset: str):
    inputs = []
    labels = []
    # decoder = json.JSONDecoder()

    with open(f'datasets/{dataset}.json') as f:
        loaded = json.load(f)
    for d in loaded:
        inputs.append(d['text'])
        labels.append(d['label'])

    return inputs, labels

class BatchDatasetLoader:
    def __init__(self, dataset: str, batch_size: int):
        self.inputs, self.outputs = data_reader(dataset)
        self.index = 0
        self.batch_size = batch_size
        self.length = len(self.inputs)

    def __len__(self):
        return self.length // self.batch_size

    def __getitem__(self, index):
        if self.length % self.batch_size == 0:
            if index >= self.__len__():
                raise StopIteration
            else:
                tmp_inputs, tmp_outputs = [], []
                for i in range(index * self.batch_size, min((index + 1) * self.batch_size, self.length)):
                    tmp_inputs.append(self.inputs[i])
                    tmp_outputs.append(self.outputs[i])
                return tmp_inputs, tmp_outputs
        else:
            if index > self.__len__():
                raise StopIteration
            else:
                tmp_inputs, tmp_outputs = [], []
                for i in range(index * self.batch_size, min((index + 1) * self.batch_size, self.length)):
                    tmp_inputs.append(self.inputs[i])
                    tmp_outputs.append(self.outputs[i])
                return tmp_inputs, tmp_outputs

def get_examples(dataset):
    examples = []
    with open(f'datasets/{dataset}_example.json') as f:
        loaded = json.load(f)
    for d in loaded:
        example = tuple((d['text'], d['label']))
        examples.append(example)
    random.shuffle(examples)
    return examples


