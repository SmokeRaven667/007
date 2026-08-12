import sys
import urllib.request
import urllib.parse
import json

def query_api(endpoint):
    url = f"https://mattwood.fyi/api/fyi/q/{endpoint}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'ClaudeAgent/1.0'})
        with urllib.request.urlopen(req) as response:
            return json.dumps(json.loads(response.read().decode('utf-8')), indent=2)
    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fyi_client.py [search|semantic|summary|edges] [query_text/id]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "summary":
        print(query_api("summary"))
    elif command in ["search", "semantic", "edges"]:
        if len(sys.argv) < 3:
            print(f"Error: Command '{command}' requires an argument.")
            sys.exit(1)
        # Safely URL encode spaces and special characters for Windows execution
        query_param = urllib.parse.quote(sys.argv[2])
        print(query_api(f"{command}/{query_param}"))
