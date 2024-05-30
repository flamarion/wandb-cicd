import wandb
import os

print(f'This is the version of wandb: {wandb.__version__}')
assert wandb.__version__ == '0.17.0', f'Expected version 0.17.0, but got {wandb.__version__}'
# wandb.login()