from pathlib import Path
import json
def save_outputs(inputs, labels, prompts, preds, args):
    if args.out_dir:
        out_path = Path(args.out_dir)
        out_path.mkdir(parents=True, exist_ok=True)

    res = []
    for input, label, prompt, pred in zip(inputs, labels, prompts, preds):
        res.append({
            'input': input,
            'prompt': prompt,
            'pred': pred,
            'label': label
        })
    with open(out_path / "results.json", "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)

    with open(out_path / "generation_params.json", "w", encoding="utf-8") as f:
        params = {
            "model": args.model,
            "dataset": args.dataset,
            "temperature": args.temperature,
            "max_tokens": args.max_tokens,
            'system_prompt': args.system_prompt,
            'form': args.form,
            'verbose': args.verbose,
        }

        params = {
            k: str(v) if not isinstance(v, (int, float)) else v
            for k, v in params.items()
        }
        json.dump(
            params,
            f,
            indent=4,
        )
