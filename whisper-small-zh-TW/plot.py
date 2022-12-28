import matplotlib.pyplot as plt
import json

dir_path = "./"

with open(dir_path + "trainer_state.json", "r") as f:
    data = json.load(f)

log = data["log_history"]

train_x = []
train_loss = []
eval_x = []
eval_wer = []

for item in log:
    if "eval_loss" in item:
        # evaluation log
        eval_x.append(item["step"])
        eval_wer.append(item["eval_wer"])
    if "loss" in item:
        train_x.append(item["step"])
        train_loss.append(item["loss"])

# evaluation
plt.figure(0)
plt.title("evaluation result")
plt.plot(eval_x, eval_wer, label='wer')
plt.legend()
plt.xlabel("steps")
plt.savefig(dir_path + 'eval.png')

# training
plt.figure(1)
plt.title("training result")
plt.plot(train_x, train_loss, label='loss')
plt.legend()
plt.xlabel("steps")
plt.savefig(dir_path + 'train.png')

print(f)
