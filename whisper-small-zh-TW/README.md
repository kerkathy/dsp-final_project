---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: whisper-small-zh-TW
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 zh-TW
      type: mozilla-foundation/common_voice_11_0
      args: zh-TW
    metrics:
    - name: Wer
      type: wer
      value: 0.4098534720747505
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-small-zh-TW

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the mozilla-foundation/common_voice_11_0 zh-TW dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2434
- Wer: 0.4099

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.1574        | 2.84  | 1000 | 0.1987          | 0.4092 |
| 0.0149        | 5.68  | 2000 | 0.2250          | 0.4028 |
| 0.0021        | 8.52  | 3000 | 0.2324          | 0.4035 |
| 0.0007        | 11.36 | 4000 | 0.2402          | 0.4084 |
| 0.0005        | 14.2  | 5000 | 0.2434          | 0.4099 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.11.0+cu102
- Datasets 2.7.1
- Tokenizers 0.13.2
