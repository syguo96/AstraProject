"""
inference_openai.py - text generation with OpenAI API
    See https://platform.openai.com/docs/quickstart for more details.
Usage:
python inference_openai.py --prompt "The quick brown fox jumps over the lazy dog." --model "gpt-3.5-turbo" --temperature 0.5 --max_tokens 256 --n 1 --stop "."
Detailed usage:
python inference_openai.py --help
Notes:
- The OpenAI API key can be set using the OPENAI_API_KEY environment variable (recommended) or using the --api_key argument.
- This script supports inference with the "chat" models only.
"""
from typing import List, Optional, Union
from openai import OpenAI
from pathlib import Path
import logging
import json
from tqdm import tqdm
from data_loader import *
from prompt_utils import *
from utils import save_outputs
import argparse


##modes: alpaca, articulation
parser = argparse.ArgumentParser()
parser.add_argument("--model", default='gpt-3.5-turbo', type=str)
parser.add_argument("--out_dir", default='outputs/', type=str)
parser.add_argument("--dataset", default='Sums', type=str)
parser.add_argument("--form", default='alpaca', type=str)
parser.add_argument("--shots", default=8, type=int)
parser.add_argument("--verbose", action='store_true', default=True)
parser.add_argument("--temperature", default=0.5, type=float)
parser.add_argument("--max_tokens", default=256, type=int)
parser.add_argument("--system_prompt", default='You are a helpful assistant.', type=str)
# parser.add_argument("--cot_backup", action='store_true', default=False)

args = parser.parse_args()
def chat_completion(
    prompt: Optional[str] = None,
    model: str = "gpt-3.5-turbo",
    system_prompt: str = "You are a helpful assistant.",
    temperature: float = 0.5,
    max_tokens: int = 6,
):
    client = OpenAI(api_key='')

    completion = client.chat.completions.create(
      model=model,
      messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
      ],
      temperature=temperature,
      max_tokens=max_tokens,
    )
    generated_texts = [
                choice.message.content.strip() for choice in completion.choices
            ]

    return generated_texts

def main():
    logger = logging.getLogger(__name__)
    inputs, labels = data_reader(args.dataset)
    # set up output directory
    args.out_dir = args.out_dir + f"textgen-{args.model}-{args.dataset}".replace(".", "-")
    logger.info(f"Saving output to {args.out_dir}...")
    logger.info(f"Generating text for {args.dataset} using model:\t{args.model}...")
    used_examples = get_examples(args.dataset)
    prompt_no_input, prefix = get_prompt(used_examples, form=args.form)
    if args.form == 'articulation':
        outputs = chat_completion(
            prompt=prompt_no_input,
            model=args.model,
            system_prompt=args.system_prompt,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
        )
        if args.verbose:
            print(f'Input: {prompt_no_input} | Output: {outputs[0]} ')
    else:
        prompts = []
        preds = []
        for input, label in tqdm(zip(inputs, labels)):
            input_strs = prompt_no_input + prefix.format(query=input)
            outputs = chat_completion(
                prompt=input_strs,
                model=args.model,
                system_prompt=args.system_prompt,
                temperature=args.temperature,
                max_tokens=args.max_tokens,
            )
            preds.append(outputs[0])
            prompts.append(input_strs)
            if args.verbose:
                print(f'Input: {input} | Output: {outputs[0]} | Label: {label}')
        save_outputs(inputs, labels, prompts, preds, args)

if __name__ == "__main__":
    main()
