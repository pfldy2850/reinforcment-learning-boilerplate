from agent import create_agent
from args import argparser
from env import create_env
from model import create_model
from system import create_system

if __name__ == "__main__":
    args = argparser()

    model = create_model(args.model)
    agent = create_agent(args.agent, model=model)
    env = create_env(args.env, agent=agent)
    system = create_system(
        args.system,
        env=env,
        model=model,
    )
