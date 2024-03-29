"""
Download a specific folder from a github repo:
    gitget.py https://github.com/boppreh/keyboard/tree/master/examples
"""
__author__ = 'Divyansh Prakash'

import sys
import subprocess


def main():
    if len(sys.argv) > 1:
        github_src = sys.argv[1]

        try:
            head, branch_etc = github_src.split("/tree/")
            folder_url = "/".join(branch_etc.split("/")[1:])
        except:
            print("err:\tnot a valid folder url!")
        else:
            print("fetching...")
            subprocess.call(
                ["svn", "checkout", "/".join([head, "trunk", folder_url])]
            )
    else:
        print(
            "use:\tgitget.py https://github.com/user/project/tree/branch-name/folder\n"
        )
