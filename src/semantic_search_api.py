import requests
import json

'''
    The search syntax used by Semantic Scholar can be found here:
    - https://api.semanticscholar.org/api-docs/graph#tag/Paper-Data/operation/get_graph_paper_bulk_search 
'''

# what are you looking for.
# exact searches for a term or set of terms must
# be enclosed with escaped quotation marks
query = "immune system immunology"

# fields to retrieve
fields = "title,abstract,isOpenAccess"
# querying from 2010 and onwards result in 100-200k papers, which creates a file too large for github
url = f"http://api.semanticscholar.org/graph/v1/paper/search/bulk?query={query}&fields={fields}&year=2015-"
r = requests.get(url).json()
total_docs = r['total']
print(f"Will retrieve an estimated {r['total']} documents")
retrieved = 0
document_content = ""

#string to append JSON content to
if total_docs > 0:
    document_content += "[\n"

while True:
    if "data" in r:
        #remove all items which are missing abstracts
        items = [x for x in r["data"] if x["abstract"]]
        curr_len = len(items)
        retrieved += curr_len 
        print(f"Retrieved {retrieved} papers...")
        for idx,paper in enumerate(items):
            # normal \t is usually 8 spaces, here we use four
            # since otherwise the actual JSON objects
            # will be strangely indented
            document_content += "\t".expandtabs(4)
            json_str = json.dumps(paper, indent=8,separators=(",",":"))
            '''
                weird string indexing to get correct formatting
                E.g. looks like this
                {
                    ...,
                    ...}
                which we transform to i.e. remove trailing newline and } and place it 
                in a "better" place
                -->
                {
                    ...,
                    ...
                }
            '''
            document_content += json_str[0:-2] + "\n\t".expandtabs(4)+json_str[-1]
            document_content += ",\n"
    if "token" not in r:
        break
    #retry using token to paginate more results, each REST call return a 1000 items
    r = requests.get(f"{url}&token={r['token']}").json()
document_content = document_content[0:-2] #this is ugly but otherwise format will be wack 
if total_docs > 0:
    document_content += "\n]"

#sanity check
if retrieved > 0:
    with open(f"../data/paper_abstracts.json", "w+") as file:
        file.write(document_content)
    print(f"Done! Retrieved {retrieved} papers total")
else: 
    print("Search resulted in no documents")
