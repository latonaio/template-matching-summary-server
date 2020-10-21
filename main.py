import sys


def main():
    try:
        from src.run import run
        run()
    except Exception:
        sys.exit(1)
    return


if __name__ == "__main__":
    main()
