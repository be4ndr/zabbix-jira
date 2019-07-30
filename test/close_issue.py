from base64 import main

from jira import JIRA
import config



def close_issue(issue, status):
    jira_server = {'server': config.jira_server, 'verify': config.jira_verify}
    jira = JIRA(options=jira_server, basic_auth=(config.jira_user, config.jira_pass))
    jira.transition_issue(issue, status)


close_issue('AB-28', '461')  # ZBX-2: Project key, 41: transition id for closing issue

if __name__ == '__main__':
    main()