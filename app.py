from github_api import get_issues, apply_label
from labeler import classify_issue

def main():
    issues = get_issues()
    for issue in issues:
        if 'pull_request' in issue:
            continue  # skip PRs
        issue_number = issue['number']
        title = issue['title']
        body = issue['body'] or ""
        print(f"Labeling issue #{issue_number}: {title}")
        label = classify_issue(title, body)
        print(f"Predicted label: {label}")
        apply_label(issue_number, label)
        print(f"Applied label '{label}' to issue #{issue_number}\n")

if __name__ == "__main__":
    main()
