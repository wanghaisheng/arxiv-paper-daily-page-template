1.create new repo use this template                 


2. handwrite the topic.yml

how to choose better keywords, you can run your root keyword search agaisnt wos, use the filter mesh term to find out more relevant ones


infant:
  infant1: '"infant"or"neonatal"'
  infant2: '"infant"and"neonatal"'
  infant3: '"infant" or "neonatal"'
  infant4: '"infant "or"neonatal "'  
  infant5: '"infant "and"neonatal"'


for  or and operator，only  infants works


how to write complex query ,ple refer here

https://info.arxiv.org/help/api/user-manual.html#query_details


check yml format to be valid against https://www.yamllint.com/






The query string would look like this: image segmentation AND (cat:cs.CV OR cat:stat.ML OR cat:cs.LG). You could build this in query_with_keywords:

categories = ["cs.CV", "stat.ML", "cs.LG"]
category_condition = " OR ".join(["cat:" + c for c in categories]) # "cat:cs.CV OR cat:stat.ML OR cat:cs.LG"

def query_with_keywords(query):
    query_with_categories = "{} AND ({})".format(query, category_condition)
    search = arxiv.Search(
        query=query_with_categories,
        max_results=3000,
        sort_by=arxiv.SortCriterion.LastUpdatedDate
    )
    terms = []
    titles = []
    abstracts = []
    for res in tqdm(client.results(search), desc=query):
        terms.append(res.categories)
        titles.append(res.title)
        abstracts.append(res.summary)
    return terms, titles, abstracts
    
    
    

3. edit  mkdocs.yml 

4. replace with your own clarity

main/overrides/main.html


 
4.  run github action

