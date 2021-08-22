from .tag_from_spotify import tfsp
import fire
import sys
from ._version import version

def print_version(ver):
    print("tag-from-spotify", ver)
    sys.exit()

def main():
    if (any(a in sys.argv[1:] for a in ("-V", "--version"))):
        print_version(version)
    fire.Fire(tfsp)

if __name__ == '__main__':
    main()