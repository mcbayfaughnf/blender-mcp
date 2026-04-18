from blender_mcp.server import main as server_main
import sys

# Personal fork: added version info on startup for easier debugging
def main():
    """Entry point for the blender-mcp package"""
    print(f"blender-mcp starting (personal fork) - Python {sys.version_info.major}.{sys.version_info.minor}")
    server_main()

if __name__ == "__main__":
    main()
