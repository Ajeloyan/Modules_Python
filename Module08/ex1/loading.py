import sys
import importlib


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()

    print("Checking dependencies:")
    try:
        pd = importlib.import_module('pandas')
        print(f"[OK] {pd.__name__} ({pd.__version__}) - Data manipulation "
              "ready")
    except (ImportError, AttributeError):
        print("pandas missing")
        sys.exit(1)
    try:
        rq = importlib.import_module('requests')
        print(f"[OK] {rq.__name__} ({rq.__version__}) - Network access ready")
    except (ImportError, AttributeError):
        print("requests missing")
        sys.exit(1)
    try:
        mpl = importlib.import_module('matplotlib')
        plt = importlib.import_module('matplotlib.pyplot')
        print(f"[OK] {mpl.__name__} ({mpl.__version__}) - Visualization ready")
    except (ImportError, AttributeError):
        print("matplotlib missing")
        sys.exit(1)
    try:
        np = importlib.import_module('numpy')
    except (ImportError, AttributeError):
        print("numpy missing")
        sys.exit(1)
    print()
    print("Analyzing Matrix data...")
    array_x = np.array([x for x in range(1000)])
    array_y = np.array([y for y in range(1000)])

    print("Processing 1000 data points...")
    x = pd.Series(array_x)
    y = pd.Series(array_y)

    print("Generating visualization...")
    plt.plot(x, y)
    plt.savefig("matrix_analysis.png")

    print()
    print("Analysis complete!")
    print("Result saved to: matrix\\_analysis.png}")


if __name__ == "__main__":
    main()
