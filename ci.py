import wandb
import os

print(f'This is the version of wandb: {wandb.__version__}')
assert wandb.__version__ == '0.10.33', f'Expected version 0.10.33, but got {wandb.__version__}'
# wandb.login()