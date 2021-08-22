from .tag_from_spotify import tfsp
import fire
import sys
from ._version import version

def main():
    if (any(a in sys.argv[1:] for a in ("-V", "--version"))):
        print(version)
        sys.exit()
    fire.Fire(tfsp)

if __name__ == '__main__':
    main()