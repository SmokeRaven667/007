# 007

repo sandbox for AI agent play

## matt wood

chief AI & tech officer at aws has experimental website optimized for AI agents

https://mattwood.fyi/

# Lets wire up Claude & Matt Wood FYI

## Step 1: Initialize your Claude Code agent directory

Open your terminal inside your project directory and create the standard configuration folder where Claude checks for custom agent files:

mkdir -p .claude/agents

## Step 2: Create the agent markdown file

Create a new file named matt_wood_fyi.md inside that directory:

touch .claude/agents/matt_wood_fyi.md

## Step 3: Paste the configuration and system prompt

Open matt_wood_fyi.md in your favorite text editor and paste the code block below. This configuration gives the agent permission to use your local curl tool to fetch his public REST endpoints, maps out his API, and instructs the agent exactly how to handle his data.

get matt's agent instructions: https://mattwood.fyi/agents/

## Step 4: Run your agent in Claude Code

Start your Claude Code session as normal. The platform will automatically parse the front matter in your .claude/agents/ folder — note the front matter block (`name`/`description`/`tools`) must be the very first thing in the file, starting with `---` on line 1, or it won't be recognized. You can now invoke your new agent by asking naturally in chat; Claude auto-delegates to it based on its `description` field, or you can ask explicitly:

"Use the matt-wood-fyi agent — what does Matt think about the middle class of software engineering?"

## The sub-agent will spin up, use the bash tool to run fyi_client.py against Matt's query API, read the returned JSON payload, and provide you with a cited answer.

## Step 5. Create Python Helper Script

Create a file named `fyi_client.py` in your project root folder. This script will safely fetch data from the API and format it nicely for your agent.

```python
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

```

## Step 6. Configure the Agent File

Create or update your agent markdown file at `.claude/agents/matt_wood_fyi.md`. We specify `Bash` as the tool (in the `tools:` front matter field) because the Claude Code runtime environment translates this internally to your Windows shell commands safely.

## Step 7. Run the Agent on Windows

Just ask Claude Code naturally — it will delegate to the subagent based on its description:

"What are the latest tensions or challenges Matt is looking at?"

> **Note:** Claude Code reads `.claude/agents/` once at session start. If you just created or edited `matt_wood_fyi.md`, the agent won't be invokable in your *current* session — start a new Claude Code session in this project directory before trying to use it.
