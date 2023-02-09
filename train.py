import torch
import yaml
from pytorch_lightning import Trainer
from pytorch_lightning.loggers import CSVLogger
from yaml import Dumper, Loader

from agent import create_agent
from args import get_args
from env import create_env
from model import create_model
from system import create_system

if __name__ == "__main__":
    args = get_args()

    # Config
    conf = yaml.load(open(args.config, "r"), Loader=Loader)

    # Environment
    env = create_env(args.env, **conf["env"])

    # Model
    model = create_model(
        args.model,
        observation_space=env.observation_space,
        action_space=env.action_space,
        **conf["model"]
    )
    print(model)

    # Agent
    agent = create_agent(args.agent, model=model, env=env, **conf["agent"])

    # System
    system = create_system(
        args.system, env=env, model=model, agent=agent, **conf["system"]
    )

    # Train
    trainer = Trainer(
        accelerator="cpu",
        devices=1 if torch.cuda.is_available() else None,  # limiting got iPython runs
        max_epochs=150,
        val_check_interval=50,
        logger=CSVLogger(save_dir="logs/"),
    )

    trainer.fit(
        system,
    )
