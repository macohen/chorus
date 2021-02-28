import sys,json,requests

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print('Usage: push_common_rules.py <rules.txt> <http://<solr_host:port>/solr/<collection>/querqy/rewriter/<rewriter_name>')
        sys.exit(1)

    rules_file = sys.argv[1]
    rewriter_url = sys.argv[2]

    f = open(rules_file, "r")

    req = {
        "class": "querqy.solr.rewriter.commonrules.CommonRulesRewriterFactory",
        "config": {
            "rules" : f.read()
        }
    }

    resp = requests.post(rewriter_url + '?action=save', json=req)
    if resp.status_code != 200:
        sys.exit(2)
