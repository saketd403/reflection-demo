import argparse


def get_args():

    parser = argparse.ArgumentParser(description='Reflection demo')

    parser.add_argument('--model', type=str, default="gpt-4o",
                        choices=["gpt-4o","gpt-4o-mini","o1","o1-mini","o3-mini"],
                        help='Choose ChatGPT model to use.')

    # 0.3 seems to be a good temperature for code generation
    parser.add_argument('--temperature', type=float, default=0.3,
                        help='Choose temperature to use with the model')

    parser.add_argument('--num_steps', type=int, default=5,
                        help='Max num of times to reflect to take for each user input.')

    args = parser.parse_args()

    return args

