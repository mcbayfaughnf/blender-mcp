from blender_mcp.server import main as server_main

# Personal fork: added version info on startup for easier debugging
def main():
    """Entry point for the blender-mcp package"""
    print("blender-mcp starting (personal fork)")
    server_main()

if __name__ == "__main__":
    main()
