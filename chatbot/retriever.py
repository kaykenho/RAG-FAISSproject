import requests


class DuckDuckGoSearchAPI:
    def __init__(self):
        self.endpoint = "https://api.duckduckgo.com/"

    def search(self, query):
        # Send GET request to DuckDuckGo API with the query
        params = {"q": query, "format": "json"}
        response = requests.get(self.endpoint, params=params)

        if response.status_code == 200:
            data = response.json()
            # Return related topics (snippets, answers)
            return data.get("RelatedTopics", [])
        else:
            return []


class DocumentRetriever:
    def __init__(self):
        self.ddg_search_api = DuckDuckGoSearchAPI()

    def retrieve_documents(self, query):
        # Retrieve documents from DuckDuckGo API related to the query
        results = self.ddg_search_api.search(query)

        # Extract relevant text snippets from results
        documents = [result.get('Text', '') for result in results]

        return documents
