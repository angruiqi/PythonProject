import requests
import scrapy
import unittest


# requesting for a get request from https://www.nike.com/sg/
url = "https://brickset.com/sets/year-2005"
user_agent = {'User-Agent': 'Mobile'}
r = requests.get(url)

#Status Code
print("Status code:")
print("\t *", r.status_code)

# Requesting for web header
h = requests.head(url)
print("Web Header:")
print("**********")

# To print out the Web Header line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

# Requesting for CLient header then printing it out
response = requests.get(url, headers=user_agent)
print("User-Agent:,")
print("**********")
print(response.request.headers)
print("**********")



    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                    'Image Link': x.xpath(newsel).extract_first(),
            }


        )

# a unit test to test out the code
class TestMyProgram(unittest.TestCase):
    url2 = 'https://brickset.com/sets/year-2005'
    headers = {'User-Agent': 'Mobile'}
    rh = requests.get(url2, headers=headers)
    statuscode = rh.status_code
    user_agent = rh.request.headers

#testing the status code
    def test_statuscode(self):
        self.assertEqual(TestMyProgram.statuscode, 200)

#testing the user-agent
    def test_headers(self):
        self.assertTrue(TestMyProgram.user_agent, "Mobile")


        
if __name__ == '__main__':
    unittest.main()
