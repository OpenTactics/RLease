#!/usr/bin/env python3

import numpy as np
import argparse
import pickle
from collections import OrderedDict
from trueskill import Rating, quality_1vs1, rate_1vs1
from rlease_utils import print_league_table, print_head_to_head, save_multiagent_results
import yaml

'''
Tools to help analyze the performance of agents in multi-agent zero sum games
'''

'''
last action:
  need to do play and print functions but kind of already have those on linux



conceptionally,
want an outer loop that takes agents, plays them against each other, gets results, display results

I'm thinking want an abstract class, then examples for specific classes since different envs, algs, and agents will be loaded and played against each other in different ways

Taking agents:
  load from json file or dict I think
    agent name, load dir, SP steps/version (then classess can do optional)
  Then class specific load
    abstract function that passes this

Play them against each other
  the trueskill loop, though trueskill can be a mode
  get trueskill, W-L-D, score, other stats from it

Display results
  print table
  head to head for each type
  order by trueskill with SP steps/version
  way to zoom in on each type
  plots

so minimal version of this is above with display results being minimal



to do
this runs but might want a class to stub out certain envs
some hard coded keys to fill in with constants
fill out the args and the args in the yaml dict

saving and loading
smarter save and load
better print



save different outputs
wandb, tensorboard, pandas, logging
seed everything
more eval types: ELO, None, Trueskill 2 etc
sampling type
zero sum or not

more effective way to load
more optional args to add
scan dir for more opponents or opponent descriptions from a json or python dict or something

way to tell if loop where unstable learning
  some sort of version number, ideally later versions are better
  tracking elo?
condition games on some variable to see if learning betterworse in some ways


'''


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--config-file",
        default=None,
        type=str,
        help="If specified, load arguments from yaml file specified by this path. Overrides all other argparse arguments.",
    )
    parser.add_argument('project-name', type=str, default='multiagent_zero_sum_analysis',
                        help='Name of project. Used in save file')
    parser.add_argument("--seed", type=int, default=0,
                        help="Seed for environment if applicable. If set to 0 defaults to None seed")
    parser.add_argument("--load-path", type=str, default="", help="Path to load results from")
    parser.add_argument("--print-and-quit", type=int, default=0, help="Load results, print them and quit")
    parser.add_argument("--num-games", type=int, default=1)

    parser.add_argument("--eval-type", type=str, default="", help="Path to load results from")

    return parser


def print_results():
    pass


def run(args, parser):
    # Get arguments
    if args.config_file:
        with open(args.config_file) as f:
            arg_dict = yaml.safe_load(f)
    else:
        arg_dict = {
            # to do, fill in args from dict
            'agents_path': args.agents_path,

        }

    # load agents: either inputted directly in yaml or a yaml file to load or a directory to scan for agent files
    if 'agents_dict' in arg_dict:
        pass
    elif 'agents_path' in arg_dict:
        pass
    elif 'agent_file' in arg_dict:
        agent_dict = yaml.safe_load(args_dict['agent_file'])
    else:
        print("ERROR: No agents specified to load, quitting")
        quit()

    # play agents against each other
    results_dict = play_game(TBD)

    # display results
    # league table sorted by skill, arg to show head to head stats, args/env specific for more skills
    # show skill, mu, WLD, score
    # I'm thinking just do pandas
    print_league_table(TBD)
    if 'print_head_to_head' in arg_dict:
        print_head_to_head(TBD)

    # save results
    save_multiagent_results(TBD, TBD)


def main():
    parser = create_parser()
    args = parser.parse_args()
    run(args, parser)


if __name__ == "__main__":
    main()