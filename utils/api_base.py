from playwright.sync_api import Playwright

payload = {
    "order":[
        {
        "country": "India",
        "productOrderId": "6581ca399fd99c85e8ee7f45"
        }
    ]
}

class Base_api():

    def get_token(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com") #creates a new API request session with the given base URL.
                                                                                                        #The same context can be used for multiple API calls
        response = api_request_context.post("/api/ecom/auth/login",data={"userEmail":"rahulshetty@gmail.com","userPassword":"Iamking@000"}) #This sends login credentials to the authentication API.
        assert response.ok #Ensures the request was successful (i.e., status code 200-299).
                            #If the request fails, the script stops execution.
        resp_body = response.json() #Converts the response body to a JSON dictionary.
        return resp_body["token"]

    def create_order(self,playwright:Playwright):
        token = self.get_token(playwright)
        api_request_context = playwright.request.new_context(base_url= "https://rahulshettyacademy.com")
        response = api_request_context.post(url="/api/ecom/order/create-order",data=payload,headers={"Authorization":token,
                                                                                         "Content-Type":"application/json"})
        resp_body = response.json()
        print(resp_body)
        order_id = resp_body["orders"][0]
        return order_id