# arxiv_toolkit_server.py
import argparse
import sys

from camel.toolkits import ArxivToolkit

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run Arxiv Toolkit with MCP server mode.",
        usage=f"python {sys.argv[0]} [--mode MODE]",
    )
    parser.add_argument(
        "--mode",
        choices=["stdio", "sse"],
        default="stdio",
        help="MCP server mode (default: 'stdio')",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=None,
        help="Timeout for the MCP server (default: None)",
    )

    args = parser.parse_args()

    toolkit = ArxivToolkit(timeout=args.timeout)

    # Run the toolkit as an MCP server
    toolkit.mcp.run(args.mode)