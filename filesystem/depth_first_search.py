#!/usr/bin/env python3

"""
Author: ilyi
Date: September 12, 2023
"""

import os
import re

def dfs(root, target):
    """
    Depth-first search algorithm to search for files with specific extensions
    """
    stack = [root]
    target = re.compile(target)
    results = []

    while stack:
        curr_node = stack.pop()
        # print(curr_node)
        if os.path.exists(curr_node):
            for entry in os.listdir(curr_node):
                entry_path = os.path.join(curr_node, entry)
                if os.path.isdir(entry_path):
                    stack.append(entry_path)
                
                elif bool(target.search(entry_path)):
                    results.append(entry_path)
    return results


if __name__ == '__main__':
    # Argument parsing
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=str, required=True, help='Root directory')
    args = parser.parse_args()


    root = args.root
    # Extensions to search for
    extensions = ['jpg', 'jpeg', 'png']
    # Create target regex
    target = '|'.join([f'\.{ext}$' if ext.isalpha() else exit("[ERROR] The extensions must be alphabetic only.")for ext in extensions])

    results = dfs(root, target)

    print(results)