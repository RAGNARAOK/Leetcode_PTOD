# ------------------------------------------------------------------------------Approach 1 --------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------time complexity:O(K)-----------------------------------------------------------------------------



class ProductOfNumbers:
 
    def __init__(self):
        self.stack=[]
 
    def add(self, num: int) -> None:
        self.stack.append(num)
 
    def getProduct(self, k: int) -> int:
        self.temp = 1
        self.i = -1
        while k:
            self.temp = self.temp * self.stack[self.i]
            self.i =self.i-1
            k-=1
        return self.temp
 
 
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


# Approach 2 using prefix product method with time complexity O(1):
class ProductOfNumbers:
    def __init__(self):
        self.products = [1]  # Store running products, starting with 1
    
    def add(self, num: int) -> None:
        if num == 0:
            # If num is 0, reset products list as subsequent products will be 0
            self.products = [1]
        else:
            # Multiply the last product with current number
            self.products.append(self.products[-1] * num)
    
    def getProduct(self, k: int) -> int:
        if k > len(self.products) - 1:
            # If k is larger than our stored products (due to zeros), return 0
            return 0
            
        # Get product by dividing last product by product before the k window
        if k == len(self.products) - 1:
            return self.products[-1]
        return self.products[-1] // self.products[-(k+1)]
