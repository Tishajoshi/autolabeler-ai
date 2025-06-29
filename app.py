from labeler import classify_issue
from github_api import get_issues, apply_label

def main():
    issues = get_issues()
    
    # ✅ DEBUG: Show raw data from GitHub
    print("🧪 DEBUG: Raw issues returned:")
    print(issues)
    print(type(issues))

    for issue in issues:
        # Skip pull requests
        if 'pull_request' in issue:
            continue

        issue_number = issue['number']
        title = issue['title']
        body = issue['body'] or ""

        print(f"🔍 Labeling issue #{issue_number}: {title}")
        label = classify_issue(title, body)
        print(f"🏷️ Predicted label: {label}")
        apply_label(issue_number, label)
        print(f"✅ Applied label '{label}' to issue #{issue_number}\n")

if __name__ == "__main__":
    main()
