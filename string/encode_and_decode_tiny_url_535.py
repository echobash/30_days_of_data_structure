import base64


class Codec:
    def __init__(self):
        self.key = 1
        self.long_to_short_url_mapping = dict()
        self.short_to_long_url_mapping = dict()
        self.url_domain = 'https://tinyurl.com'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.long_to_short_url_mapping:
            return self.long_to_short_url_mapping[longUrl]

        self.long_to_short_url_mapping[longUrl] = str(base64.b64encode(str(self.key).encode("ascii")))
        self.short_to_long_url_mapping[str(base64.b64encode(str(self.key).encode("ascii")))] = longUrl
        self.key += 1
        return self.url_domain + '/' + self.long_to_short_url_mapping[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl.split('/')[-1] in self.short_to_long_url_mapping:
            return self.short_to_long_url_mapping[shortUrl.split('/')[-1]]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


sol = Codec()

s = "3902"
print(f"{s = }  {sol.encode('https://leetcode.com/problems/encode-and-decode-tinyurl')}")
print(sol.decode(sol.encode('https://leetcode.com/problems/encode-and-decode-tinyurl')))
