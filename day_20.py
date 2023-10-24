class Solution:
    def __init__(self):
        self.url_map = {}  # Initialize a dictionary to store mappings between tiny URLs and long URLs
        self.base_url = "http://tinyurl.com/"  # Define a base URL for the tiny URLs
        self.counter = 0  # Initialize a counter to generate unique keys

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        # Check if the long URL is already in the mapping
        if longUrl in self.url_map:
            return self.url_map[longUrl]
        else:
            # Generate a unique key for the long URL and create a tiny URL
            self.counter += 1
            tiny_url = self.base_url + str(self.counter)
            self.url_map[longUrl] = tiny_url
            self.url_map[tiny_url] = longUrl  # Add a reverse mapping for decoding
            return tiny_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.url_map.get(shortUrl, None)

# Example usage:
url = "https://github.com/HavaleShreyash/100-Days-Of-Code-Challenge"
obj = Solution()
tiny = obj.encode(url)
ans = obj.decode(tiny)
print(ans) 
